import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers.urls import URLS


class ConstructorPage(BasePage):
    """
    Page object for managing burger constructor actions and navigating to the orders feed.
    """

    # Locators with Russian text preserved for stability
    CONSTRUCTOR_LINK: tuple = (
        By.XPATH,
        "//p[contains(text(),'Конструктор')]"
    )
    ORDERS_FEED_HEADER: tuple = (
        By.XPATH,
        '//*[contains(text(),"Лента Заказов")]'
    )
    AVAILABLE_INGREDIENTS: tuple = (
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient')]"
    )
    INGREDIENT_INFO: tuple = (
        By.XPATH,
        '//h2[contains(text(),"Детали ингредиента")]'
    )
    CLOSE_INGREDIENT_INFO: tuple = (
        By.XPATH,
        '//button[contains(@class, "Modal_modal__close")]'
    )
    COUNTER_INGREDIENT: tuple = (
        By.XPATH,
        (
            "//a[contains(@class, 'BurgerIngredient_ingredient')]"
            "//*[contains(@class,'counter__num')]"
        )
    )
    ORDER_BLOCK: tuple = (
        By.XPATH,
        "//ul[contains(@class, 'BurgerConstructor_basket__list__')]"
    )
    SUBMIT_ORDER_BUTTON: tuple = (
        By.XPATH,
        '//button[contains(text(), "Оформить заказ")]'
    )
    ORDER_CONFIRMATION: tuple = (
        By.XPATH,
        '//p[contains(text(), "Ваш заказ начали готовить")]'
    )
    CLOSE_ORDER_CONFIRMATION: tuple = (
        By.XPATH,
        '//button[contains(@class, "Modal_modal__close")]'
    )
    ORDER_NUMBER: tuple = (
        By.XPATH,
        '//h2[contains(@class,"Modal_modal__title_shadow__")]'
    )
    ICON_WAITING: tuple = (
        By.XPATH,
        ".//div[contains(@class, 'Modal_modal_opened')]"
    )

    @allure.step("Open main application page")
    def open_base_page(self) -> None:
        """Navigate to the base URL of the application."""
        self.get_page(URLS.BASE_URL)

    @allure.step("Open login page")
    def open_login_page(self) -> None:
        """Navigate to the login page URL."""
        self.get_page(URLS.LOGIN_PAGE)

    @allure.step("Click on 'Конструктор'")
    def click_on_constructor(self) -> None:
        """Click the constructor link via JavaScript and confirm page load."""
        self.click_on_with_execute_script(self.CONSTRUCTOR_LINK)
        self.wait_for_page(URLS.BASE_URL)

    @allure.step("Click on orders feed header")
    def click_on_orders_feed(self) -> None:
        """Click the orders feed header and wait for the feed page."""
        self.click_on_with_execute_script(self.ORDERS_FEED_HEADER)
        self.wait_for_page(URLS.ORDERS_FEED_PAGE)

    @allure.step("Click on Ingridient")
    def click_on_ingredient_info(self, index: int = 0) -> None:
        """Scroll to and click an ingredient to view its details."""
        ingredient = self.find_elements(self.AVAILABLE_INGREDIENTS)[index]
        self.scroll_to_element(ingredient)
        ingredient.click()
        return self.wait_for_element_to_be_visible(self.INGREDIENT_INFO)

    @allure.step("Close ingredient info modal")
    def click_on_close_ingredient_info(self) -> None:
        """Close the ingredient details modal and wait for it to disappear."""
        self.click_on(self.CLOSE_INGREDIENT_INFO)
        self.wait_for_element_to_be_invisible(self.INGREDIENT_INFO)

    @allure.step("Add ingredient to order")
    def add_ingredient_to_order(self, index: int = 8) -> None:
        """Drag a specific ingredient into the order constructor."""
        ingredient = self.find_elements(self.AVAILABLE_INGREDIENTS)[index]
        self.scroll_to_element(ingredient)
        order_block = self.find_element(self.ORDER_BLOCK)
        self.drag_ingredient_to_order(ingredient, order_block)

    @allure.step("Add bun to order")
    def add_bun_to_order(self, index: int = 0) -> None:
        """Drag a bun element into the order constructor."""
        bun = self.find_elements(self.AVAILABLE_INGREDIENTS)[index]
        self.scroll_to_element(bun)
        order_block = self.find_element(self.ORDER_BLOCK)
        self.drag_ingredient_to_order(bun, order_block)

    @allure.step("Get ingredient counter value")
    def get_counter_value(self, index: int) -> int:
        """Return the counter number for a given ingredient."""
        counters = self.find_elements(self.COUNTER_INGREDIENT)
        return int(counters[index].text)

    @allure.step("Submit the current order")
    def submit_order(self) -> None:
        """Click the submit button and wait for confirmation modal."""
        self.click_on_with_execute_script(self.SUBMIT_ORDER_BUTTON)
        return self.wait_for_element_to_be_visible(self.ORDER_CONFIRMATION)

    @allure.step("Close order confirmation modal")
    def close_order_confirmation(self) -> None:
        """Close the order confirmation dialog and wait for its disappearance."""
        self.click_on(self.CLOSE_ORDER_CONFIRMATION)
        self.wait_for_element_to_be_invisible(self.ORDER_CONFIRMATION)

    @allure.step("Complete a full order flow")
    def complete_order(self) -> str:
        """
        Perform the full order workflow: open page, add bun and ingredient,
        submit, wait for processing, extract the order number, and close.

        :return: The text of the order number element.
        """
        self.open_base_page()
        self.wait_for_element_to_be_clickable(self.AVAILABLE_INGREDIENTS)
        self.add_bun_to_order()
        self.add_ingredient_to_order()
        self.submit_order()
        # Increase timeout to wait for processing indicator to disappear
        self.set_timeout(40)
        self.wait_for_close_element(self.ICON_WAITING)
        order_id = self.find_element(self.ORDER_NUMBER).text
        self.close_order_confirmation()
        return order_id