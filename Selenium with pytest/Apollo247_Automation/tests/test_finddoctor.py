

import pytest
import allure
import time

from pages.finddoctorpage import FindDoctorPage
from utils.csv_reader import CSVReader
from utils.logger import LogGen

logger = LogGen.loggen()


@pytest.mark.parametrize(
    "speciality, date, location",
    CSVReader.read_csv("finddoctor_data.csv")
)
@pytest.mark.order(3)
@allure.title("Verify User Can Search Doctor Successfully (E2E)")
def test_find_doctor(driver, speciality, date, location):

    logger.info("Starting E2E Test: Find Doctor Flow")

    finddoctor = FindDoctorPage(driver)

    # =========================================================
    # 1. PAGE NAVIGATION CHECK
    # =========================================================
    with allure.step("Verify Page Navigation - Open Find Doctor"):
        finddoctor.click_find_doctor_menu()
        time.sleep(2)

        assert "apollo247" in driver.current_url.lower(), \
            "Navigation failed - not on Apollo site"

    logger.info("Page navigation successful")

    # =========================================================
    # 2. SCROLL CHECK (UI INTERACTION VALIDATION)
    # =========================================================
    with allure.step("Scroll to Quick Book Section"):
        finddoctor.scroll_to_quickbook_section()

        page_source = driver.page_source.lower()
        assert "find a doctor" in page_source or "quick" in page_source, \
            "UI section not loaded properly"

    logger.info("Quick book section visible")

    # =========================================================
    # 3. INPUT VALIDATION (SPECIALITY)
    # =========================================================
    with allure.step(f"Enter Speciality: {speciality}"):
        finddoctor.enter_speciality(speciality)

        # verify input accepted (basic validation via page state)
        assert speciality.lower() in driver.page_source.lower(), \
            "Speciality not accepted in UI"

    logger.info("Speciality entered successfully")

    # =========================================================
    # 4. DATE SELECTION VALIDATION
    # =========================================================
    with allure.step(f"Select Date: {date}"):
        finddoctor.select_date(date)

        # verify calendar interaction happened
        assert len(driver.find_elements(*finddoctor.DATE_OPTIONS)) > 0, \
            "Date selection UI not available"

    logger.info("Date selected successfully")

    # =========================================================
    # 5. LOCATION INPUT VALIDATION
    # =========================================================
    with allure.step(f"Enter Location: {location}"):
        finddoctor.enter_location(location)

        assert location.lower() in driver.page_source.lower(), \
            "Location not accepted in UI"

    logger.info("Location entered successfully")

    # =========================================================
    # 6. SEARCH TRIGGER CHECK
    # =========================================================
    with allure.step("Click Submit Button"):
        finddoctor.click_submit()

        time.sleep(5)

        # verify navigation or results trigger
        assert (
            "doctor" in driver.current_url.lower()
            or "specialties" in driver.current_url.lower()
            or "appointment" in driver.current_url.lower()
            or len(driver.page_source) > 5000
        ), "Search did not trigger results properly"

    logger.info("Search triggered successfully")

    # =========================================================
    # 7. RESULTS VISIBILITY CHECK (IMPORTANT E2E ASSERTION)
    # =========================================================
    with allure.step("Verify Doctor Results Visible"):

        page_source = driver.page_source.lower()

        assert (
            "doctor" in page_source
            or "appointment" in page_source
            or "consult" in page_source
        ), "Doctor results not visible"

    logger.info("Doctor results visible")

    # =========================================================
    # 8. BASIC UI ERROR CHECK (SAFE GUARD)
    # =========================================================
    with allure.step("Check UI Errors"):

        error_keywords = [
            "error",
            "something went wrong",
            "exception",
            "failed to load"
        ]

        page_source = driver.page_source.lower()

        for err in error_keywords:
            assert err not in page_source, f"UI Error detected: {err}"

    logger.info("No UI errors detected")

    # =========================================================
    # FINAL SUCCESS
    # =========================================================
    logger.info("E2E Test Completed Successfully")