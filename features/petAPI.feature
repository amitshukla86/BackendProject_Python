Feature: Verify pet API is working correctly

    Scenario: Verify user is able to retrieve the pet ID's using the API
        Given: Pet ID's are available in the DB
        When: We execute the rest API
        Then: List is successfully retrieved

