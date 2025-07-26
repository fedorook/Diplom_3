import allure
from conftest import driver, login_user
from src import OrderFeedPage, ConstructorPage


@allure.feature('Order Feed')
class TestOrderFeed:

    @allure.story('Display order details on click')
    def test_click_on_order(self, driver):
        """
        Verify that clicking an order displays its details.
        """
        feed_page = OrderFeedPage(driver)
        feed_page.get_feed_page()

        order_info = feed_page.click_on_order(2)
        assert order_info.is_displayed() is True

    @allure.story('Increase total order counter')
    def test_increase_total_order_counter(self, driver, login_user):
        """
        Ensure the total order counter increments after placing an order.
        """
        feed_page = OrderFeedPage(driver)
        feed_page.get_feed_page()
        initial_count = int(feed_page.get_total_count().text)

        ConstructorPage(driver).complete_order()

        feed_page.get_feed_page()
        updated_count = int(feed_page.get_total_count().text)

        with allure.step('Test data'):
            allure.attach(str(initial_count), name='initial_count')
            allure.attach(str(updated_count), name='updated_count')

        assert initial_count < updated_count

    @allure.story('Increase today order counter')
    def test_increase_today_order_counter(self, driver, login_user):
        """
        Ensure today's order counter increments after placing an order.
        """
        feed_page = OrderFeedPage(driver)
        feed_page.get_feed_page()
        today_initial = int(feed_page.get_today_count().text)

        ConstructorPage(driver).complete_order()

        feed_page.get_feed_page()
        today_updated = int(feed_page.get_today_count().text)

        with allure.step('Test data'):
            allure.attach(str(today_initial), name='today_initial')
            allure.attach(str(today_updated), name='today_updated')

        assert today_initial < today_updated

    @allure.story('New order appears as In Progress')
    def test_new_order_in_progress(self, driver, login_user):
        """
        Verify a newly placed order shows up in the "In Progress" list.
        """
        order_number = '0' + ConstructorPage(driver).complete_order()

        feed_page = OrderFeedPage(driver)
        feed_page.get_feed_page()
        in_progress_text = feed_page.get_in_progress().text

        with allure.step('Test data'):
            allure.attach(order_number, name='order_number')
            allure.attach(in_progress_text, name='in_progress')

        assert order_number == in_progress_text

    @allure.story('User order appears in feed')
    def test_user_order_visible_in_feed(self, driver, login_user):
        """
        Confirm the current user's order is present in the feed page.
        """
        ConstructorPage(driver).complete_order()

        personal_page = login_user
        personal_page.click_on_personal_account()
        personal_page.click_on_order_history()
        user_order = personal_page.get_order_number()

        feed_page = OrderFeedPage(driver)
        feed_page.get_feed_page()
        feed_orders = feed_page.get_set_elements_text(feed_page.get_all_orders())

        with allure.step('Test data'):
            allure.attach(user_order, name='user_order')
            allure.attach(str(feed_orders), name='feed_orders')

        assert user_order in feed_orders
