import pytest

from homework_17.page_objects.home_page import HomePage
from homework_17.utilities.config_reader import get_application_url, get_browser_id
from homework_17.utilities.config_reader import get_user_creds
from homework_17.utilities.driver_factory import driver_factory


@pytest.fixture()
def create_browser():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_application_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_browser):
    return HomePage(create_browser).open_login_page()


@pytest.fixture()
def open_create_account_page(create_browser):
    return HomePage(create_browser).open_login_page().click_register_link()


@pytest.fixture()
def open_my_account_page(create_browser):
    return HomePage(create_browser).open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button()


@pytest.fixture()
def open_identity_page(create_browser):
    return HomePage(create_browser).open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button().open_identity_card()


@pytest.fixture()
def open_home_page(create_browser):
    return HomePage(create_browser)
