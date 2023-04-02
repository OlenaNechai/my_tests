from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _wait_until_to_be_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator):
        self._wait_until_to_be_clickable(locator).click()

    def _get_text(self, locator):
        element = self._wait_until_element_located(locator)
        return element.text

    def _get_title(self):
        return self.driver.title

    def _vertical_scroll(self, y: int):
        self.driver.execute_script(f'window.scrollBy(0,{y}')

    def _scroll_to_element(self, locator):
        max_retries = 100
        tries = 0
        while tries != max_retries:
            try:
                element = self._wait_until_element_located(locator)
                return element
            except Exception:
                self._vertical_scroll(100)
                tries += 1

    def _wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _get_visible_text(self, locator):
        element = self._wait_until_element_visible(locator)
        return element.get_attribute('value')
