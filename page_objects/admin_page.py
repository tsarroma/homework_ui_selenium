from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

ADMIN_PAGE_URL = "/admin"


class AdminPage(BasePage):
    PANEL_BODY = (By.CSS_SELECTOR, ".panel-body")
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BTN_PRIMARY = (By.CSS_SELECTOR, ".btn-primary")
    FOOTER = (By.CSS_SELECTOR, "#footer")
    ADD_NEW = (By.CSS_SELECTOR, "[data-original-title='Add New']")
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog > a:nth-child(1)")
    MENU_PRODUCT = (By.XPATH, "/html/body/div/nav/ul/li[2]/ul/li[2]/a")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    SAVE = (By.CSS_SELECTOR, "[data-original-title='Save']")
    DATA = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/form/ul/li[2]/a")
    MODEL = (By.CSS_SELECTOR, "#input-model")
    SEARCH_INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name")
    FILTER_BTN = (By.CSS_SELECTOR, "#button-filter")
    CHECKBOX = (By.CSS_SELECTOR, "[type='checkbox']")
    DELETE_BTN = (By.CSS_SELECTOR, ".fa-trash-o")

    def open_admin_page(self):
        self._open_page(ADMIN_PAGE_URL)

    def login_admin(self, username, password):
        self._send_keys(self.INPUT_USERNAME, username)
        self._send_keys(self.INPUT_PASSWORD, password)
        self._click(self.BTN_PRIMARY)

    def click_to_product_left_menu(self):
        self._click(self.MENU_CATALOG)
        self._click(self.MENU_PRODUCT)

    def click_add_new_product_btn(self):
        self._click(self.ADD_NEW)

    def input_general_info_new_product(self, product, tag):
        self._send_keys(self.PRODUCT_NAME, product)
        self._send_keys(self.TAG_TITLE, tag)

    def click_data_tab(self):
        self._click(self.DATA)

    def input_data_new_product(self, model):
        self._send_keys(self.MODEL, model)

    def click_save_btn(self):
        self._click(self.SAVE)

    def filter_test_product(self, product, model):
        self._send_keys(self.SEARCH_INPUT_PRODUCT_NAME, product)
        self._send_keys(self.MODEL, model)
        self._click(self.FILTER_BTN)

    def click_checkbox(self):
        self._click(self.CHECKBOX)

    def click_delete_btn(self):
        self._click(self.DELETE_BTN)
