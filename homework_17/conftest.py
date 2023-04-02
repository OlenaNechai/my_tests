import pytest

from homework_17.page_objects.home_page import HomePage
from homework_17.page_objects.login_page import LoginPage
from homework_17.utilities.config_reader import get_application_url, get_browser_id

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
    return LoginPage(create_browser)


@pytest.fixture()
def open_home_page(create_browser):
    return HomePage(create_browser)
