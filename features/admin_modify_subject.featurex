Feature: Admin Modifies Subject
  In order to update the content for my users
  As an admin
  I want to modify some Subject info

  Background: There is a registered admin
    Given Exists an admin "admin" with password "password"
    And Exists University registered
    And Exists Degree registered
    And Exists Subject registered

  Scenario: Modify just Degree description
    Given I login as admin "admin" with password "password"
    When I edit the Subject with name "Xarxes"
      | description |
      | Assignatura on aprendras el veritable signigicat de RTFM |
    Then I'm viewing the details page for the Subject
      | name      | ects | description |
      | Xarxes    | 9    | Assignatura on aprendras el veritable signigicat de RTFM |
    And There is 1 Subject