from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    CURRENCY_FORM = (By.CSS_SELECTOR, "#form-currency")
    CART_CURRENCY_ICON = (By.CSS_SELECTOR, "#cart-total")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    EUR_BTN = (By.CSS_SELECTOR, "[name='EUR']")
    GBP_BTN = (By.CSS_SELECTOR, "[name='GBP']")
    USD_BTN = (By.CSS_SELECTOR, "[name='USD']")

    def __init__(self, browser, base_url):
        TIME_WAIT = 5
        self.browser = browser
        self.base_url = base_url
        self.browser.get(self.base_url)
        self.wait = WebDriverWait(self.browser, TIME_WAIT)

    def _element_visibility(self, locator):
        wait = self.wait
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator}")

    def _click(self, locator):
        element = self._element_visibility(locator)
        element.click()

    def _send_keys(self, locator, keys):
        element = self._element_visibility(locator)
        element.send_keys(keys)

    def switch_to_alert_accept(self):
        self.browser.switch_to.alert.accept()

    def find_alert_success(self):
        self._element_visibility(self.ALERT_SUCCESS)

    def change_currency(self, currency):
        locator = {}
        if currency == "EUR":
            locator = self.EUR_BTN
        elif currency == "GBP":
            locator = self.GBP_BTN
        elif currency == "USD":
            locator = self.USD_BTN
        self._click(self.CURRENCY_FORM)
        self._click(locator)

    def get_currency_text(self):
        return self._element_visibility(self.CART_CURRENCY_ICON).text
