import allure

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

REGISTER_PAGE_URL = "/index.php?route=account/register"


class RegisterPage(BasePage):
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='email']")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#input-confirm")
    LINK_LOGIN_PAGE = (By.CSS_SELECTOR, "#content > p > a")
    RADIO_SUBSCRIBE = (By.CSS_SELECTOR, "[class='radio-inline']")
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".btn-primary")

    @allure.step("Open register page")
    def open_register_page(self):
        self._open_page(REGISTER_PAGE_URL)

    @allure.step("Input firtsname")
    def firstname_input(self, firstname):
        self._send_keys(self.FIRSTNAME_INPUT, firstname)

    @allure.step("Input lastname")
    def lastname_input(self, lastname):
        self._send_keys(self.LASTNAME_INPUT, lastname)

    @allure.step("Input email")
    def email_input(self, email):
        self._send_keys(self.EMAIL_INPUT, email)

    @allure.step("Input telephone")
    def telephone_input(self, telephone):
        self._send_keys(self.TELEPHONE_INPUT, telephone)

    @allure.step("Input password")
    def password_input(self, password):
        self._send_keys(self.PASSWORD_INPUT, password)
        self._send_keys(self.PASSWORD_CONFIRM_INPUT, password)

    @allure.step("Click agree checkbox")
    def click_agree_checkbox(self):
        self._click(self.AGREE_CHECKBOX)

    @allure.step("Click continue button")
    def click_continue_btn(self):
        self._click(self.CONTINUE_BTN)
