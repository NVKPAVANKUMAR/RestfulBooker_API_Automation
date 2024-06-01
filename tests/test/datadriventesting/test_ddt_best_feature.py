# Read the CSV or EXCEL file
# Create a Function create_token which can take values from the Excel File
# Verify the Expected Result.

# Read the Excel - openpyxl
import openpyxl
import pytest
import os
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.utils.utils import Util


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append(({
            "username": username,
            "password": password
        }))
    return credentials


def create_auth_request(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = post_request(
        url=APIConstants.url_create_token(),
        headers=Util().common_headers_json(),
        auth=None,
        payload=payload,
        in_json=False
    )
    return response


def getfilepath():
    absolute_path = os.path.dirname(__file__)
    relative_path = "/mock_test_data.xlsx"
    file_path = absolute_path + relative_path
    return file_path


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(getfilepath()))
def test_create_auth_with_excel(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    response = create_auth_request(username=username, password=password)
    print(response.status_code)