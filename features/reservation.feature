Feature: Rezerwacja slotu czasowego
  Jako klient z aktywnym karnetem
  Chcę móc zarezerwować wizytę na siłowni
  Aby zaplanować swój trening

  Background:
    Given że jestem zalogowany jako klient "testclient"
    And mam aktywny karnet z 10 wejściami

  Scenario: Pomyślna rezerwacja wolnego slotu
    When przechodzę do strony przeglądania slotów
    And wybieram jutrzejszą datę
    And wybieram slot czasowy "09:00-11:00"
    And klikam przycisk rezerwacji
    Then powinienem zobaczyć komunikat "Reservation created successfully"
    And rezerwacja powinna pojawić się na moim dashboardzie

  Scenario: Próba rezerwacji bez karnetu
    Given że nie mam aktywnego karnetu
    When próbuję zarezerwować slot "09:00-11:00" na jutro
    Then powinienem zobaczyć komunikat błędu "need a valid pass"

  Scenario: Przeglądanie dostępnych slotów
    When przechodzę do strony przeglądania slotów
    Then powinienem zobaczyć listę dostępnych terminów
    And każdy slot powinien pokazywać liczbę wolnych miejsc
