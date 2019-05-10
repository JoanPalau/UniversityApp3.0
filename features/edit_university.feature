Feature: Edit University
  In order to keep updated my previous registers about universities
  As a user
  I want to edit a University register I created

  Background: There are registered a user and University by one of them
    Given Exists a user "user" with password "password"
    And Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists University registered by "user1"
      | name              | description                   |
      | The University    | This is a brief description.  |

  Scenario: Edit owned University registry description
    Given I login as user "user1" with password "password"
    When edit the university with name "The University"
      | description                   |
      | This an other description.  |
  Then I'm viewing the details page for University by "user1"
      | name              | description                     |
      | The University    | This is an other description.   |
  And There are 1 Universities
