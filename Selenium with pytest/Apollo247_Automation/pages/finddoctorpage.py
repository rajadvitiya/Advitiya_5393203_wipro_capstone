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

        time.sleep(3)

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

        # OPEN DROPDOWN
        dropdown = self.wait_until_clickable(
            self.SPECIALITY_DROPDOWN
        )

        dropdown.click()

        time.sleep(2)

        # SEARCH INPUT
        search_input = self.wait_until_clickable(
            self.SPECIALITY_SEARCH_INPUT
        )

        search_input.click()

        search_input.send_keys(Keys.CONTROL + "a")
        search_input.send_keys(Keys.BACKSPACE)

        search_input.send_keys(speciality)

        time.sleep(3)

        # GET OPTIONS
        options = self.wait.until(
            EC.presence_of_all_elements_located(
                self.SPECIALITY_OPTIONS
            )
        )

        selected = False

        for option in options:

            # GET ONLY FIRST SPAN
            option_text = option.find_element(
                By.XPATH,
                ".//span[1]"
            ).text.strip().lower()

            print("Available Option:", option_text)

            # EXACT MATCH
            if option_text == speciality.lower():

                self.driver.execute_script(
                    "arguments[0].click();",
                    option
                )

                print(f"Selected Speciality: {option_text}")

                selected = True
                break

        if not selected:

            raise Exception(
                f"Speciality '{speciality}' not found"
            )

        time.sleep(2)

    # =========================================================
    # SELECT DATE
    # =========================================================

    # =========================================================
    # SELECT DATE
    # =========================================================

    def select_date(self, required_date):

        """
        CSV DATE FORMAT:
        25
        26
        30
        """

        # OPEN CALENDAR
        calendar = self.wait_until_clickable(
            self.CALENDAR_ICON
        )

        self.driver.execute_script(
            "arguments[0].click();",
            calendar
        )

        time.sleep(2)

        # DYNAMIC DATE XPATH
        # SELECT ONLY ENABLED DATE BUTTONS
        date_xpath = (
            f"//button[not(@disabled)]"
            f"//abbr[text()='{required_date}']"
        )

        # WAIT FOR DATE
        date_element = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    date_xpath
                )
            )
        )

        # CLICK DATE
        self.driver.execute_script(
            "arguments[0].click();",
            date_element
        )

        print(f"Selected Date: {required_date}")

        time.sleep(2)
    # =========================================================
    # ENTER LOCATION
    # =========================================================

    # =========================================================
    # ENTER LOCATION
    # =========================================================

    def enter_location(self, location):

        # LOCATION INPUT FIELD
        location_input = self.wait_until_clickable(
            self.LOCATION_INPUT
        )

        # CLICK INPUT
        self.driver.execute_script(
            "arguments[0].click();",
            location_input
        )

        time.sleep(1)

        # CLEAR EXISTING LOCATION PROPERLY
        location_input.send_keys(Keys.CONTROL + "a")
        location_input.send_keys(Keys.DELETE)

        time.sleep(1)

        # TYPE LOCATION SLOWLY
        for char in location:
            location_input.send_keys(char)
            time.sleep(0.2)

        print(f"Entered Location: {location}")

        # WAIT FOR DROPDOWN OPTIONS
        location_option_xpath = (
            f"//li[.//*[contains(translate(text(), "
            f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
            f"'abcdefghijklmnopqrstuvwxyz'), "
            f"'{location.lower()}')]]"
        )

        location_option = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    location_option_xpath
                )
            )
        )

        # SCROLL OPTION INTO VIEW
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            location_option
        )

        time.sleep(1)

        # CLICK LOCATION OPTION
        self.driver.execute_script(
            "arguments[0].click();",
            location_option
        )

        print(f"Selected Location: {location}")

        time.sleep(2)

        # VERIFY LOCATION IS SELECTED
        selected_value = location_input.get_attribute("value")

        print(f"Final Location Value: {selected_value}")


    # =========================================================
    # CLICK SUBMIT
    # =========================================================

    def click_submit(self):

        submit_btn = self.wait_until_clickable(
            self.SUBMIT_BUTTON
        )

        self.driver.execute_script(
            "arguments[0].click();",
            submit_btn
        )

        time.sleep(5)

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