Feature: Home Page

  Scenario: Redirect to Checkbox Page
    Given I am on the Home Page
    When I click on the Checkboxes
    When I am redirected to the "checkboxes" page
    Then I click checkbox2

  Scenario: Redirect to Drop-down
    Given I am on the Home Page
    When I click on the Dropdown
    When I am redirected to the "dropdown" page
    Then I click option2

  Scenario: Redirect to Form Authentication
    Given I am on the Home Page
    When I click on the Form Authentication
    When I am redirected to the "login" page
    Then I click Login button


