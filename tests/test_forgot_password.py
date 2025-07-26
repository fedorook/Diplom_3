import allure
from src.pages.forgot_password_page import ForgotPasswordPage
from src.helpers.urls import URLS

@allure.feature("Password Recovery")
class TestForgotPassword:
    """Tests for the forgotten-password workflow."""

    @allure.story("Navigate to forgot-password page via 'Forgot Password' link")
    def test_go_to_forgot_password_page(self, driver):
        page = ForgotPasswordPage(driver)
        page.get_login_page()
        page.click_on_forgot_password_link()

        assert page.get_current_url() == URLS.FORGOT_PASSWORD_PAGE

    @allure.story("Enter email and click 'Recover' button")
    def test_enter_email_and_click_recover(self, driver, user_data):
        page = ForgotPasswordPage(driver)
        page.get_forgot_password_page()

        page.enter_email(user_data["email"])
        page.click_on_recover_button()

        assert page.get_current_url() == URLS.RESET_PASSWORD_PAGE

    @allure.story("Toggle password visibility activates the field")
    def test_show_hide_password(self, driver, user_data):
        page = ForgotPasswordPage(driver)
        page.get_reset_password_page(user_data["email"])

        page.enter_password(user_data["password"])
        password_field = page.get_password_field()

        assert password_field.get_attribute("type") == "password"
        page.click_on_show_hide_password()
        assert password_field.get_attribute("type") == "text"