from selenium.webdriver.common.by import By
from homework_17.page_objects.identity_page import IdentityPage
from homework_17.utilities.web_ui.base_page import BasePage


class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __identity = (By.CSS_SELECTOR, "#identity-link")
    __address = (By.CSS_SELECTOR, "#address-link")
    __history = (By.CSS_SELECTOR, '#history-link')
    __slips = (By.CSS_SELECTOR, '#order-slips-link')
    __discounts = (By.CSS_SELECTOR, '#discounts-link')

    def open_identity_card(self):
        self._click(locator=self.__identity)
        return IdentityPage(self.driver)

    def get_page_title(self):
        return self._get_title()

    def get_identity_card_text(self):
        return self._get_text(self.__identity)

    def get_address_card_text(self):
        return self._get_text(self.__address)

    def get_history_card_text(self):
        return self._get_text(self.__history)

    def get_slips_card_text(self):
        return self._get_text(self.__slips)

    def get_discounts_card_text(self):
        return self._get_text(self.__discounts)
