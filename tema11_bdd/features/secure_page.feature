Feature: Secure page
  Scenario: Secure page logged message is displayed
    Given I am on the login page
    When Enter the correct username
    When Enter the correct password
    When I click Login button
    When I can see a confirmation message on the page
    Then I press x on message

  Scenario: Logout from secure page
    Given I am on the login page
    When Enter the correct username
    When Enter the correct password
    When I click Login button
    When I am redirected to the "secure" page
    When I press logout button
    Then I am redirected to the "login" page
