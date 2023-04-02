import pytest

from homework_17.utilities.config_reader import get_user_creds, get_user_name


@pytest.mark.regression
def test_identity_page_header(open_login_page):
    login_page = open_login_page
    identity_page = login_page.open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button().open_identity_card()
    assert identity_page.get_identity_page_header() == "Моя персональна інформація", 'Identity page is not displayed'


@pytest.mark.regression
def test_open_identity_page(open_login_page):
    login_page = open_login_page
    identity_page = login_page.open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button().open_identity_card()
    assert identity_page.get_page_title() == "Identity", 'Identity page title is not correct'


@pytest.mark.smoke
def test_check_user_email(open_login_page):
    login_page = open_login_page
    identity_page = login_page.open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button().open_identity_card()
    assert identity_page.check_user_email() == get_user_creds()[0], 'User email is not correct'


@pytest.mark.smoke
def test_check_user_name(open_login_page):
    login_page = open_login_page
    identity_page = login_page.open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button().open_identity_card()
    assert identity_page.check_user_name() == get_user_name()[0], 'User name is not correct'


@pytest.mark.smoke
def test_check_user_surname(open_login_page):
    login_page = open_login_page
    identity_page = login_page.open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button().open_identity_card()
    assert identity_page.check_user_surname() == get_user_name()[1], 'User surname is not correct'
