from behave import given
from behave.runner import Context

from pages.home_page import HomePage
from logger import get_logger

logger = get_logger()


@given("User launches Apollo247 website")
def launch_website(context: Context):

    logger.info(
        "========== STARTING BDD SCENARIO =========="
    )

    logger.info(
        "BDD Scenario Started"
    )

    context.home = HomePage(
        context.driver
    )

    logger.info(
        "Apollo247 website launched successfully"
    )