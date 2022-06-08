import pytest

from page_objects.base_page import BasePage


@pytest.mark.parametrize("currency, currency_icon", [("EUR", "€"), ("GBP", "£"), ("USD", "$")])
def test_change_currency(browser, base_url, currency, currency_icon):
    base_page = BasePage(browser, base_url)
    base_page.change_currency(currency)
    currency_text = base_page.get_currency_text()
    assert currency_text == currency_icon + "  "

