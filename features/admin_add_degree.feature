Feature: Admin Adds Degree
  In order to provide content to my users
  As an admin
  I want to register a University with all it's information

  Background: There is a registered admin and university
    Given Exists an admin "admin" with password "password"
    And Exists University registered

  Scenario: Register a Degree with all info
    Given I login as admin "admin" with password "password"
    And
    When I register the Degree
      | title                     | ects | description | university |
      | Enginyeria en Telecomunicacions    | 240  | Grau en enginyeria, amb moltes mates i males persones | 1 |
    Then I'm viewing the details page for the Degree
      | title                     | ects | description | university |
      | Enginyeria en Telecomunicacions    | 240  | Grau en enginyeria, amb moltes mates i males persones | 1 |
    And There are 3 Degrees