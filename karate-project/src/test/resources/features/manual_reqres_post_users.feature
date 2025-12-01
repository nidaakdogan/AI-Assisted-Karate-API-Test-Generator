Feature: ReqRes POST /users positive scenarios

  Background:
    * url 'https://reqres.in'

  Scenario: Successful POST /users creates a user
    Given path 'api/users'
    And request { name: 'Nida', job: 'QA Engineer' }
    When method post
    Then status 201
    And match response.name == 'Nida'
    And match response.job == 'QA Engineer'
    And match response.id == '#string'
    And match response.createdAt == '#string'


