Feature: Zakup karnetu
  Jako zalogowany klient
  Chcę móc kupić karnet wstępu
  Aby móc rezerwować wizyty na siłowni

  Background:
    Given że jestem zalogowany jako klient "testclient"

  Scenario: Zakup karnetu 10-wejściowego
    When przechodzę do strony zakupu karnetów
    And wybieram karnet "10-entry"
    And klikam przycisk zakupu
    Then powinienem zobaczyć komunikat "Successfully purchased"
    And powinienem mieć aktywny karnet "10-entry" z 10 wejściami

  Scenario: Zakup karnetu 30-dniowego
    When przechodzę do strony zakupu karnetów
    And wybieram karnet "30-day"
    And klikam przycisk zakupu
    Then powinienem zobaczyć komunikat "Successfully purchased"
    And powinienem mieć aktywny karnet "30-day"

  Scenario: Próba zakupu drugiego karnetu gdy mam aktywny
    Given że mam już aktywny karnet
    When przechodzę do strony zakupu karnetów
    Then wszystkie przyciski zakupu powinny być wyłączone
    And powinienem zobaczyć informację o aktywnym karnecie
