import pytest

from selenium import webdriver

DRIVERS = "/home/tsarroma/develop/drivers"

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="This is browser selection")
    parser.addoption("--base_url", default="http://192.168.4.209:8081", help="This is base url")

@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=DRIVERS + "/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=DRIVERS + "/geckodriver")
    elif browser == "opera":
        driver = webdriver.Chrome(executable_path=DRIVERS + "/operadriver")
    elif browser == "yandex":
        driver = webdriver.Chrome(executable_path=DRIVERS + "/yandexdriver")
    else:
        raise Exception("Driver not supported")

    request.addfinalizer(driver.quit)

    return driver

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")

