Feature: Wypożyczanie butów wspinaczkowych
  Jako recepcjonista
  Chcę móc wypożyczać i przyjmować zwroty butów
  Aby zarządzać inwentarzem siłowni

  Background:
    Given że jestem zalogowany jako recepcjonista
    And przechodzę do strony zarządzania butami

  Scenario: Dodawanie nowych butów do inwentarza
    When klikam na formularz dodawania butów
    And wypełniam pole "size" wartością "9.5"
    And klikam przycisk "Add Shoes"
    Then powinienem zobaczyć komunikat "Added shoes"
    And buty rozmiaru "9.5" powinny być widoczne w liście

  Scenario: Wypożyczanie butów klientowi
    Given że w inwentarzu są dostępne buty ID "1"
    And użytkownik "testclient" istnieje
    When wypełniam formularz wypożyczenia:
      | shoe_id  | 1          |
      | username | testclient |
    And klikam przycisk "Rent Shoes"
    Then powinienem zobaczyć komunikat "Rented shoes"
    And buty powinny mieć status "Rented"
    And w kolumnie "Rented By" powinienem zobaczyć "testclient"

  Scenario: Zwrot wypożyczonych butów
    Given że buty ID "1" są wypożyczone przez "testclient"
    When wypełniam pole "shoe_id" wartością "1" w formularzu zwrotu
    And klikam przycisk "Return Shoes"
    Then powinienem zobaczyć komunikat "Returned shoes"
    And buty powinny mieć status "Available"
