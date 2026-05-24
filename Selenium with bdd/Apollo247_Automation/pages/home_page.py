from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from logger import get_logger


class HomePage(BasePage):

    logger = get_logger()

    HOME_PAGE_LOGO = (
        By.XPATH,
        "//img[contains(@src,'apollo247.svg')]"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//span[contains(text(),'Login')]"
    )

    SEARCH_BOX = (
        By.XPATH,
        "//input[contains(@placeholder,'Search Doctors')]"
    )

    POPUP_CLOSE_BUTTON = (
        By.XPATH,
        "//button//*[name()='svg']"
    )

    def close_popup_if_present(self):

        self.logger.info("Checking for popup")

        try:

            popup = self.wait_until_clickable(
                self.POPUP_CLOSE_BUTTON,
                5
            )

            self.driver.execute_script(
                "arguments[0].click();",
                popup
            )

            self.logger.info("Popup closed successfully")

        except Exception:

            self.logger.info("Popup not displayed")

            pass

        try:

            self.driver.execute_script("""
                let popup = document.querySelector('ct-web-popup-imageonly');
                if(popup){
                    popup.remove();
                }
            """)

            self.logger.info("Hidden popup removed using JavaScript")

        except Exception:

            self.logger.info("No hidden popup found")

            pass

    def click_login(self):

        self.logger.info("Clicking login button")

        self.close_popup_if_present()

        login_btn = self.wait_until_clickable(
            self.LOGIN_BUTTON,
            20
        )

        ActionChains(self.driver).move_to_element(
            login_btn
        ).perform()

        self.driver.execute_script(
            "arguments[0].click();",
            login_btn
        )

        self.logger.info("Login button clicked successfully")

    def search_doctor(self, doctor_name):

        self.logger.info(f"Searching doctor: {doctor_name}")

        self.close_popup_if_present()

        search = self.wait_until_clickable(
            self.SEARCH_BOX,
            20
        )

        search.clear()
        search.send_keys(doctor_name)

        self.logger.info("Doctor name entered in search box")

    def is_homepage_loaded(self):

        self.logger.info("Verifying homepage loaded")

        self.close_popup_if_present()

        result = self.is_displayed(
            self.HOME_PAGE_LOGO
        )

        self.logger.info(f"Homepage loaded status: {result}")

        return result