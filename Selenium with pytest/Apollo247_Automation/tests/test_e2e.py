import pytest
import allure
import time

from pages.homepage import HomePage
from utils.logger import LogGen
from pages.loginpage import LoginPage
from pages.finddoctorpage import FindDoctorPage
from pages.availabledoctorpage import AvailableDoctorPage
from utils.csv_reader import CSVReader





logger = LogGen.loggen()


@allure.title("Verify Homepage Loads Successfully")
@pytest.mark.order(1)
def test_homepage_loaded(driver):
    logger.info("Starting FULL E2E Test")
    logger.info("Starting Homepage Load Test")

    home = HomePage(driver)

    assert home.is_homepage_loaded()

    logger.info("Homepage Load Test Passed")





@pytest.mark.parametrize(
    "phone_number",
    CSVReader.read_csv("login_data.csv")
)
@pytest.mark.order(2)
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






@pytest.mark.parametrize(
    "speciality, date, location, consultation_mode, schedule_date, schedule_time",
    CSVReader.read_csv("schedule_data.csv")
)
@allure.title("Verify Full End-to-End Doctor Search & Appointment Flow")
def test_find_and_schedule_appointment(
        driver,
        speciality,
        date,
        location,
        consultation_mode,
        schedule_date,
        schedule_time
):



    finddoctor = FindDoctorPage(driver)

    # =========================================================
    # 1. NAVIGATE TO FIND DOCTOR
    # =========================================================
    with allure.step("Open Find Doctor Module"):
        finddoctor.click_find_doctor_menu()
        time.sleep(2)

        assert "apollo247" in driver.current_url.lower()

    logger.info("Navigation successful")

    # =========================================================
    # 2. QUICK BOOK SECTION
    # =========================================================
    with allure.step("Scroll To Quick Book Section"):
        finddoctor.scroll_to_quickbook_section()

        assert "find a doctor" in driver.page_source.lower()

    logger.info("Quick book visible")

    # =========================================================
    # 3. INPUT SPECIALITY
    # =========================================================
    with allure.step(f"Enter Speciality: {speciality}"):
        actual_speciality = finddoctor.enter_speciality(
            speciality)

    logger.info("Speciality entered")

    # =========================================================
    # 4. SELECT DATE (SEARCH FLOW)
    # =========================================================
    with allure.step(f"Select Search Date: {date}"):
        finddoctor.select_date(date)

    logger.info("Date selected")

    # =========================================================
    # 5. ENTER LOCATION
    # =========================================================
    with allure.step(f"Enter Location: {location}"):
        actual_location = finddoctor.enter_location(
            location
        )

    logger.info("Location entered")

    # =========================================================
    # 6. SUBMIT SEARCH
    # =========================================================
    with allure.step("Click Submit Button"):
        finddoctor.click_submit()

        # time.sleep(5)

        current_url = driver.current_url.lower()
        page_source = driver.page_source.lower()

        logger.info(f"Current URL: {current_url}")

        # =====================================================
        # VALIDATE SEARCH PAGE OPENED
        # =====================================================
        assert (
                "doctor" in current_url
                or "specialties" in current_url
                or "appointment" in current_url
        ), "Search result page did not open"

        logger.info("Search result page opened successfully")

        # =====================================================
        # VALIDATE SPECIALITY MATCH
        # =====================================================
        speciality_match = (
                speciality.lower() in current_url
                or speciality.lower() in page_source
        )

        # =====================================================
        # VALIDATE LOCATION MATCH
        # =====================================================
        location_match = (
                location.lower() in current_url
                or location.lower() in page_source
        )

        logger.info(
            f"Speciality Match Status: {speciality_match}"
        )

        logger.info(
            f"Location Match Status: {location_match}"
        )

        # =====================================================
        # FINAL ASSERTIONS
        # =====================================================

        assert speciality_match, (
            f"Entered speciality '{speciality}' "
            f"not reflected in search results"
        )

        assert location_match, (
            f"Entered location '{location}' "
            f"not reflected in search results"
        )

        logger.info(
            "Speciality and Location validation successful"
        )

    logger.info("Search completed")

    # =========================================================
    # 7. APPOINTMENT FLOW START
    # =========================================================
    availabledoctor = AvailableDoctorPage(driver)

    # =========================================================
    # 8. CONSULTATION MODE
    # =========================================================
    with allure.step(f"Select Consultation Mode: {consultation_mode}"):
        availabledoctor.select_consultation_mode(consultation_mode)

    # =========================================================
    # 9. SELECT DOCTOR
    # =========================================================
    with allure.step("Click Available Doctor"):
        availabledoctor.click_available_doctor()

    # =========================================================
    # 10. SELECT SLOT DATE
    # =========================================================
    with allure.step(f"Select Appointment Date: {schedule_date}"):
        availabledoctor.select_schedule_date(schedule_date)

    # =========================================================
    # 11. SELECT SLOT TIME
    # =========================================================
    with allure.step(f"Select Appointment Time: {schedule_time}"):
        availabledoctor.select_schedule_time(schedule_time)

    # =========================================================
    # 12. CONTINUE
    # =========================================================
    with allure.step("Click Continue Button"):
        availabledoctor.click_continue()

    # =========================================================
    # 13. FINAL VALIDATION
    # =========================================================
    with allure.step("Verify Appointment Page Opened"):

        assert availabledoctor.verify_appointment_page_opened()

    logger.info("FULL E2E FLOW COMPLETED SUCCESSFULLY")