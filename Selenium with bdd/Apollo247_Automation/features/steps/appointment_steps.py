from behave import when, then
from behave.runner import Context

from pages.login_page import LoginPage
from pages.finddoctorpage import FindDoctorPage
from pages.availabledoctorpage import AvailableDoctorPage

from utils.csv_reader import CSVReader
from logger import get_logger

logger = get_logger()


# =========================================================
# READ CSV DATA
# =========================================================

login_data = CSVReader.read_csv(
    "login_data.csv"
)

schedule_data = CSVReader.read_csv(
    "schedule_data.csv"
)

phone_number = login_data[0][0]

(
    speciality,
    date,
    location,
    consultation_mode,
    schedule_date,
    schedule_time
) = schedule_data[0]


# =========================================================
# HOMEPAGE VALIDATION
# =========================================================

@when("User verifies homepage loaded")
def verify_homepage(context: Context):

    logger.info(
        "Verifying homepage loaded"
    )

    assert context.home.is_homepage_loaded()

    logger.info(
        "Homepage loaded successfully"
    )


# =========================================================
# LOGIN FLOW
# =========================================================

@when("User clicks login button")
def click_login(context: Context):

    logger.info(
        "Clicking Login Button"
    )

    context.login = LoginPage(
        context.driver
    )

    context.login.click_login_button()


@when("User enters mobile number from csv")
def enter_mobile(context: Context):

    logger.info(
        f"Entering Mobile Number: {phone_number}"
    )

    context.login.enter_phone_number(
        phone_number
    )


@when("User clicks continue button")
def click_continue(context: Context):

    logger.info(
        "Clicking Continue Button"
    )

    context.login.click_continue_button()


@when("User enters OTP manually and clicks verify")
def verify_otp(context: Context):

    logger.info(
        "Waiting For Manual OTP Entry"
    )

    context.login.enter_otp_manually_and_verify()

    logger.info(
        "OTP Verification Successful"
    )

# =========================================================
# FIND DOCTOR FLOW
# =========================================================

@when("User clicks Find Doctor menu")
def click_finddoctor(context: Context):

    logger.info(
        "Clicking Find Doctor Menu"
    )

    context.finddoctor = FindDoctorPage(
        context.driver
    )

    context.finddoctor.click_find_doctor_menu()


@when("User scrolls to QuickBook section")
def scroll_quickbook(context: Context):

    logger.info(
        "Scrolling to QuickBook Section"
    )

    context.finddoctor.scroll_to_quickbook_section()


@when("User enters speciality")
def enter_speciality(context: Context):

    logger.info(
        f"Entering Speciality: {speciality}"
    )

    result = context.finddoctor.enter_speciality(
        speciality
    )

    assert result is not None

    logger.info(
        f"Selected Speciality: {result}"
    )


@when("User selects appointment date")
def select_date(context: Context):

    logger.info(
        f"Selecting Date: {date}"
    )

    context.finddoctor.select_date(
        str(date)
    )


@when("User enters location")
def enter_location(context: Context):

    logger.info(
        f"Entering Location: {location}"
    )

    result = context.finddoctor.enter_location(
        location
    )

    assert result is not None

    logger.info(
        f"Selected Location: {result}"
    )


@when("User clicks submit button")
def click_submit(context: Context):

    logger.info(
        "Clicking Submit Button"
    )

    context.finddoctor.click_submit()


@then("Search result page should open successfully")
def validate_search(context: Context):

    current_url = (
        context.driver.current_url.lower()
    )

    logger.info(
        f"Current URL: {current_url}"
    )

    assert (
        "doctor" in current_url
        or "specialties" in current_url
        or "appointment" in current_url
    )

    logger.info(
        "Search Result Page Opened Successfully"
    )


# =========================================================
# APPOINTMENT BOOKING FLOW
# =========================================================

@when("User selects consultation mode")
def consultation_mode_step(context: Context):

    logger.info(
        f"Selecting Consultation Mode: "
        f"{consultation_mode}"
    )

    context.availabledoctor = (
        AvailableDoctorPage(
            context.driver
        )
    )

    context.availabledoctor.select_consultation_mode(
        consultation_mode
    )


@when("User selects first available doctor")
def select_doctor(context: Context):

    logger.info(
        "Selecting First Available Doctor"
    )

    context.availabledoctor.click_available_doctor()


@when("User selects available schedule date")
def schedule_date_step(context: Context):

    logger.info(
        f"Selecting Schedule Date: "
        f"{schedule_date}"
    )

    context.availabledoctor.select_schedule_date(
        str(schedule_date)
    )


@when("User selects available time slot")
def schedule_time_step(context: Context):

    logger.info(
        f"Selecting Time Slot: "
        f"{schedule_time}"
    )

    context.availabledoctor.select_schedule_time(
        schedule_time
    )


@when("User clicks continue for appointment")
def continue_appointment(context: Context):

    logger.info(
        "Clicking Continue Appointment"
    )

    context.availabledoctor.click_continue()


@then("Confirm appointment page should open")
def appointment_confirmation(context: Context):

    logger.info(
        "Validating Appointment Confirmation Page"
    )

    assert (
        context.availabledoctor
        .verify_appointment_page_opened()
    )

    logger.info(
        "FULL E2E FLOW COMPLETED SUCCESSFULLY"
    )

    logger.info(
        "========== BDD SCENARIO COMPLETED =========="
    )