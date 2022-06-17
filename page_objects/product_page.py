from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

PRODUCT_PAGE_URL = "/laptop-notebook"


class ProductPage(BasePage):
    LEFT_MENU = (By.CSS_SELECTOR, "#column-left")
    BTN_GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
    NAV = (By.CSS_SELECTOR, "#top")
    SEARCH = (By.CSS_SELECTOR, ".form-control")
    SUMMA = (By.CSS_SELECTOR, "#cart-total")

    def open_product_page(self):
        self._open_page(PRODUCT_PAGE_URL)
