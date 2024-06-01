# class or functions
class Util(object):

    @staticmethod
    def common_headers_json():
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    @staticmethod
    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    @staticmethod
    def common_headers_put_delete_patch_basic_auth(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }
        return headers

    @staticmethod
    def common_header_put_delete_patch_cookie(token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers

    @staticmethod
    def read_csv_file(self):
        pass

    @staticmethod
    def read_env_file(self):
        pass

    @staticmethod
    def read_database(self):
        pass
