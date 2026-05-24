import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AvailableDoctorPage(BasePage):

    # CONSULT MODE
    ONLINE_CONSULT_OPTION = (
        By.XPATH,
        "//label[contains(text(),'Consult Online')]"
    )

    HOSPITAL_VISIT_OPTION = (
        By.XPATH,
        "//label[contains(text(),'Hospital Visit')]"
    )

    # DOCTOR CARD
    AVAILABLE_DOCTOR = (
        By.XPATH,
        "(//div[contains(@class,'mj_')]//button)[1]"
    )

    # DATE
    DATE_OPTIONS = (
        By.XPATH,
        "//div[contains(@class,'slots_date__Dy0W_')]"
    )

    # SLOT TIME
    SLOT_OPTIONS = (
        By.XPATH,
        "//div[contains(@class,'slots_slot__YYaL_')]"
    )

    # CONTINUE BUTTON
    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'slots_proceedBtn')]"
    )

    # CONFIRM APPOINTMENT BUTTON
    CONFIRM_APPOINTMENT_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Confirm Appointment')]"
    )

    def select_consultation_mode(self, mode):

        mode = mode.lower().strip()

        if mode == "online consult":

            online = self.wait_until_clickable(
                self.ONLINE_CONSULT_OPTION,
                20
            )

            self.driver.execute_script(
                "arguments[0].click();",
                online
            )

            print("Selected Consultation Mode: Online Consult")

        elif mode == "hospital visit":

            hospital = self.wait_until_clickable(
                self.HOSPITAL_VISIT_OPTION,
                20
            )

            self.driver.execute_script(
                "arguments[0].click();",
                hospital
            )



        else:
            raise Exception(
                f"Invalid Consultation Mode: {mode}"
            )

        time.sleep(2)

    def click_available_doctor(self):

        doctor = self.wait_until_clickable(
            self.AVAILABLE_DOCTOR,
            20
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            doctor
        )

        # time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            doctor
        )



        # time.sleep(5)

    def select_schedule_date(self, required_date):

        # time.sleep(2)

        def get_dates():
            return self.driver.find_elements(*self.DATE_OPTIONS)

        selected = False

        dates = get_dates()

        for d in dates:
            text = d.text.strip()


            if required_date in text:
                self.driver.execute_script("arguments[0].click();", d)

                selected = True
                break

        # IF REQUIRED DATE NOT FOUND → SELECT FIRST AVAILABLE
        if not selected:
            if dates:
                self.driver.execute_script("arguments[0].click();", dates[0])



    def select_schedule_time(self, required_time):

        time.sleep(2)

        def get_slots():
            return self.driver.find_elements(*self.SLOT_OPTIONS)

        selected = False

        # TRY CLICK "GO TO NEXT AVAILABLE DATE" IF NO SLOTS
        try:
            no_slots = self.driver.find_elements(
                By.XPATH,
                "//div[contains(@class,'slots_noSlots')]"
            )

            if no_slots:
                next_btn = self.driver.find_elements(
                    By.XPATH,
                    "//button[contains(.,'Go to next available date')]"
                )

                if next_btn:
                    self.driver.execute_script("arguments[0].click();", next_btn[0])
                    print("Clicked: Go to next available date")
                    time.sleep(3)

        except Exception:
            pass

        slots = get_slots()

        # WAIT UNTIL SLOTS APPEAR
        if not slots:
            time.sleep(3)
            slots = get_slots()

        # ---------------- EXACT MATCH ----------------
        for s in slots:
            txt = s.text.strip()


            if required_time.lower() == txt.lower():
                self.driver.execute_script("arguments[0].click();", s)

                return

        # ---------------- SAME HOUR MATCH ----------------
        try:
            target_hour = required_time.split(":")[0]
            target_period = required_time.split(" ")[1]

            for s in slots:
                txt = s.text.strip()
                try:
                    hour = txt.split(":")[0]
                    period = txt.split(" ")[1]

                    if hour == target_hour and period == target_period:
                        self.driver.execute_script("arguments[0].click();", s)
                        print(f"Closest slot selected: {txt}")
                        return
                except:
                    continue
        except:
            pass

        # ---------------- FALLBACK: FIRST SLOT ----------------
        slots = get_slots()

        if slots:
            self.driver.execute_script("arguments[0].click();", slots[0])


    def click_continue(self):

        continue_btn = self.wait_until_clickable(
            self.CONTINUE_BUTTON,
            20
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_btn
        )



        time.sleep(5)

    def verify_appointment_page_opened(self):

        possible_elements = [

            # CONFIRM BUTTON
            (
                By.XPATH,
                "//span[contains(text(),'Confirm Appointment')]"
            ),

            # PAY & CONFIRM BUTTON
            (
                By.XPATH,
                "//span[contains(text(),'Pay & Confirm')]"
            ),

            # CONTINUE BUTTON
            (
                By.XPATH,
                "//span[contains(text(),'Continue')]"
            ),

            # APPOINTMENT DETAILS HEADER
            (
                By.XPATH,
                "//h2[contains(text(),'Appointment Details')]"
            ),

            # PATIENT DETAILS
            (
                By.XPATH,
                "//*[contains(text(),'Patient Details')]"
            ),

            # TOTAL CHARGES
            (
                By.XPATH,
                "//*[contains(text(),'Total Charges')]"
            )

        ]

        for locator in possible_elements:

            elements = self.driver.find_elements(*locator)

            if len(elements) > 0 and elements[0].is_displayed():


                return True

        raise Exception(
            "Final Appointment Page "
            "Did Not Open"
        )