from behave import when, then
from behave.runner import Context

from pages.finddoctorpage import FindDoctorPage
from logger import get_logger

logger = get_logger()


@when("User navigates to Find Doctors section")
def navigate_finddoctor(context: Context):

    logger.info(
        "Navigating To Find Doctor Section"
    )

    context.finddoctor = FindDoctorPage(
        context.driver
    )

    context.finddoctor.click_find_doctor_menu()

    context.finddoctor.scroll_to_quickbook_section()

    logger.info(
        "Navigation Successful"
    )


@when('User searches speciality "{speciality}"')
def search_speciality(
        context: Context,
        speciality
):

    logger.info(
        f"Searching Speciality: {speciality}"
    )

    context.speciality = speciality

    context.actual_speciality = (
        context.finddoctor.enter_speciality(
            speciality
        )
    )

    logger.info(
        f"Actual Speciality: "
        f"{context.actual_speciality}"
    )


@when('User selects search date "{date}"')
def select_date(
        context: Context,
        date
):

    logger.info(
        f"Selecting Search Date: {date}"
    )

    context.date = date

    context.finddoctor.select_date(date)


@when('User selects location "{location}"')
def select_location(
        context: Context,
        location
):

    logger.info(
        f"Selecting Location: {location}"
    )

    context.location = location

    context.actual_location = (
        context.finddoctor.enter_location(
            location
        )
    )

    logger.info(
        f"Actual Location: "
        f"{context.actual_location}"
    )


@when("User clicks search button")
def click_submit(context: Context):

    logger.info(
        "Clicking Search Button"
    )

    context.finddoctor.click_submit()

    context.current_url = (
        context.driver.current_url.lower()
    )

    logger.info(
        f"Current URL: "
        f"{context.current_url}"
    )


@then('Validate search result for "{testtype}"')
def validate_result(
        context: Context,
        testtype
):

    logger.info(
        f"Executing {testtype} Validation"
    )

    if testtype.upper() == "POSITIVE":

        assert (
            context.actual_speciality
            == context.speciality.lower()
        )

        assert (
            context.actual_location is not None
        )

        assert (
            "doctor" in context.current_url
            or "specialties" in context.current_url
            or "appointment" in context.current_url
        )

        logger.info(
            "POSITIVE TEST PASSED"
        )

    elif testtype.upper() == "NEGATIVE":

        speciality_invalid = (
            context.actual_speciality is None
        )

        location_invalid = (
            context.actual_location is None
        )

        assert (
            speciality_invalid
            or location_invalid
        )

        logger.info(
            "NEGATIVE TEST PASSED"
        )

    else:

        raise Exception(
            f"Invalid Test Type: {testtype}"
        )

    logger.info(
        "========== BDD SCENARIO COMPLETED =========="
    )