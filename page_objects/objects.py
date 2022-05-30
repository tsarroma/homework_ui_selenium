from selenium.webdriver.common.by import By


class ObjectsClass:
    NAV = (By.CSS_SELECTOR, "#top")
    SEARCH = (By.CSS_SELECTOR, ".form-control")
    SUMMA = (By.CSS_SELECTOR, "#cart-total")
    NAVBAR = (By.CSS_SELECTOR, ".collapse")
    CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
    LEFT_MENU = (By.CSS_SELECTOR, "#column-left")
    BTN_GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
    TEXT_VALUE = (By.CSS_SELECTOR, "[name='option[208]']")
    SELECT = (By.CSS_SELECTOR, "[for='input-option217']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='email']")
    LINK_LOGIN_PAGE = (By.CSS_SELECTOR, "#content > p > a")
    RADIO_SUBSCRIBE = (By.CSS_SELECTOR, "[class='radio-inline']")
    PANEL_BODY = (By.CSS_SELECTOR, ".panel-body")
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BTN_PRIMARY = (By.CSS_SELECTOR, ".btn-primary")
    FOOTER = (By.CSS_SELECTOR, "#footer")
