from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage

PRODUCT_PAGE_URL = "/laptop-notebook"


class ProductPage(BasePage):
    LEFT_MENU = (By.CSS_SELECTOR, "#column-left")
    BTN_GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
    NAV = (By.CSS_SELECTOR, "#top")
    SEARCH = (By.CSS_SELECTOR, ".form-control")
    SUMMA = (By.CSS_SELECTOR, "#cart-total")

    def __init__(self, browser, base_url):
        TIME_WAIT = 6
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(self.browser, TIME_WAIT)

    def open_product_page(self):
        self.open_page(PRODUCT_PAGE_URL)
