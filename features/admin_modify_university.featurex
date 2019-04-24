Feature: Admin Modifies University
  In order to update the content for my users
  As an admin
  I want to modify some University info

    Background: There is a registered admin
    Given Exists an admin "admin" with password "password"
    And Exists University registered

  Scenario: Modify just University telephone
    Given I login as admin "admin" with password "password"
    When I edit the University
      | telephone |
      | 973256424    |
    Then I'm viewing the details page for the University
      | name            | telephone |
      | Universitat de Lleida    | 973256424    |
    And There is 1 University