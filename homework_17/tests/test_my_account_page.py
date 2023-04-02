import pytest

from homework_17.utilities.config_reader import get_user_creds

__TEXT_ERROR = 'Text is not correct'


@pytest.mark.smoke
def test_open_identity_page(open_login_page):
    login_page = open_login_page
    identity_page = login_page.open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button().open_identity_card()
    assert identity_page.get_page_title() == "Identity", 'Identity page is not displayed'


@pytest.mark.regression
def test_check_cards_texts(open_login_page):
    login_page = open_login_page
    my_account_cards = login_page.open_login_page().set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button()
    assert my_account_cards.get_identity_card_text() == "\ue853\nІНФОРМАЦІЯ", __TEXT_ERROR
    assert my_account_cards.get_address_card_text() == "\ue567\nДОДАЙТЕ СВОЮ ПЕРШУ АДРЕСУ", __TEXT_ERROR
    assert my_account_cards.get_history_card_text() == "\ue916\nІСТОРІЯ І ДЕТАЛІ МОЇХ ЗАМОВЛЕНЬ", __TEXT_ERROR
    assert my_account_cards.get_slips_card_text() == "\ue8b0\nРАХУНКИ", __TEXT_ERROR
    assert my_account_cards.get_discounts_card_text() == "\ue54e\nКУПОНИ", __TEXT_ERROR
