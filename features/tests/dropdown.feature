
Feature:Dropdown test


  Scenario: User can search for an item in a different Amazon department.
  Given Open amazon main page
  When Select department alexa skills
  When Search for echo dot
  Then verify correct department shown



 Scenario: User can see language option
   Given  Open amazon main page
   When   Hover over language options
   Then   Verify Spanish option present



