import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.basepage import BasePage


class LoginPage(BasePage):

    # LOGIN BUTTON
    LOGIN_BUTTON = (
        By.XPATH,
        "//span[contains(text(),'Login')]"
    )

    # PHONE NUMBER INPUT
    PHONE_NUMBER_INPUT = (
        By.XPATH,
        "//input[@name='mobileNumber']"
    )

    # CONTINUE BUTTON
    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Continue')]"
    )

    # OTP INPUT FIELD
    OTP_INPUT = (
        By.XPATH,
        "//input[@title='Please enter the otp']"
    )

    # VERIFY BUTTON
    VERIFY_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Verify')]"
    )

    def click_login_button(self):

        login_btn = self.wait_until_clickable(
            self.LOGIN_BUTTON,
            20
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_btn
        )

        print("Clicked Login Button")

    def enter_phone_number(self, phone_number):

        phone_input = self.wait.until(
            EC.visibility_of_element_located(
                self.PHONE_NUMBER_INPUT
            )
        )

        phone_input.clear()

        phone_input.send_keys(phone_number)

        print(f"Entered Phone Number: {phone_number}")

    def click_continue_button(self):

        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_btn
        )

        print("Clicked Continue Button")

    def enter_otp_manually_and_verify(self):

        # WAIT FOR OTP FIELD TO APPEAR
        self.wait.until(
            EC.visibility_of_element_located(
                self.OTP_INPUT
            )
        )

        print("OTP Sent Successfully")
        print("Waiting 30 Seconds For Manual OTP Entry...")

        # TIME TO ENTER OTP MANUALLY
        time.sleep(30)

        # CLICK VERIFY BUTTON
        verify_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.VERIFY_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            verify_btn
        )

        print("Clicked Verify Button")

    def login(self, phone_number):

        self.click_login_button()

        time.sleep(2)

        self.enter_phone_number(phone_number)

        time.sleep(2)

        self.click_continue_button()

        self.enter_otp_manually_and_verify()

        time.sleep(5)

        print("Login Completed Successfully")