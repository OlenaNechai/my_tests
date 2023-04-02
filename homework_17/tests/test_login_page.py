import pytest

from homework_17.utilities.config_reader import get_user_creds, get_wrong_user_creds


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login(open_login_page):
    login_page = open_login_page
    my_account_page = login_page.open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button()
    assert my_account_page.get_page_title() == "My account", 'My Account page is not displayed'


@pytest.mark.smoke
def test_login_fails_wrong_email(open_login_page):
    login_page = open_login_page
    login_failed = login_page.open_login_page().set_email(get_wrong_user_creds()[0]).set_password(
        get_user_creds()[1]).get_failure_message()
    assert login_failed == 'Помилка автентифікації.', 'Error is not displayed'


@pytest.mark.smoke
def test_login_fails_wrong_password(open_login_page):
    login_page = open_login_page
    login_failed = login_page.open_login_page().set_email(get_user_creds()[0]).set_password(
        get_wrong_user_creds()[1]).get_failure_message()
    assert login_failed == 'Помилка автентифікації.', 'Error is not displayed'


@pytest.mark.regression
def test_login_page_ui(open_login_page):
    header = open_login_page.open_login_page().check_header()
    assert header == 'Увійти до облікового запису', 'Header is not displayed'


@pytest.mark.smoke
@pytest.mark.regression
def test_redirect_to_create_account_page(open_login_page):
    login_page = open_login_page
    create_account_page = login_page.open_login_page().click_register_link()
    assert create_account_page.get_page_title() == "Login", 'Create Account page is not displayed'
