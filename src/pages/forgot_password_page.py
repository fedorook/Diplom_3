import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers.urls import URLS


class ForgotPasswordPage(BasePage):
    """
    Page object for handling the 'Forgot Password' workflow.
    """

    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[contains(text(),'Восстановить пароль')]"
    )
    SHOW_HIDE_PASSWORD = (
        By.XPATH,
        "//div[contains(@class, 'input__icon')]"
    )
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//label[text()='Пароль']/following-sibling::input"
    )
    RECOVER_BUTTON = (
        By.XPATH,
        "//button[text()='Восстановить']"
    )

    @allure.step("Navigate to login page")
    def get_login_page(self) -> None:
        """Open the login page."""
        self.get_page(URLS.LOGIN_PAGE)

    @allure.step("Navigate to forgot password page")
    def get_forgot_password_page(self) -> None:
        """Open the forgot password page."""
        self.get_page(URLS.FORGOT_PASSWORD_PAGE)

    @allure.step("Click 'Forgot Password' link")
    def click_on_forgot_password_link(self) -> None:
        """Click the link to access the forgot password form."""
        self.click_on_with_execute_script(self.FORGOT_PASSWORD_LINK)
        self.wait_for_page(URLS.FORGOT_PASSWORD_PAGE)

    @allure.step("Enter email for password recovery")
    def enter_email(self, email: str) -> None:
        """Type the email address into the recovery field."""
        self.send_keys(self.EMAIL_INPUT, email)

    @allure.step("Click 'Recover' button")
    def click_on_recover_button(self) -> None:
        """Submit the recovery request."""
        self.click_on(self.RECOVER_BUTTON)
        self.wait_for_page(URLS.RESET_PASSWORD_PAGE)

    @allure.step("Navigate to reset password page and perform recovery flow")
    def get_reset_password_page(self, email: str) -> None:
        """Complete the full recovery process: open forgot-password page, enter email, and submit."""
        self.get_forgot_password_page()
        self.enter_email(email)
        self.click_on_recover_button()

    @allure.step("Enter new password")
    def enter_password(self, password: str) -> None:
        """Type the new password into the reset field."""
        self.send_keys(self.PASSWORD_INPUT, password)

    @allure.step("Toggle password visibility")
    def click_on_show_hide_password(self) -> None:
        """Show or hide the password using the visibility toggle."""
        self.click_on_with_execute_script(self.SHOW_HIDE_PASSWORD)

    @allure.step("Get password input element")
    def get_password_field(self):
        """Return the WebElement for the password input field."""
        return self.find_element(self.PASSWORD_INPUT)
