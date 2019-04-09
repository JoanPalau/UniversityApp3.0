Feature: Admin Modifies Degree
  In order to update the content for my users
  As an admin
  I want to modify a Degree info

  Background: There is a registered admin
    Given Exists an admin "admin" with password "password"
    And Exists University registered
    And Exists Degree registered
      | title                     | ects | description | university |
      | Enginyeria Informatica    | 240  | Grau en enginyeria, molt guay | 0 |

    Scenario: Modify just Degree description
      Given I login as admin "admin" with password "password"
      When I edit the Degree with name "Enginyeria Informatica"
        | description |
        | Grau acreditat i que dura 4 anys |
      Then I'm viewing the details page for the Degree
        | title                     | ects | description | university |
        | Enginyeria Informatica    | 240  | Grau en enginyeria, molt guay | 0 |
      And There are 2 Degrees