# tests/test_finddoctor.py

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
@pytest.mark.order(2)
@allure.title("Verify User Can Search Doctor Successfully")
def test_find_doctor(driver, speciality, date, location):
    logger.info("Starting Test for Find Doctor")

    finddoctor = FindDoctorPage(driver)
    logger.info("Open Find Doctor Module")

    with allure.step("Open Find Doctor Module"):
        finddoctor.click_find_doctor_menu()

    time.sleep(3)
    logger.info("Scroll To Quick Book Section")


    with allure.step("Scroll To Quick Book Section"):
        finddoctor.scroll_to_quickbook_section()

    logger.info(f"Enter Speciality: {speciality}")

    with allure.step(f"Enter Speciality: {speciality}"):
        finddoctor.enter_speciality(speciality)

    logger.info(f"Select Date: {date}")
    with allure.step(f"Select Date: {date}"):
        finddoctor.select_date(date)

    logger.info(f"Enter Location: {location}")
    with allure.step(f"Enter Location: {location}"):
        finddoctor.enter_location(location)

    logger.info("Clicking Submit Button")
    with allure.step("Click Submit Button"):
        finddoctor.click_submit()

    time.sleep(5)

    logger.info("Verify Search Result Page Opened")
    with allure.step("Verify Search Result Page Opened"):

        current_url = driver.current_url.lower()

        assert (
            "doctor" in current_url
            or "specialties" in current_url
            or "appointment" in current_url
        )
    logger.info("Find Doctor Page Test completed Successfully")