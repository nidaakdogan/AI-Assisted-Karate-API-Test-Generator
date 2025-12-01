Feature: AI generated negative scenarios for ReqRes POST /users

  Background:
    * url 'https://reqres.in'
    * def endpoint = 'api/users'

  Scenario: Negative POST /users - missing name
    Given path endpoint
    And request {"job": "QA Engineer"}
    When method post
    Then status 400

  Scenario: Negative POST /users - missing job
    Given path endpoint
    And request {"name": "Nida"}
    When method post
    Then status 400

  Scenario: Negative POST /users - wrong type name
    Given path endpoint
    And request {"name": 123, "job": "QA Engineer"}
    When method post
    Then status 400

  Scenario: Negative POST /users - wrong type job
    Given path endpoint
    And request {"name": "Nida", "job": 123}
    When method post
    Then status 400

  Scenario: Negative POST /users - empty body
    Given path endpoint
    And request {}
    When method post
    Then status 400
