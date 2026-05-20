import time
import pytest
import allure

from pages.loginpage import LoginPage
from utils.csv_reader import CSVReader
from utils.logger import LogGen


logger = LogGen.loggen()


@pytest.mark.parametrize(
    "phone_number",
    CSVReader.read_csv("login_data.csv")
)
@pytest.mark.order(1)
@allure.title("Verify User Can Login Successfully")
def test_login(driver, phone_number):

    logger.info("Starting Login Test")

    login = LoginPage(driver)

    with allure.step("Click Login Button"):

        logger.info("Clicking Login Button")

        login.click_login_button()

    time.sleep(2)

    with allure.step(
        f"Enter Phone Number: {phone_number}"
    ):

        logger.info(
            f"Entering Phone Number: {phone_number}"
        )

        login.enter_phone_number(phone_number)

    time.sleep(2)

    with allure.step("Click Continue Button"):

        logger.info("Clicking Continue Button")

        login.click_continue_button()

    with allure.step(
        "Enter OTP Manually And Verify Login"
    ):

        logger.info(
            "Waiting For Manual OTP Entry"
        )

        login.enter_otp_manually_and_verify()

    time.sleep(5)

    logger.info("Verifying Login Success")

    current_url = driver.current_url.lower()

    assert (
        "apollo247" in current_url
    )

    logger.info("Login Test Passed Successfully")