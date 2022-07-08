import allure

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

MAIN_PAGE_URL = "/index.php?route=common/home"


class MainPage(BasePage):
    NAV = (By.CSS_SELECTOR, "#top")
    SEARCH = (By.CSS_SELECTOR, ".form-control")
    SUMMA = (By.CSS_SELECTOR, "#cart-total")
    NAVBAR = (By.CSS_SELECTOR, ".collapse")
    CAROUSEL = (By.CSS_SELECTOR, "#carousel0")

    @allure.step("Open main page")
    def open_main_page(self):
        self._open_page(MAIN_PAGE_URL)
