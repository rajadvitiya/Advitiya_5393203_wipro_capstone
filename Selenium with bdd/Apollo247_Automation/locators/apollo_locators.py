from selenium.webdriver.common.by import By


class ApolloLocators:

    # -----------------------------
    # HOME PAGE
    # -----------------------------

    LOGIN_POPUP_CLOSE = (
        By.XPATH,
        "//*[contains(@class,'close') or contains(@aria-label,'close')]"
    )

    FIND_DOCTORS = (
        By.XPATH,
        "//a[contains(.,'Find Doctors')]"
    )

    SPECIALITY_DROPDOWN = (
        By.XPATH,
        "//input[@placeholder='Enter Speciality']"
    )

    LOCATION_INPUT = (
        By.XPATH,
        "//input[@placeholder='Search location']"
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[span[contains(text(),'Submit')]]"
    )

    # -----------------------------
    # DOCTOR LISTING
    # -----------------------------

    FIRST_DOCTOR = (
        By.XPATH,
        "(//button[contains(.,'Clinic Visit')])[1]"
    )

    # -----------------------------
    # SLOT BOOKING
    # -----------------------------

    DATE_SELECTION = (
        By.XPATH,
        "(//div[contains(@class,'slots_date')])[1]"
    )

    FIRST_SLOT = (
        By.XPATH,
        "(//div[contains(@class,'slots_slot')])[1]"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[span[contains(text(),'Continue')]]"
    )

    # -----------------------------
    # LOGIN PAGE
    # -----------------------------

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@type='tel']"
    )

    LOGIN_CONTINUE_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Continue')]"
    )

    # -----------------------------
    # CONFIRMATION PAGE
    # -----------------------------

    CONFIRM_APPOINTMENT_PAGE = (
        By.XPATH,
        "//*[contains(text(),'Schedule Appointment') or contains(text(),'Confirm Appointment')]"
    )