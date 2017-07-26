Feature: Contact group CRUD
    Description

   Scenario Outline: Add new group
       Given a group list
       Given a new group with <name>, <header>, <footer>
       When I add this group to the list
       Then a new group list is equal to the old list with this new group

       Examples:
       | name        | header       | footer |
       | pety        | Old header   | test   |
       | 123432$%^   | &$*#%&^%     | 12314  |
       | опачки      | новая группа | упс    |