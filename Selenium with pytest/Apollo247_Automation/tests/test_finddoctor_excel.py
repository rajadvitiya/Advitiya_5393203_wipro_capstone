import pytest
import time

from utils.excel_reader import ExcelReader
from pages.finddoctorpage import FindDoctorPage
from utils.logger import LogGen


# LOGGER INIT
logger = LogGen.loggen()

# READ EXCEL DATA
test_data = ExcelReader.read_excel(
    "testdata/finddoctor_testdata.xlsx"
)


@pytest.mark.parametrize(
    "testtype, speciality, date, location, expected",
    test_data
)
def test_find_doctor_excel(
        driver,
        testtype,
        speciality,
        date,
        location,
        expected
):

    logger.info("========== STARTING TEST CASE ==========")
    logger.info(f"TestType: {testtype}")
    logger.info(f"Speciality: {speciality}")
    logger.info(f"Date: {date}")
    logger.info(f"Location: {location}")

    finddoctor = FindDoctorPage(driver)

    # OPEN MODULE
    logger.info("Clicking Find Doctor Menu")
    finddoctor.click_find_doctor_menu()
    time.sleep(2)

    # SCROLL
    logger.info("Scrolling to QuickBook Section")
    finddoctor.scroll_to_quickbook_section()

    # ENTER DATA
    logger.info(f"Entering Speciality: {speciality}")
    actual_speciality = finddoctor.enter_speciality(
        speciality
    )

    logger.info(f"Selecting Date: {date}")
    finddoctor.select_date(str(date))

    logger.info(f"Entering Location: {location}")
    actual_location = finddoctor.enter_location(
        location
    )

    # SUBMIT
    logger.info("Clicking Submit Button")
    finddoctor.click_submit()

    time.sleep(5)

    current_url = driver.current_url.lower()
    logger.info(f"Current URL: {current_url}")

    # ---------------- POSITIVE TEST CASES ----------------
    if testtype.upper() == "POSITIVE":

        logger.info("Executing POSITIVE validation")

        assert (
            "doctor" in current_url
            or "specialties" in current_url
            or "appointment" in current_url
        ), "Positive test failed - results page not opened"

        logger.info("POSITIVE TEST PASSED")

    # ---------------- NEGATIVE TEST CASES ----------------
    elif testtype.upper() == "NEGATIVE":

        logger.info("Executing NEGATIVE validation")

        speciality_mismatch = (
                actual_speciality is None
                or actual_speciality != speciality.lower()
        )

        location_mismatch = (
                actual_location is None
                or location.lower() not in actual_location
        )

        assert (
                speciality_mismatch
                or location_mismatch
        ), (
            "Negative test failed - "
            "invalid inputs were accepted"
        )

    else:
        logger.error(f"Invalid test type found: {testtype}")
        raise Exception(f"Unknown test type: {testtype}")

    logger.info("========== TEST CASE COMPLETED ==========")