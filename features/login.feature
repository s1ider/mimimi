Feature: Login

    Scenario: Incorrect password
        Given I am on 'Home' page
        When Fill form:
            | label         | value             |
            | Email address | r2d2@getgoing.com |
            | Password      | wrong_password    |
        And Click on button 'Sign In'
        Then Text 'not right password' should be displayed

