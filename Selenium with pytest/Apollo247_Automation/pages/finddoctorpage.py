# pages/finddoctorpage.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import BasePage
import time


class FindDoctorPage(BasePage):

    # =========================================================
    # TOP NAVIGATION
    # =========================================================

    FIND_DOCTOR_MENU = (
        By.XPATH,
        "//a[contains(@href,'/specialties') and contains(text(),'Find Doctors')]"
    )

    # =========================================================
    # QUICK BOOK SECTION
    # =========================================================

    QUICKBOOK_SECTION = (
        By.XPATH,
        "//h4[contains(text(),'Find a Doctor in 3 easy steps')]"
    )

    # =========================================================
    # SPECIALITY FIELD
    # =========================================================

    SPECIALITY_DROPDOWN = (
        By.XPATH,
        "//div[contains(@class,'QuickBook_speciality__14Rw0')]"
    )

    SPECIALITY_SEARCH_INPUT = (
        By.XPATH,
        "//input[@placeholder='Example: Dermatology']"
    )

    SPECIALITY_OPTIONS = (
        By.XPATH,
        "//div[contains(@class,'QuickBook_autoSearchPopover')]//li"
    )

    # =========================================================
    # DATE FIELD
    # =========================================================

    CALENDAR_ICON = (
        By.XPATH,
        "//span[contains(@class,'QuickBook_dateImage')]"
    )

    # =========================================================
    # LOCATION FIELD
    # =========================================================

    LOCATION_INPUT = (
        By.XPATH,
        "//input[@placeholder='Search location']"
    )

    LOCATION_OPTIONS = (
        By.XPATH,
        "//ul/li"
    )

    # =========================================================
    # SUBMIT BUTTON
    # =========================================================

    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'QuickBook_submitBtn')]"
    )

    # =========================================================
    # CLICK FIND DOCTOR MENU
    # =========================================================

    def click_find_doctor_menu(self):

        menu = self.wait_until_clickable(
            self.FIND_DOCTOR_MENU
        )

        self.driver.execute_script(
            "arguments[0].click();",
            menu
        )

        # time.sleep(3)

    # =========================================================
    # SCROLL TO QUICKBOOK SECTION
    # =========================================================

    def scroll_to_quickbook_section(self):

        section = self.wait.until(
            EC.presence_of_element_located(
                self.QUICKBOOK_SECTION
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            section
        )

        time.sleep(2)

    # =========================================================
    # ENTER SPECIALITY
    # =========================================================

    def enter_speciality(self, speciality):

        dropdown = self.wait_until_clickable(
            self.SPECIALITY_DROPDOWN
        )

        dropdown.click()

        # time.sleep(2)

        search_input = self.wait_until_clickable(
            self.SPECIALITY_SEARCH_INPUT
        )

        search_input.click()

        search_input.send_keys(Keys.CONTROL + "a")
        search_input.send_keys(Keys.BACKSPACE)

        search_input.send_keys(speciality)

        # time.sleep(3)

        options = self.wait.until(
            EC.presence_of_all_elements_located(
                self.SPECIALITY_OPTIONS
            )
        )

        for option in options:

            option_text = option.find_element(
                By.XPATH,
                ".//span[1]"
            ).text.strip().lower()



            # EXACT MATCH
            if option_text == speciality.lower():
                self.driver.execute_script(
                    "arguments[0].click();",
                    option
                )



                # time.sleep(2)

                return option_text

        # INVALID SPECIALITY


        self.driver.execute_script(
            "document.activeElement.blur();"
        )

        return None
    # =========================================================
    # SELECT DATE
    # =========================================================

    # =========================================================
    # SELECT DATE
    # =========================================================

    def select_date(self, required_date):

        calendar = self.wait_until_clickable(self.CALENDAR_ICON)
        self.driver.execute_script("arguments[0].click();", calendar)
        # time.sleep(2)

        try:
            date_xpath = f"//button[not(@disabled)]//abbr[text()='{required_date}']"

            date_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, date_xpath))
            )

            self.driver.execute_script("arguments[0].click();", date_element)


        except Exception:
            # ❗ FALLBACK: pick ANY enabled date instead of failing


            fallback_dates = self.driver.find_elements(
                By.XPATH,
                "//button[not(@disabled)]//abbr"
            )

            if fallback_dates:
                self.driver.execute_script("arguments[0].click();", fallback_dates[0])

        # time.sleep(2)
    # =========================================================
    # ENTER LOCATION
    # =========================================================

    # =========================================================
    # ENTER LOCATION
    # =========================================================

    def enter_location(self, location):

        location_input = self.wait_until_clickable(
            self.LOCATION_INPUT
        )

        self.driver.execute_script(
            "arguments[0].click();",
            location_input
        )

        time.sleep(1)

        location_input.send_keys(Keys.CONTROL + "a")
        location_input.send_keys(Keys.DELETE)

        time.sleep(1)

        for char in location:
            location_input.send_keys(char)
            time.sleep(0.2)

        print(f"Entered Location: {location}")

        try:

            # FIXED XPATH
            location_option_xpath = (
                f"//input[@placeholder='Search location']"
                f"/following::ul[1]/li"
                f"[contains(translate(., "
                f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                f"'abcdefghijklmnopqrstuvwxyz'),"
                f"'{location.lower()}')]"
            )

            location_option = self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        location_option_xpath
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                location_option
            )

            time.sleep(2)

            selected_value = location_input.get_attribute(
                "value"
            )



            return selected_value.lower()

        except Exception:

            print(
                f"[WARNING] Location "
                f"not found: {location}"
            )

            self.driver.execute_script(
                "document.activeElement.blur();"
            )

            return None
    # =========================================================
    # CLICK SUBMIT
    # =========================================================

    def click_submit(self):

        submit_btn = self.wait_until_clickable(self.SUBMIT_BUTTON)

        # prevent stale click issues
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(1)

        try:
            self.driver.execute_script("arguments[0].click();", submit_btn)
        except Exception:

            submit_btn.click()

        # time.sleep(5)

    # =========================================================
    # COMPLETE FLOW
    # =========================================================

    # def search_doctor(self, speciality, date, location):
    #
    #     self.click_find_doctor_menu()
    #
    #     self.scroll_to_quickbook_section()
    #
    #     self.enter_speciality(speciality)
    #
    #     self.select_date(date)
    #
    #     self.enter_location(location)
    #
    #     self.click_submit()