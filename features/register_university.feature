Feature: Register University
  In order to keep track of the universities where I studied
  As a user
  I want to register a University together with its image, name and description

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just University name
    Given I login as user "user" with password "password"
    When I register a University
      | name              |
      | The University  |
    Then I'm viewing the details page for University by "user"
      | name              |
      | The University    |
    And There are 1 Universities


  Scenario: Register just University name and description
    Given I login as user "user" with password "password"
    When I register a University
      | name              | description                   |
      | The University    | This is a brief description.  |
    Then I'm viewing the details page for University by "user"
      | name              | description                   |
      | The University    | This is a brief description.  |
    And There are 1 Universities


  Scenario: Try to register a University but not logged in
    Given I'm not logged in
    When I register a University
      | name              | description                   |
      | The University    | This is a brief description.  |
    Then I'm redirected to the login form
    And There are 0 Universities