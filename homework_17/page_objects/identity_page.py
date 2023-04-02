from selenium.webdriver.common.by import By
from homework_17.utilities.web_ui.base_page import BasePage


class IdentityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __identity_header = (By.XPATH, '//*[@id="main"]/header/h1')
    __email_input = (By.XPATH, '//input[@type="email"]')
    __name_input = (By.XPATH, '//input[@name="firstname"]')
    __surname_input = (By.XPATH, '//input[@name="lastname"]')

    def get_page_title(self):
        return self._get_title()

    def get_identity_page_header(self):
        return self._get_text(self.__identity_header)

    def check_user_email(self):
        return self._get_visible_text(self.__email_input)

    def check_user_name(self):
        return self._get_visible_text(self.__name_input)

    def check_user_surname(self):
        return self._get_visible_text(self.__surname_input)
