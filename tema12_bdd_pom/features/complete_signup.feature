Feature: Complete signup
  Scenario: Introduce all the element
    Given I am on the Jules App
    When  I click "Sign up." link
    When  I click personal value
    When I click continue button
    And I input correct first name
    And I click continue button
    And I input correct last name
    And I click continue button
    And I input wrong email
    Then I verify error message
    When I clear email input
    And I input correct email
    Then I verify that error is not displayed anymore

