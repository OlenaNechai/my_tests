import pytest

from homework_17.utilities.config_reader import get_user_creds


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login(open_login_page, env):
    login_page = open_login_page
    my_account_page = login_page.set_email(env.email).set_password(
        env.password).click_login_button()
    assert my_account_page.get_page_title() == "My account", 'My Account page is not displayed'


@pytest.mark.smoke
@pytest.mark.parametrize("email, password", [(2, 1), (0, 3)])
def test_login_fails(open_login_page, email, password):
    login_page = open_login_page
    login_failed = login_page.set_email(get_user_creds()[email]).set_password(
        get_user_creds()[password]).get_failure_message()
    assert login_failed == 'Помилка автентифікації.', 'Error is not displayed'


@pytest.mark.regression
def test_login_page_ui(open_login_page):
    header = open_login_page.get_header()
    assert header == 'Увійти до облікового запису', 'Header is not displayed'


@pytest.mark.smoke
@pytest.mark.regression
def test_redirect_to_create_account_page(open_login_page):
    login_page = open_login_page
    create_account_page = login_page.click_register_link()
    assert create_account_page.get_page_title() == "Login", 'Create Account page is not displayed'
