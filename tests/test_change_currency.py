import pytest
import allure

from page_objects.base_page import BasePage

@allure.feature('Base page')
@allure.story('Validation')
@allure.title('Change currency')
@pytest.mark.parametrize("currency, currency_icon", [("EUR", "€"), ("GBP", "£"), ("USD", "$")])
def test_change_currency(browser, base_url, currency, currency_icon):
    icon = {}
    base_page = BasePage(browser, base_url)
    base_page._open_page("/")
    base_page.change_currency(currency)
    currency_text = base_page.get_currency_text()
    if icon == "EUR":
        assert currency_text == "0 item(s) - 0.00" + currency_icon
    elif icon == "GBP":
        assert currency_text == "0 item(s) -" + currency_icon + "0.00"
    elif icon == "USD":
        assert currency_text == "0 item(s) - 0.00" + currency_icon
