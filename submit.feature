Scenario: Displaying error in username in a form
Given I am in a user form
When I do not enter value in the text field
And I click the Submit button
Then I get alert box stating username is not entered


