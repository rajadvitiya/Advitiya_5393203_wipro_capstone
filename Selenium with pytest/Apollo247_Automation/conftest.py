import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.screenshot_util import ScreenshotUtil
from utils.logger import LogGen


logger = LogGen.loggen()


@pytest.fixture(scope="module")
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


# SINGLE HOOK ONLY
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # EXECUTE ONLY AFTER TEST EXECUTION
    if report.when == "call":

        driver = item.funcargs.get("driver")

        if driver:

            test_name = item.name

            # PASS SCREENSHOT
            if report.passed:

                logger.info(f"Test Passed: {test_name}")

                screenshot_path = ScreenshotUtil.capture(
                    driver,
                    test_name,
                    "PASS"
                )

                allure.attach.file(
                    screenshot_path,
                    name=f"{test_name}_PASS",
                    attachment_type=allure.attachment_type.PNG
                )

                logger.info(
                    "Pass Screenshot Captured and Attached"
                )

            # FAIL SCREENSHOT
            elif report.failed:

                logger.error(f"Test Failed: {test_name}")

                screenshot_path = ScreenshotUtil.capture(
                    driver,
                    test_name,
                    "FAIL"
                )

                allure.attach.file(
                    screenshot_path,
                    name=f"{test_name}_FAIL",
                    attachment_type=allure.attachment_type.PNG
                )

                logger.error(
                    "Failure Screenshot Captured and Attached"
                )