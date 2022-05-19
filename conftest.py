import pytest

from selenium import webdriver

DRIVERS = "/home/tsarroma/develop/drivers"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="This is browser selection")
    parser.addoption("--base_url", default="http://192.168.4.209:8081", help="This is url")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path=DRIVERS + "/chromedriver", options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(executable_path=DRIVERS + "/geckodriver", options=options)
    elif browser == "opera":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', True)
        driver = webdriver.Opera(executable_path=DRIVERS + "/operadriver", options=options)
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path=DRIVERS + "/yandexdriver", options=options)
    else:
        raise Exception("Browser not supported, use: chrome, firefox, opera, yandex")

    request.addfinalizer(driver.quit)

    return driver


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
