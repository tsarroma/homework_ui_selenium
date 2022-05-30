from page_objects import ObjectsClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

PAGE = "/admin"


def test_login(browser, base_url):
    browser.get(base_url + PAGE)
    try:
        wait = WebDriverWait(browser, 3)
        wait.until(EC.visibility_of_element_located(ObjectsClass.PANEL_BODY))
        wait.until(EC.visibility_of_element_located(ObjectsClass.INPUT_USERNAME))
        wait.until(EC.visibility_of_element_located(ObjectsClass.INPUT_PASSWORD))
        wait.until(EC.visibility_of_element_located(ObjectsClass.BTN_PRIMARY))
        wait.until(EC.visibility_of_element_located(ObjectsClass.FOOTER))
    except TimeoutException:
        raise AssertionError("Не дождался видимости элемента")
