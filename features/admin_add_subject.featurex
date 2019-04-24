Feature: Admin Adds Subject
  In order to provide content to my users
  As an admin
  I want to register a University with all it's information

  Background: There is a registered admin, university and degree
    Given Exists an admin "admin" with password "password"
    And Exists University registered
    And Exists Degree registered

  Scenario: Register a Subject with all info
    Given I login as admin "admin" with password "password"
    When I register the Subject
      | name            | ects | description |
      | Projecte Web    | 6    | Assignatura de 3r curs |
    Then I'm viewing the details page for the Subject
      | name            | ects | description |
      | Projecte Web    | 6    | Assignatura de 3r curs |
    And There is 1 Subject