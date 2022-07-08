import allure

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

    @allure.step("Open admin page")
    def open_admin_page(self):
        self._open_page(ADMIN_PAGE_URL)

    @allure.step("Login admin")
    def login_admin(self, username, password):
        self._send_keys(self.INPUT_USERNAME, username)
        self._send_keys(self.INPUT_PASSWORD, password)
        self._click(self.BTN_PRIMARY)

    @allure.step("Click to left menu")
    def click_to_product_left_menu(self):
        self._click(self.MENU_CATALOG)
        self._click(self.MENU_PRODUCT)

    @allure.step("Click add new product button")
    def click_add_new_product_btn(self):
        self._click(self.ADD_NEW)

    @allure.step("Input general info of new product")
    def input_general_info_new_product(self, product, tag):
        self._send_keys(self.PRODUCT_NAME, product)
        self._send_keys(self.TAG_TITLE, tag)

    @allure.step("Click data tab")
    def click_data_tab(self):
        self._click(self.DATA)

    @allure.step("Input data new product")
    def input_data_new_product(self, model):
        self._send_keys(self.MODEL, model)

    @allure.step("Click save button")
    def click_save_btn(self):
        self._click(self.SAVE)

    @allure.step("Input filter product")
    def filter_test_product(self, product, model):
        self._send_keys(self.SEARCH_INPUT_PRODUCT_NAME, product)
        self._send_keys(self.MODEL, model)
        self._click(self.FILTER_BTN)

    @allure.step("Click confirm checkbox")
    def click_checkbox(self):
        self._click(self.CHECKBOX)

    @allure.step("Click delete button")
    def click_delete_btn(self):
        self._click(self.DELETE_BTN)
