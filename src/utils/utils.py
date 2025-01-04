# Contains common utilities
# read data from the excel file
# read data from the csv,json file
# set the headers - application/json , application/xml

class Utils(object):
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml",
        }
        return headers

    def common_header_put_delete_patch_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers

    def common_header_put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic " + str(basic_auth_value),
        }
        return headers
