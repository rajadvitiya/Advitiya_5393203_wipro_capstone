import pytest
import allure

from pages.homepage import HomePage
from utils.logger import LogGen


logger = LogGen.loggen()


@allure.title("Verify Homepage Loads Successfully")
@pytest.mark.order(1)
def test_homepage_loaded(driver):

    logger.info("Starting Homepage Load Test")

    home = HomePage(driver)

    assert home.is_homepage_loaded()

    logger.info("Homepage Load Test Passed")