from selenium.webdriver.common.by import By
from homework_17.utilities.web_ui.base_page import BasePage


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __enter_login_page = (By.XPATH, '//*[@id="_desktop_user_info"]/descendant::span')
    __registration_header = (By.XPATH, '//*[@id="main"]/header/h1')
    __registration_link = (By.XPATH, '//*[@data-link-action="display-register-form"]')
    __show_password_button = (By.XPATH, '//button[@data-action="show-password"]')
    __submit_button = (By.XPATH, '//button[@data-link-action="save-customer"]')

    def open_login_page(self):
        self._click(locator=self.__enter_login_page)
        return self

    def get_page_title(self):
        return self._get_title()

    def click_register_link(self):
        self._click(self.__registration_link)
        return CreateAccountPage(self.driver)

    def check_header(self):
        element = self._get_text(self.__registration_header)
        return element

    def get_password_button_name(self):
        return self._get_text(self.__show_password_button)

    def get_hidden_password_button_name(self):
        self._click(locator=self.__show_password_button)
        return self._get_text(self.__show_password_button)

    def get_submit_button_text(self):
        return self._get_text(self.__submit_button)
