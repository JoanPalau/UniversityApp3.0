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
        | name            | description         |
        | The First       | First description   |
      When I list Universities
      Then I'm viewing a list containing
        | name            |
        | The First       |
      And The list contains 1 Universities


    Scenario: List the Universities
      Given Exists University registered by "user"
        | name            | description         |
        | The First       | First description   |
        | The Second      | Second description  |
        | The Third       | Third description   |
        | The Fourth      | Fourth description  |
        | The Fifth       | Fifth description   |
      When I list Universities
      Then I'm viewing a list containing
        | name            |
        | The First       |
        | The Second      |
        | The Third       |
        | The Fourth      |
        | The Fifth       |
      And The list contains 5 Universities