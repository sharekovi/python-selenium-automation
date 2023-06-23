# Created by sharekovi at 6/10/23
Feature: Page Object test

#

  Scenario: Logged out user sees Sign in page when clicking Orders

 Given Open amazon main page
 When Click Amazon Orders link
 Then Verify Sign In page opens


