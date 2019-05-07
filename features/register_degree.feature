Feature: Register Degree
  In order to promote a degrees in my University
  As a user
  I want to register a degree in the corresponding University together with its details

  Background: There is a registered user and University
    Given Exists a user "user" with password "password"
    And Exists University registered by "user"
      | name            |
      | The University  |

  Scenario: Register just degree title
    Given I login as user "user" with password "password"
    When I register a degree at University "The University"
      | name          |
      | First degree  |
    Then I'm viewing the details page for degree at University "The University" by "user"
      | name          |
      | First degree  |
    And There are 1 degree