import pytest

__TEXT_ERROR = 'Text is not correct'


@pytest.mark.smoke
def test_open_identity_page(open_my_account_page):
    identity_page = open_my_account_page.open_identity_card()
    assert identity_page.get_page_title() == "Identity", 'Identity page is not displayed'


@pytest.mark.regression
def test_check_cards_texts(open_my_account_page):
    my_account_cards = open_my_account_page
    assert my_account_cards.get_identity_card_text() == "\ue853\nІНФОРМАЦІЯ", __TEXT_ERROR
    assert my_account_cards.get_address_card_text() == "\ue567\nДОДАЙТЕ СВОЮ ПЕРШУ АДРЕСУ", __TEXT_ERROR
    assert my_account_cards.get_history_card_text() == "\ue916\nІСТОРІЯ І ДЕТАЛІ МОЇХ ЗАМОВЛЕНЬ", __TEXT_ERROR
    assert my_account_cards.get_slips_card_text() == "\ue8b0\nРАХУНКИ", __TEXT_ERROR
    assert my_account_cards.get_discounts_card_text() == "\ue54e\nКУПОНИ", __TEXT_ERROR
