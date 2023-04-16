from selenium.webdriver.common.by import By

from homework_17.page_objects.login_page import LoginPage
from homework_17.utilities.web_ui.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __info_header = (By.XPATH, "//h3[text()='Інфо']")
    __carousel = (By.CSS_SELECTOR, "#carousel")
    __enter_login_page = (By.XPATH, '//*[@id="_desktop_user_info"]/descendant::span')

    def scroll_to_info_header(self):
        return self._scroll_to_element(self.__info_header)

    def get_page_title(self):
        return self._get_title()

    def get_carousel(self):
        return self._wait_until_element_located(self.__carousel)

    def open_login_page(self):
        self._click(locator=self.__enter_login_page)
        return LoginPage(self.driver)

    def get_login_button_text(self):
        return self._get_text(self.__enter_login_page)
