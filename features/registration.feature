Feature: Rejestracja nowego użytkownika
  Jako potencjalny klient siłowni
  Chcę móc zarejestrować nowe konto
  Aby móc korzystać z systemu rezerwacji

  Scenario: Pomyślna rejestracja nowego klienta
    Given otwieram stronę główną aplikacji
    When klikam w link "Register"
    And wypełniam pole "username" wartością "jankowalski"
    And wypełniam pole "email" wartością "jan.kowalski@example.com"
    And wypełniam pole "password" wartością "bezpieczne123"
    And wybieram rolę "client"
    And klikam przycisk "Register"
    Then powinienem zobaczyć komunikat "Registration successful"
    And powinienem być przekierowany na stronę logowania

  Scenario: Rejestracja z istniejącą nazwą użytkownika
    Given że użytkownik "jankowalski" już istnieje
    And otwieram stronę rejestracji
    When wypełniam pole "username" wartością "jankowalski"
    And wypełniam pole "email" wartością "inny@example.com"
    And wypełniam pole "password" wartością "haslo123"
    And wybieram rolę "client"
    And klikam przycisk "Register"
    Then powinienem zobaczyć komunikat błędu "Username already exists"
