Feature: Logging in with not valid credentials
  Scenario:  User login in not successfully

    Given I am at the login page
    When I type valid email
    When I type invalid password
    Then I should not see the text welcome