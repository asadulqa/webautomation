Feature: SauceDemo login functionality

  Scenario: Successful login with valid credentials
    Given the user is on the SauceDemo login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should see the products page

  Scenario: Unsuccessful login with invalid credentials
    Given the user is on the SauceDemo login page
    When the user enters invalid credentials
    And clicks the login button
    Then an error message should be shown

