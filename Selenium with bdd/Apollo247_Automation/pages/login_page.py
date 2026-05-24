import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


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
        "//button[normalize-space()='Verify']"
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

    time.sleep(30)

    def enter_otp_manually_and_verify(self):
        # WAIT FOR OTP INPUT FIELD
        otp_input = self.wait.until(
            EC.visibility_of_element_located(
                self.OTP_INPUT
            )
        )

        print(
            "\nEnter OTP manually in browser..."
        )

        # WAIT UNTIL VERIFY BUTTON BECOMES ENABLED
        self.wait.until(
            lambda driver: (
                driver.find_element(
                    *self.VERIFY_BUTTON
                ).is_enabled()
            )
        )

        verify_btn = self.driver.find_element(
            *self.VERIFY_BUTTON
        )

        # SCROLL INTO VIEW
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            verify_btn
        )

        # CLICK VERIFY
        self.driver.execute_script(
            "arguments[0].click();",
            verify_btn
        )

        print("Clicked Verify Button")
