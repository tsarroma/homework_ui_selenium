from page_objects import ObjectsClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

PAGE = "/index.php?route=account/register"


def test_login(browser, base_url):
    browser.get(base_url + PAGE)
    try:
        wait = WebDriverWait(browser, 3)
        wait.until(EC.visibility_of_element_located(ObjectsClass.FIRSTNAME_INPUT))
        wait.until(EC.visibility_of_element_located(ObjectsClass.LASTNAME_INPUT))
        wait.until(EC.visibility_of_element_located(ObjectsClass.EMAIL_INPUT))
        wait.until(EC.visibility_of_element_located(ObjectsClass.LINK_LOGIN_PAGE))
        wait.until(EC.visibility_of_element_located(ObjectsClass.RADIO_SUBSCRIBE))
    except TimeoutException:
        raise AssertionError("Не дождался видимости элемента")
