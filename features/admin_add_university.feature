Feature: Admin Adds University
  In order to provide content to my users
  As an admin
  I want to register a University with all it's information

  Background: There is a registered admin
    Given Exists an admin "admin" with password "password"

  Scenario: Register a University without location info
    Given I login as admin "admin" with password "password"
    When I register the University
      | name            | telephone |
      | Universitat de Lleida    | 973256423    |
    Then I'm viewing the details page for the University
      | name            | telephone |
      | Universitat de Lleida    | 973256423    |
    And There is 1 University