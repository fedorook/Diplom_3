import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers.urls import URLS


class OrderFeedPage(BasePage):
    """
    Page object for interacting with the orders feed section.
    """

    # Locators (keeping Russian text for stability)
    ORDER_LIST_ITEMS: tuple = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_list')]/li"
    )
    ORDERS_FEED_HEADER: tuple = (
        By.XPATH,
        '//*[contains(text(),"Лента Заказов")]'
    )
    ORDER_INFO: tuple = (
        By.XPATH,
        '//p[contains(text(),"Cостав")]'
    )

    TOTAL_COUNT: tuple = (
        By.XPATH,
        '//p[contains(text(),"Выполнено за все время:")]/following-sibling::*'
    )
    TODAY_COUNT: tuple = (
        By.XPATH,
        '//p[contains(text(),"Выполнено за сегодня:")]/following-sibling::*'
    )

    IN_PROGRESS: tuple = (
        By.XPATH,
        '//*[contains(@class,"OrderFeed_orderListReady_")]'
    )
    ORDER_NUMBERS_LIST: tuple = (
        By.XPATH,
        ".//p[@class='text text_type_digits-default']"
    )
    ORDER_STATUS: tuple = (
        By.XPATH,
        ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[@class='text text_type_digits-default mb-2']"
    )

    @allure.step("Open orders feed page")
    def get_feed_page(self) -> None:
        """Navigate to the orders feed URL."""
        self.get_page(URLS.ORDERS_FEED_PAGE)

    @allure.step("Click on orders feed header")
    def click_on_orders_feed(self) -> None:
        """Click the feed header and wait for the page to load."""
        self.click_on_with_execute_script(self.ORDERS_FEED_HEADER)
        self.wait_for_page(URLS.ORDERS_FEED_PAGE)

    @allure.step("Get list of orders in feed")
    def get_orders(self):
        """Return all order elements from the feed."""
        self.wait_for_element_to_be_visible(self.ORDER_LIST_ITEMS)
        return self.find_elements(self.ORDER_LIST_ITEMS)

    @allure.step("Click on a specific order")
    def click_on_order(self, index: int):
        """Scroll to and click an order, returning its info panel."""
        order = self.get_orders()[index]
        self.scroll_to_element(order)
        order.click()
        return self.wait_for_element_to_be_visible(self.ORDER_INFO)

    @allure.step("Get total orders count")
    def get_total_count(self):
        """Retrieve the total orders count element."""
        return self.wait_for_element_to_be_visible(self.TOTAL_COUNT)

    @allure.step("Get today's orders count")
    def get_today_count(self):
        """Retrieve the count of today's completed orders."""
        return self.wait_for_element_to_be_visible(self.TODAY_COUNT)

    @allure.step("Get first in-progress order")
    def get_in_progress(self):
        """Return the element for an order marked as 'in progress'."""
        self.wait_for_element_to_be_visible(self.ORDER_STATUS)
        return self.find_element(self.IN_PROGRESS)

    def get_set_elements_text(self, elements):
        """Convert a list of elements to a set of their text values."""
        return {elem.text for elem in elements}

    @allure.step("Get all order numbers from feed")
    def get_all_orders(self):
        """Return all order number elements."""
        self.wait_for_element_to_be_visible(self.ORDER_NUMBERS_LIST)
        return self.find_elements(self.ORDER_NUMBERS_LIST)