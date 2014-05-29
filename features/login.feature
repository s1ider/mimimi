Feature: Login

    Scenario: Incorrect email address
        Given I am on 'Home' page
        When Enter text 'r2d2@getgoing.com' in textedit with label 'Email address'
        When Enter text 'wrong_password' in textedit with label 'Password'
        And Click on button 'Sign In'
        Then Text 'not the right password' should be displayed


