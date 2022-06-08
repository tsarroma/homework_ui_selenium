from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

PAGE = "/index.php?route=common/home"


class MainPage(BasePage):
    NAV = (By.CSS_SELECTOR, "#top")
    SEARCH = (By.CSS_SELECTOR, ".form-control")
    SUMMA = (By.CSS_SELECTOR, "#cart-total")
    NAVBAR = (By.CSS_SELECTOR, ".collapse")
    CAROUSEL = (By.CSS_SELECTOR, "#carousel0")

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.browser.get(self.base_url + PAGE)
