import os
import allure
import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from logger import get_logger

logger = get_logger()


# =====================================================
# BEFORE ALL
# =====================================================

def before_all(context):

    logger.info("========== STARTING BDD TEST EXECUTION ==========")

    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("reports/allure-results", exist_ok=True)


# =====================================================
# BEFORE SCENARIO
# =====================================================

def before_scenario(context, scenario):

    logger.info("Initializing Chrome Driver")

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    context.driver.get(
        "https://www.apollo247.com"
    )

    logger.info(
        "Chrome Driver Initialized Successfully"
    )

    logger.info(
        f"Starting Scenario: {scenario.name}"
    )


# =====================================================
# AFTER SCENARIO
# =====================================================

def after_scenario(context, scenario):

    scenario_name = (
        scenario.name.replace(" ", "_")
    )

    screenshot_path = (
        f"screenshots/{scenario_name}.png"
    )

    context.driver.save_screenshot(
        screenshot_path
    )

    with open(screenshot_path, "rb") as file:

        allure.attach(
            file.read(),
            name=scenario.name,
            attachment_type=allure.attachment_type.PNG
        )

    if scenario.status == "passed":

        logger.info(
            f"Scenario Passed: {scenario.name}"
        )

    else:

        logger.error(
            f"Scenario Failed: {scenario.name}"
        )

    logger.info("Closing Browser")

    context.driver.quit()

    logger.info(
        "Browser Closed Successfully"
    )


# =====================================================
# AFTER ALL
# =====================================================

def after_all(context):

    logger.info(
        "========== BDD TEST EXECUTION COMPLETED =========="
    )

    logger.info(
        "Generating Allure Report"
    )

    os.system(
        "allure generate reports/allure-results "
        "-o reports/allure-report --clean"
    )

    logger.info(
        "Allure Report Generated Successfully"
    )

    logger.info(
        "Report Path: reports/allure-report/index.html"
    )