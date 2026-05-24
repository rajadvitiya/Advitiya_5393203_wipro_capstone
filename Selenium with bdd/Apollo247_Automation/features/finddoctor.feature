Feature: Find Doctor Validation

  Scenario Outline: Validate Find Doctor Flow

    Given User launches Apollo247 website

    When User navigates to Find Doctors section
    And User searches speciality "<speciality>"
    And User selects search date "<date>"
    And User selects location "<location>"
    And User clicks search button

    Then Validate search result for "<testtype>"

    Examples:
      | testtype | speciality | date | location  |
      | POSITIVE | Cardiology | 25   | Chennai   |
      | POSITIVE | Neurology  | 30   | Bangalore |
      | NEGATIVE | FakeSpec   | 99   | Nowhere   |