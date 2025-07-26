import allure
from src import URLS
from conftest import driver, login_user


@allure.feature('Personal Account')
class TestPersonalAccount:

    @allure.story('Navigate to Personal Account')
    def test_personal_account(self, driver, login_user):
        """
        Verify that clicking the Personal Account link navigates to the profile page.
        """
        page = login_user
        page.click_on_personal_account()
        assert page.get_current_url() == URLS.PROFILE_PAGE

    @allure.story('Logout from account')
    def test_logout(self, driver, login_user):
        """
        Ensure that logging out redirects the user to the login page.
        """
        page = login_user
        page.click_on_personal_account()
        page.click_on_logout()
        assert page.get_current_url() == URLS.LOGIN_PAGE

    @allure.story('Navigate to Order History')
    def test_order_history(self, driver, login_user):
        """
        From the Personal Account, navigate to the Order History section.
        """
        page = login_user
        page.click_on_personal_account()
        page.click_on_order_history()
        assert page.get_current_url() == URLS.ORDER_HISTORY_PAGE