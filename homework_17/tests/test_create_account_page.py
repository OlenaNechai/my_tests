import pytest


@pytest.mark.smoke
def test_open_create_account_page(open_create_account_page):
    create_account_page = open_create_account_page
    assert create_account_page.get_page_title() == "Login", 'Create Account page is not displayed'


@pytest.mark.smoke
def test_open_identity_page(open_create_account_page):
    create_account_page = open_create_account_page
    assert create_account_page.check_header() == "Реєстрація", 'Create page header is not correct'


@pytest.mark.regression
def test_check_password_button_name(open_create_account_page):
    create_account_page = open_create_account_page
    assert create_account_page.get_password_button_name() == "ПОКАЗАТИ", 'Show Password button name is incorrect'


@pytest.mark.regression
def test_check_password_button_name_hidden(open_create_account_page):
    create_account_page = open_create_account_page
    assert create_account_page.get_hidden_password_button_name() == "ПРИХОВАТИ", 'Hidden button name is incorrect'


@pytest.mark.regression
def test_check_submit_button_name(open_create_account_page):
    create_account_page = open_create_account_page
    assert create_account_page.get_submit_button_text() == "ЗБЕРЕГТИ", 'Show Password button name is incorrect'
