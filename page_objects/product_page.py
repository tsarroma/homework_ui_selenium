from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

PAGE = "/laptop-notebook"


class ProductPage(BasePage):
    LEFT_MENU = (By.CSS_SELECTOR, "#column-left")
    BTN_GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
    NAV = (By.CSS_SELECTOR, "#top")
    SEARCH = (By.CSS_SELECTOR, ".form-control")
    SUMMA = (By.CSS_SELECTOR, "#cart-total")

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.browser.get(self.base_url + PAGE)
