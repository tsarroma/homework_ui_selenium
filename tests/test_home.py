from page_objects import ObjectsClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

page = "/index.php?route=common/home"


def test_items_exist_home_page(browser, base_url):
    browser.get(base_url + page)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(ObjectsClass.NAV))
    wait.until(EC.visibility_of_element_located(ObjectsClass.SEARCH))
    wait.until(EC.visibility_of_element_located(ObjectsClass.SUMMA))
    wait.until(EC.visibility_of_element_located(ObjectsClass.NAVBAR))
    wait.until(EC.visibility_of_element_located(ObjectsClass.CAROUSEL))
