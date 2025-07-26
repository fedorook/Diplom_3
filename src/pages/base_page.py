from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Base page class providing common Selenium actions and explicit waits.
    """

    def __init__(self, driver, timeout=10):
        """
        Initialize with a WebDriver instance and default timeout.

        :param driver: Selenium WebDriver
        :param timeout: wait timeout in seconds
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    def set_timeout(self, timeout):
        """Update the default wait timeout and WebDriverWait instance."""
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_for_page(self, url):
        """Wait until the current URL matches the expected URL."""
        return self.wait.until(EC.url_to_be(url))

    def get_page(self, url):
        """Navigate to the specified URL and wait for it to load by URL check."""
        self.driver.get(url)
        return self.wait_for_page(url)

    def get_current_url(self):
        """Return the current browser URL."""
        return self.driver.current_url

    def find_element(self, locator):
        """Find a single element using a locator tuple."""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Find multiple elements using a locator tuple."""
        return self.driver.find_elements(*locator)

    def click_on(self, locator):
        """Click on an element located by the locator."""
        elem = self.find_element(locator)
        elem.click()

    def click_on_with_execute_script(self, locator):
        """Click an element via JavaScript execution."""
        elem = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", elem)

    def send_keys(self, locator, text):
        """Clear and type text into an element located by the locator."""
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def scroll_to(self, locator):
        """Scroll to an element located by the locator and wait until visible."""
        elem = self.find_element(locator)
        return self.scroll_to_element(elem)

    def scroll_to_element(self, elem):
        """Scroll until the specified element is visible."""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        return self.wait.until(EC.visibility_of(elem))

    def wait_for_element(self, locator):
        """Wait for an element to be present in the DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        """Wait for an element to become clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator):
        """Wait for an element to be visible on the page."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_invisible(self, locator):
        """Wait for an element to disappear or become invisible."""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_close_element(self, locator):
        """Wait until an element is no longer visible."""
        self.wait.until_not(EC.visibility_of_element_located(locator))

    def drag_ingredient_to_order(self, source, target):
        """Simulate drag-and-drop using JavaScript events."""
        script = (
            "const [src, dst] = arguments;"
            "['dragstart','dragover','drop'].forEach(type => {"
            "  const evt = new DragEvent(type, { bubbles: true });"
            "  (type=='dragstart'?src:dst).dispatchEvent(evt);"
            "});"
        )
        self.driver.execute_script(script, source, target)