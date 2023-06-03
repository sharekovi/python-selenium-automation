
Feature: Amazon Search test


  Scenario:User can search for table on Amazon
  Given  Open amazon main page
  When  Search for table
  Then Verify search result shown for "table"


      Scenario:User can search for coffee on Amazon
  Given  Open amazon main page
  When  Search for coffee
  Then Verify search result shown for "coffee"

