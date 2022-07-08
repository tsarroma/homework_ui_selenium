import allure

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

CATALOG_PAGE_URL = "/laptop-notebook"


class CatalogPage(BasePage):
    LEFT_MENU = (By.CSS_SELECTOR, "#column-left")
    BTN_GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
    NAV = (By.CSS_SELECTOR, "#top")
    SEARCH = (By.CSS_SELECTOR, ".form-control")
    SUMMA = (By.CSS_SELECTOR, "#cart-total")

    @allure.step("Open catalog page")
    def open_catalog_page(self):
        self._open_page(CATALOG_PAGE_URL)
