import allure

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

    def __init__(self, browser, base_url, wait=5):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(self.browser, wait)
        self.logger = browser.logger

    def _open_page(self, url):
        self.logger.info("Opening url: " + self.base_url + "{}".format(url))
        self.browser.get(self.base_url + url)

    def _element_visibility(self, locator):
        self.logger.info(f"Check if element is present {locator}")
        wait = self.wait
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Didn't wait for the visibility of the element: {locator}")

    def _click(self, locator):
        self.logger.info("Clicking element: {}".format(locator))
        element = self._element_visibility(locator)
        element.click()

    def _send_keys(self, locator, keys):
        self.logger.info("Input {} in input {}".format(keys, locator))
        element = self._element_visibility(locator)
        element.send_keys(keys)

    @allure.step("Switch to alert accept")
    def switch_to_alert_accept(self):
        self.logger.info("Confirmed Alert")
        self.browser.switch_to.alert.accept()

    @allure.step("Find allert success")
    def find_alert_success(self):
        self._element_visibility(self.ALERT_SUCCESS)

    @allure.step("Change currency")
    def change_currency(self, currency):
        locator = {}
        if currency == "EUR":
            locator = self.EUR_BTN
        elif currency == "GBP":
            locator = self.GBP_BTN
            self.logger.info("Confirmed currency gbp")
        elif currency == "USD":
            self.logger.info("Confirmed currency usd")
            locator = self.USD_BTN
        self._click(self.CURRENCY_FORM)
        self._click(locator)
        self.browser.refresh()

    @allure.step("Get currency text")
    def get_currency_text(self):
        self.logger.info("Get currency {}".format(self._element_visibility(self.CART_CURRENCY_ICON).text))
        return self._element_visibility(self.CART_CURRENCY_ICON).text
