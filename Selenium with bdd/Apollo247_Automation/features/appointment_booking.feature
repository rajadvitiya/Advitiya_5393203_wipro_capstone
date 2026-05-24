Feature: Appointment Booking E2E Flow

  Scenario: Successful Appointment Booking

    Given User launches Apollo247 website

    When User verifies homepage loaded
    And User clicks login button
    And User enters mobile number from csv
    And User clicks continue button
    And User enters OTP manually and clicks verify

    And User clicks Find Doctor menu
    And User scrolls to QuickBook section

    And User enters speciality
    And User selects appointment date
    And User enters location

    And User clicks submit button

    Then Search result page should open successfully

    When User selects consultation mode
    And User selects first available doctor
    And User selects available schedule date
    And User selects available time slot
    And User clicks continue for appointment

    Then Confirm appointment page should open