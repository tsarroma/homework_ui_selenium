import os
import allure
import pytest
import logging
import datetime

from selenium import webdriver
from selenium.webdriver.opera.options import Options

DRIVERS = "/home/tsarroma/develop/drivers"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="yandex", help="This is browser selection")
    parser.addoption("--base_url", action="store", default="http://192.168.4.209:8081", help="This is url")
    parser.addoption("--log_level", action="store", default="DEBUG", help="This is log level")
    parser.addoption("--executor", action="store", default="192.168.4.209")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--videos", action="store_true")
    parser.addoption("--bv")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.originalname}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test started at {}".format(datetime.datetime.now()))

    if executor == "local":

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

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "name": "Tsarroma",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
        }

        options = Options()
        if browser == "opera":
            options.add_experimental_option('w3c', True)

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities,
            options=options
        )

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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    browser = item.funcargs['browser']
                else:
                    print('Fail to take screenshot')
                    return
            allure.attach(
                browser.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f'Fail to take screenshot: {e}')
