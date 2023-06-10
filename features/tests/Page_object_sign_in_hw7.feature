# Created by sharekovi at 6/10/23
Feature: Page Object test

#
  Scenario: User can search for table on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown for "table"

  Scenario:: Logged out user sees Sign in page when clicking Orders

  Given Open Amazon page
  When Click Amazon Orders
  Then Verify Sign In page is opened

Scenario: 'Your Shopping Cart is empty' shown if no product added

 Given Open Amazon page
 When Click on cart icon
 Then Verify 'Your Shopping Cart is empty.' text present

