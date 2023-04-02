import pytest


@pytest.mark.smoke
def test_scroll_to_element(open_home_page):
    home_page = open_home_page
    element = home_page.scroll_to_element()
    assert element, "Page is not scrollable"


@pytest.mark.regression
def test_get_page_title(open_home_page):
    home_page = open_home_page
    assert home_page.get_page_title() == "Туконі Магазин", 'Home page title is not correct'


@pytest.mark.regression
def test_carousel_is_present(open_home_page):
    home_page = open_home_page
    assert home_page.check_carousel_presence(), 'Carousel is not present'


@pytest.mark.smoke
@pytest.mark.regression
def test_logo_redirects_correctly(open_home_page):
    home_page = open_home_page
    redirect = home_page.check_logo_redirect()
    assert redirect.get_page_title() == "Туконі Магазин", 'Home page logo redirect doesn\'t work'


@pytest.mark.smoke
@pytest.mark.regression
def test_open_login_page(open_home_page):
    login_page = open_home_page.open_login_page()
    assert login_page.get_page_title() == "Login", 'Login page is not displayed'


@pytest.mark.regression
def test_check_login_button_text(open_home_page):
    home_page = open_home_page
    assert home_page.get_login_button_text() == "Увійти", 'Text is not correct'
