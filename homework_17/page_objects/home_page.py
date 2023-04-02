from selenium.webdriver.common.by import By
from homework_17.utilities.web_ui.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __footer = (By.CSS_SELECTOR, "#footer")
    __carousel = (By.CSS_SELECTOR, "#carousel")
    __logo = (By.XPATH, '//*[@id="_desktop_logo"]/descendant::img')
    __enter_login_page = (By.XPATH, '//*[@id="_desktop_user_info"]/descendant::span')

    def scroll_to_element(self):
        return self._scroll_to_element(self.__footer)

    def get_page_title(self):
        return self._get_title()

    def check_carousel_presence(self):
        return self._wait_until_element_located(self.__carousel)

    def check_logo_redirect(self):
        self._click(locator=self.__logo)
        return HomePage(self.driver)

    def open_login_page(self):
        self._click(locator=self.__enter_login_page)
        return self

    def get_login_button_text(self):
        return self._get_text(self.__enter_login_page)
