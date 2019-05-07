Feature: List Universities
  In order to keep myself up to date about universities registered in UniApp
  As a user
  I want to list all registered Universities

  Background: There are not registered Universities
    Given Exists a user "user" with password "password"

    Scenario: List the Universities
      When I list Universities
      Then The list contains 0 Universities


    Scenario: List the Universities
      Given Exists University registered by "user"
        | name            | description         | telephone     |
        | The First       | First description   | +34 973003588 |
      When I list Universities
      Then I'm viewing a list containing
        | name            |
        | The First       |
      And The list contains 1 Universities


    Scenario: List the Universities
      Given Exists University registered by "user"
        | name            | description         | telephone     |
        | The Second      | Second description  | +34 973003589 |
        | The Third       | Third description   | +34 973003580 |
        | The Fourth      | Fourth description  | +34 973003581 |
        | The Fifth       | Fifth description   | +34 973003582 |
      When I list Universities
      Then I'm viewing a list containing
        | name            |
        | The First       |
        | The Second      |
        | The Third       |
        | The Fourth      |
        | The Fifth       |
      And The list contains 5 Universities