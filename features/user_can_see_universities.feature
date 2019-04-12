Feature: User sees different universities
  In order to get information
  As a user
  I want to access universities page


  Scenario: Enter universities but there is none registered
    Given There is no university registered
    When I enter "/universities"
    Then I should see "Sorry, No universities registered yet."
    And There are 0 University

  Scenario: Enter universities and there is one registered
    Given There are one universities registered:
      | id | name | telephone | location |
      | 0  | Universitat Politecnica de Catalunya | 934 016 200 | 0 |
    And their location is also registered:
      | id | address | zipcode | city | country | lat | long |
      | 0  | Campus Nord, Carrer de Jordi Girona | 08034 | Barcelona | Spain | 0.0 | 0.0 |
    When I enter "/universities"
    Then I'm viewing a list of Universities containing
      | name |
      | Campus Nord, Carrer de Jordi Girona |
    And The list contains 1 University


  Scenario: Enter universities and there are multiple registered
    Given There are 2 universities registered:
      | id | name | telephone | location |
      | 0  | Universitat Politecnica de Catalunya | 934 016 200 | 0 |
      | 1  | Universitat de Lleida                | 973 003 588 | 1 |
    And their location is also registered:
      | id | address | zipcode | city | country | lat | long |
      | 0  | Campus Nord, Carrer de Jordi Girona | 08034 | Barcelona | Spain | 0.0 | 0.0 |
      | 1  | Plasa de Victor Siurana, 1 | 25003 | Lleida | Spain | 0.0 | 0.0 |
    When I enter "/universities"
    Then I'm viewing a list of Universities containing
      | name |
      | Campus Nord, Carrer de Jordi Girona |
      | Plasa de Victor Siurana, 1          |
    And The list contains 2 University