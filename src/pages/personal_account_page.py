import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers.urls import URLS


class PersonalAccountPage(BasePage):
    """
    Page object for the user's personal account functionality.
    """

    EMAIL_INPUT: tuple = (
        By.XPATH,
        '//label[text()="Email"]/following-sibling::input'
    )
    PASSWORD_INPUT: tuple = (
        By.XPATH,
        '//label[text()="Пароль"]/following-sibling::input'
    )
    LOGIN_BUTTON: tuple = (
        By.XPATH,
        '//button[text()="Войти"]'
    )
    PERSONAL_ACCOUNT_LINK: tuple = (
        By.XPATH,
        '//a[@href="/account"]'
    )
    ORDER_HISTORY_BUTTON: tuple = (
        By.XPATH,
        '//a[text()="История заказов"]'
    )
    LOGOUT_BUTTON: tuple = (
        By.XPATH,
        '//button[text()="Выход"]'
    )

    ORDER_LIST_ITEMS: tuple = (
        By.XPATH,
        "//li[contains(@class,'OrderHistory_listItem__')]"
    )
    ORDER_NUMBER: tuple = (
        By.XPATH,
        ".//p[@class='text text_type_digits-default']"
    )

    @allure.step("Open login page")
    def get_login_page(self) -> None:
        """Navigate to the login page."""
        self.get_page(URLS.LOGIN_PAGE)

    @allure.step("Click on personal account")
    def click_on_personal_account(self) -> None:
        """Click the personal account link and wait for the profile page."""
        self.click_on_with_execute_script(self.PERSONAL_ACCOUNT_LINK)
        self.wait_for_page(URLS.PROFILE_PAGE)

    @allure.step("Enter user credentials")
    def enter_login_field(self, email: str, password: str) -> None:
        """Fill in the email and password fields."""
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)

    @allure.step("Click login")
    def click_on_login(self) -> None:
        """Click the login button and wait for the base URL to load."""
        self.click_on_with_execute_script(self.LOGIN_BUTTON)
        self.wait_for_page(URLS.BASE_URL)

    @allure.step("Click on order history")
    def click_on_order_history(self) -> None:
        """Click the order history button and wait for that page."""
        self.wait_for_element_to_be_clickable(self.ORDER_HISTORY_BUTTON)
        self.click_on(self.ORDER_HISTORY_BUTTON)
        self.wait_for_page(URLS.ORDER_HISTORY_PAGE)

    @allure.step("Click logout")
    def click_on_logout(self) -> None:
        """Click the logout button and navigate back to the login page."""
        self.click_on(self.LOGOUT_BUTTON)
        self.wait_for_page(URLS.LOGIN_PAGE)

    @allure.step("Retrieve order history items")
    def get_orders(self) -> list:
        """Return a list of order history elements."""
        self.wait_for_element_to_be_visible(self.ORDER_LIST_ITEMS)
        return self.find_elements(self.ORDER_LIST_ITEMS)

    @allure.step("Get order number text")
    def get_order_number(self) -> str:
        """Extract and return the text of an order number element."""
        elem = self.wait_for_element_to_be_visible(self.ORDER_NUMBER)
        return elem.text.strip()