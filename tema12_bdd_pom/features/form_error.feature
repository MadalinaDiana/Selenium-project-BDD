Feature: Form Page
  Scenario: Verify error
    Given I am on the Jules App
    When  I input correct email
    When I leave pass empty
    Then Message error is displayed
    And Log in button id disabled