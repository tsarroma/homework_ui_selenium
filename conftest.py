import pytest
import logging
import datetime

from selenium import webdriver

DRIVERS = "/home/tsarroma/develop/drivers"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="This is browser selection")
    parser.addoption("--base_url", action="store", default="http://192.168.4.209:8081", help="This is url")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")

    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.originalname}.log")
    file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

#    logger = logging.getLogger(request.node.name)
#    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
#    file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
#    logger.addHandler(file_handler)
#    logger.setLevel(level=log_level)

    logger.info("===> Test started at {}".format(datetime.datetime.now()))

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

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser: {}".format(browser))

    def fin():
        driver.quit()
        logger.info("===> Test finished at {}".format(datetime.datetime.now()))

    request.addfinalizer(fin)

    return driver


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
