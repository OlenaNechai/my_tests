import pytest
import json

from homework_17.constants import ROOT_DIR
from homework_17.page_objects.home_page import HomePage
from homework_17.utilities.configuration import Configuration
from homework_17.utilities.driver_factory import driver_factory


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{ROOT_DIR}/configurations/config.json', 'r') as file:
        res = file.read()
    config = json.loads(res)
    return Configuration(**config)


@pytest.fixture()
def create_browser(env):
    driver = driver_factory(int(env.browser_id))
    driver.maximize_window()
    driver.get(env.app_url)
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_browser):
    return HomePage(create_browser).open_login_page()


@pytest.fixture()
def open_create_account_page(create_browser):
    return HomePage(create_browser).open_login_page().click_register_link()


@pytest.fixture()
def open_my_account_page(create_browser, env):
    return HomePage(create_browser).open_login_page().set_email(env.email).set_password(
        env.password).click_login_button()


@pytest.fixture()
def open_identity_page(create_browser, env):
    return HomePage(create_browser).open_login_page().set_email(env.email).set_password(
        env.password).click_login_button().open_identity_card()


@pytest.fixture()
def open_home_page(create_browser):
    return HomePage(create_browser)
