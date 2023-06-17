
Feature: Test for Window handling


Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon T&C page
 When Store original window
 And Click on Amazon Privacy Notice link
 And Switch to the new opened window
 Then Verify Amazon Privacy Notice page is opened
 And User can close new window
 And Return back to original window