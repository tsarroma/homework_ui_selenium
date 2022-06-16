from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage

MAIN_PAGE_URL = "/index.php?route=common/home"


class MainPage(BasePage):
    NAV = (By.CSS_SELECTOR, "#top")
    SEARCH = (By.CSS_SELECTOR, ".form-control")
    SUMMA = (By.CSS_SELECTOR, "#cart-total")
    NAVBAR = (By.CSS_SELECTOR, ".collapse")
    CAROUSEL = (By.CSS_SELECTOR, "#carousel0")

    def __init__(self, browser, base_url):
        TIME_WAIT = 6
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(self.browser, TIME_WAIT)

    def open_main_page(self):
        self.open_page(MAIN_PAGE_URL)
