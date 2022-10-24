Feature: Login Page

  Scenario: Redirect to Secure Area
    Given I am on the login page
    When Enter the correct username
    When Enter the correct password
    When I click Login button
    Then I can see a confirmation message on the page
