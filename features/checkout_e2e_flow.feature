Feature: E2E Pet creation and checkout

  Scenario: Create a pet via API and login via UI and use the pet id in the checkout page Zip code field
    Given I create a pet via API
    When I login to the application
    Then I should see the inventory page
    And the pet ID should not be null
    When click on Shopping cart link after adding an item
    Then I should see cart page
    When I click on checkout button
    Then I should see checkout page
    When I enter checkout information
    And I click on continue
    Then Make sure finish button is visible
    And Make sure the same item which is added in listing page exist in checkout