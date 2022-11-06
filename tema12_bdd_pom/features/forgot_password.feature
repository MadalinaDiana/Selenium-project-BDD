Feature: Send email
  Scenario: Send email forgot password
    Given I am on the Jules App-sign-in
    When  I click "Forgot password?" link
    And  I input email.
    And I click "SEND EMAIL" button.
    Then I recive the the mail send message.


