Feature: ReqRes GET /users positive scenarios

  Background:
    * url 'https://reqres.in'

  Scenario: Successful GET /users?page=2 returns 200 and user list
    Given path 'api/users'
    And param page = 2
    When method get
    Then status 200
    And match response.page == 2
    And match response.data == '#[] notnull'


