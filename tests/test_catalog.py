from page_objects import ObjectsClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

page = "/laptop-notebook"


def test_items_exist_catalog_page(browser, base_url):
    browser.get(base_url + page)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(ObjectsClass.LEFT_MENU))
    wait.until(EC.visibility_of_element_located(ObjectsClass.BTN_GRID_VIEW))
    wait.until(EC.visibility_of_element_located(ObjectsClass.NAV))
    wait.until(EC.visibility_of_element_located(ObjectsClass.SEARCH))
    wait.until(EC.visibility_of_element_located(ObjectsClass.SUMMA))
