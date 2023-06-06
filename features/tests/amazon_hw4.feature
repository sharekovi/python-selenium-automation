
Feature: Amazon Cart Product Test



   Scenario: User can add a product to the cart
      Given Open amazon main page
      When Search for coffee
      And Click on the first product
      And Store product name
      And Click on Add to cart button
      And Open cart page
      Then Verify cart has 1 item(s)
      And Verify cart has correct product
      




