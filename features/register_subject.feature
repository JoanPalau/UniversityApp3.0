Feature: Register Subject
  In order to report about the subject in a degree
  As a user
  I want to register a subject in the corresponding degree together with its details

  Background: There is a registered user and University and degree
    Given Exists a user "user" with password "password"
    And Exists University registered by "user"
      | name            |
      | The University  |
    And Exists degree registered by "user" in "The University"
      | title         |
      | The Degree    |

  Scenario: Register just subject name
    Given I login as user "user" with password "password"
    When I register a subject at "The University" in "The Degree"
      | name          | _course  |
      | First subject | 1       |
    Then I'm viewing the details page for the subject at University "The University" in "The Degree" by "user"
      | name          | _course  |
      | First subject | 1       |
    And There are 1 subject