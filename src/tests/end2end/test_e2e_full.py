import allure
import pytest


class TestE2E(object):

    @allure.title("E2E - Create Booking -> Update -> Delete(Verify)")
    @allure.description(
        "Verify that created booking id when we update we are able to update it and delete it also | Full CRUD")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1", name="E2ETC1")
    def test_update_booking_with_id_token(self, create_token, get_booking_id):
        pass

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description(
        "Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self, create_token, get_booking_id):
        pass
