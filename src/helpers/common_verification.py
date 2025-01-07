# Common Verification

# HTTP Status Code
# Headers
# Data Verification
# JSON schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed to match status Code"


def verify_response_key(key, expected_data):
    assert key == expected_data, "Failed to match the key"


def verify_json_key_not_null(key):
    assert key != 0, "Failed Key is null"


def verify_json_key_not_none(key):
    assert key is not None


def verify_json_key_gr_zero(key):
    assert key > 0, "Failed Key is not > 0"


def verify_response_delete(response):
    assert "Created" in response