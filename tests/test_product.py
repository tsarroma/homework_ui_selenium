from page_objects import ObjectsClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

PAGE = "/test"


def test_items_exist_product_page(browser, base_url):
    browser.get(base_url + PAGE)
    try:
        wait = WebDriverWait(browser, 3)
        wait.until(EC.visibility_of_element_located(ObjectsClass.TEXT_VALUE))
        wait.until(EC.visibility_of_element_located(ObjectsClass.SELECT))
        wait.until(EC.visibility_of_element_located(ObjectsClass.NAV))
        wait.until(EC.visibility_of_element_located(ObjectsClass.SEARCH))
        wait.until(EC.visibility_of_element_located(ObjectsClass.SUMMA))
    except TimeoutException:
        raise AssertionError("Не дождался видимости элемента")
