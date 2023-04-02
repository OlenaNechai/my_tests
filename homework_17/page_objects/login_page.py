from selenium.webdriver.common.by import By

from homework_17.page_objects.create_account_page import CreateAccountPage
from homework_17.page_objects.my_account_page import MyAccountPage
from homework_17.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __enter_login_page = (By.XPATH, '//*[@id="_desktop_user_info"]/descendant::span')
    __email_input = (By.XPATH, '//input[@name="email"]')
    __password_input = (By.XPATH, '//input[@name="password"]')
    __login_button = (By.XPATH, '//button[@data-link-action="sign-in"]')
    __auth_error = (By.XPATH, '//*[text()="Помилка автентифікації."]')
    __header = (By.XPATH, '//h1')
    __register = (By.XPATH, '//*[@data-link-action="display-register-form"]')

    def open_login_page(self):
        self._click(locator=self.__enter_login_page)
        return self

    def set_email(self, email: str):
        self._send_keys(locator=self.__email_input, value=email)
        return self

    def set_password(self, password: str):
        self._send_keys(locator=self.__password_input, value=password)
        return self

    def click_login_button(self):
        self._click(self.__login_button)
        return MyAccountPage(self.driver)

    def get_failure_message(self):
        self._click(self.__login_button)
        element = self._get_text(self.__auth_error)
        return element

    def check_header(self):
        self._click(self.__login_button)
        element = self._get_text(self.__header)
        return element

    def login(self, email, password):
        self.open_login_page().set_email(email).set_password(password).click_login_button()
        return MyAccountPage(self.driver)

    def click_register_link(self):
        self._click(self.__register)
        return CreateAccountPage(self.driver)
