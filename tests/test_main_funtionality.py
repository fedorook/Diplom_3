import allure
import pytest
from src.pages.constructor_page import ConstructorPage
from src.helpers.urls import URLS

@allure.feature("Core Functionality")
class TestMainFunctionality:
    """Tests covering main navigation and order operations."""

    @allure.story("Navigate to Constructor with authentication")
    def test_click_on_constructor(self, driver, login_user):
        # Access personal account to ensure authentication
        login_user.click_on_personal_account()

        page = ConstructorPage(driver)
        page.click_on_constructor()

        assert page.get_current_url() == URLS.BASE_URL

    @allure.story("Navigate to Constructor without authentication")
    def test_click_on_constructor_without_login(self, driver):
        page = ConstructorPage(driver)
        page.open_login_page()
        page.click_on_constructor()

        assert page.get_current_url() == URLS.BASE_URL

    @allure.story("Navigate to Orders Feed with authentication")
    def test_click_on_orders_feed(self, driver, login_user):
        page = ConstructorPage(driver)
        page.click_on_orders_feed()

        assert page.get_current_url() == URLS.ORDERS_FEED_PAGE

    @allure.story("Navigate to Orders Feed without authentication")
    def test_click_on_orders_feed_without_login(self, driver):
        page = ConstructorPage(driver)
        page.open_login_page()
        page.click_on_orders_feed()

        assert page.get_current_url() == URLS.ORDERS_FEED_PAGE

    @allure.story("Display ingredient details")
    @allure.title("Display ingredient details: {index}")
    @pytest.mark.parametrize("index", [0, 5, 10])
    def test_get_ingredient_info(self, driver, index):
        page = ConstructorPage(driver)
        page.open_base_page()
        ingredient_info = page.click_on_ingredient_info(index)

        assert ingredient_info.is_displayed() is True

    @allure.story("Close ingredient details display")
    @allure.title("Close ingredient details: {index}")
    @pytest.mark.parametrize("index", [0, 5, 10])
    def test_close_ingredient_info(self, driver, index):
        page = ConstructorPage(driver)
        page.open_base_page()
        ingredient_info = page.click_on_ingredient_info(index)

        page.click_on_close_ingredient_info()
        assert ingredient_info.is_displayed() is False

    @allure.story("Increment ingredient counter")
    def test_add_ingredient_to_order(self, driver):
        page = ConstructorPage(driver)
        page.open_base_page()

        index = 6
        initial_count = page.get_counter_value(index)
        assert initial_count == 0

        page.add_ingredient_to_order(index)
        new_count = page.get_counter_value(index)
        assert new_count > initial_count

    @allure.story("Submit order")
    def test_submit_order(self, driver, login_user):
        page = ConstructorPage(driver)
        page.add_bun_to_order()
        page.add_ingredient_to_order()

        confirmation = page.submit_order()
        assert confirmation.is_displayed() is True
