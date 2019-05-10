Feature: View University
  In order to know about a University
  As a user
  I want to view the University details including all its degrees

  Background: There is one University with 2 degrees and another without
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists University registered by "user1"
      | name            | description         |
      | The First       | First description   |
    #And Exists degree at University "The First" by "user1"
    #  | name          |
    #  | Degree 1      |
    #  | Degree other  |
    And Exists University registered by "user2"
      | name            | description         |
      | The Second      | Second description  |

  Scenario: View details for owned University with two degrees
    Given I login as user "user1" with password "password"
    When I view the details for University "The First"
    #Then I'm viewing a University degrees list containing
    # | name          |
    # | Degree 1      |
    # | Degree other  |
    #And The list contains 2 degrees

  Scenario: View details for owned University with zero degrees
    Given I login as user "user2" with password "password"
    When I view the details for University "The Second"
    Then I'm viewing a University degrees list containing
     | name          |
    And The list contains 0 degrees

  Scenario: View details for University with 2 degree when not logged in
    Given I'm not logged in
    When I view the details for University "The First"
    #Then I'm viewing a University degrees list containing
    # | name          |
    # | Degree 1      |
    # | Degree other  |
    #And The list contains 2 degrees