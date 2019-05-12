Feature: Edit Degree
  In order to keep updated my previous registers about degrees
  As a user
  I want to edit a degree register I created

  Background: There are registered user and a degree by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists University registered by "user1"
    | name              | description                   |
    | The University    | This is a brief description.  |
    And Exists degree registered by "user1" in "The University"
    | title          |
    | First degree   |

  Scenario: Edit owned degree
    Given I login as user "user1" with password "password"
    # When I'm viewing the details page for degree at University "The University" by "User1"