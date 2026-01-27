Feature: Logowanie do systemu
  Jako zarejestrowany użytkownik
  Chcę móc się zalogować do systemu
  Aby uzyskać dostęp do moich funkcjonalności

  Scenario: Pomyślne logowanie klienta
    Given że użytkownik klienta istnieje z danymi:
      | username | testclient |
      | password | test123    |
    When otwieram stronę logowania
    And wypełniam pole "username" wartością "testclient"
    And wypełniam pole "password" wartością "test123"
    And klikam przycisk "Login"
    Then powinienem zobaczyć komunikat "Welcome back"
    And powinienem być na stronie dashboard klienta

  Scenario: Pomyślne logowanie recepcjonisty
    Given że użytkownik recepcjonisty istnieje z danymi:
      | username | receptionist |
      | password | admin123     |
    When otwieram stronę logowania
    And wypełniam pole "username" wartością "receptionist"
    And wypełniam pole "password" wartością "admin123"
    And klikam przycisk "Login"
    Then powinienem zobaczyć dashboard recepcjonisty

  Scenario: Logowanie z błędnym hasłem
    Given że użytkownik klienta istnieje z danymi:
      | username | testclient |
      | password | test123    |
    When otwieram stronę logowania
    And wypełniam pole "username" wartością "testclient"
    And wypełniam pole "password" wartością "zlehaslo"
    And klikam przycisk "Login"
    Then powinienem zobaczyć komunikat błędu "Invalid username or password"
