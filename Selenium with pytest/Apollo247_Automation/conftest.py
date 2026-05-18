import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.logger import LogGen


logger = LogGen.loggen()


@pytest.fixture(scope="function")
def driver():

    logger.info("Launching Chrome Browser")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    logger.info("Chrome Browser Launched Successfully")

    driver.get("https://www.apollo247.com/")

    logger.info("Navigated to Apollo247 Website")

    yield driver

    logger.info("Closing Browser")

    driver.quit()

    logger.info("Browser Closed Successfully")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        logger.error(f"Test Failed: {item.name}")

        driver = item.funcargs["driver"]

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        logger.error("Failure Screenshot Captured and Attached to Allure Report")

    elif report.when == "call" and report.passed:

        logger.info(f"Test Passed: {item.name}")