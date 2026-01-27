Feature: Zarządzanie rezerwacjami przez recepcjonistę
  Jako recepcjonista
  Chcę móc zarządzać rezerwacjami klientów
  Aby kontrolować wejścia na siłownię

  Background:
    Given że jestem zalogowany jako recepcjonista

  Scenario: Potwierdzanie rezerwacji klienta
    Given że istnieje oczekująca rezerwacja dla użytkownika "testclient"
    When przechodzę do dashboardu recepcjonisty
    And znajduję rezerwację użytkownika "testclient"
    And klikam przycisk "Confirm"
    Then powinienem zobaczyć komunikat "Entry confirmed successfully"
    And status rezerwacji powinien zmienić się na "Confirmed"

  Scenario: Odrzucanie rezerwacji
    Given że istnieje oczekująca rezerwacja dla użytkownika "testclient"
    When przechodzę do dashboardu recepcjonisty
    And znajduję rezerwację użytkownika "testclient"
    And klikam przycisk "Decline"
    Then powinienem zobaczyć komunikat "Reservation declined"
    And status rezerwacji powinien zmienić się na "Cancelled"

  Scenario: Wyszukiwanie rezerwacji po użytkowniku
    Given że istnieje rezerwacja dla użytkownika "testclient"
    When przechodzę do strony wyszukiwania rezerwacji
    And wpisuję "testclient" w pole wyszukiwania
    And klikam przycisk "Search"
    Then powinienem zobaczyć rezerwacje użytkownika "testclient"

  Scenario: Sortowanie rezerwacji według statusu pending
    Given że istnieją rezerwacje z różnymi statusami
    When przechodzę do dashboardu recepcjonisty
    And wybieram sortowanie "Pending First"
    Then rezerwacje ze statusem "Pending" powinny być na górze listy
