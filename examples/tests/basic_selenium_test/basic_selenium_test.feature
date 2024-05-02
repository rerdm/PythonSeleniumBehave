Feature: Verifying the hope page url

  # Note "And" statement need no step-definition can be used to concatenate given preconditions

  Scenario: The BundID website has the correct title
    Given The user open the Website "https://test.id.bund.de/de" with the "firefox" browser
    Then The page title of the Website-Title should be "ANMELDEN"

