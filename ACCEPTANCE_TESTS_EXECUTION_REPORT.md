# Raport Wykonania Testów Akceptacyjnych
## Boulder Gym Management System

**Data wykonania:** 27 stycznia 2025  
**Framework testowy:** Behave 1.2.6 (BDD/Gherkin)  
**Narzędzie automatyzacji:** Selenium WebDriver 4.15.2  
**Przeglądarka:** Chrome (headless mode)

---

## 1. Podsumowanie Struktury Testów

### Przegląd Funkcji Testowych

| Feature | Liczba Scenariuszy | Liczba Kroków | Plik |
|---------|-------------------|---------------|------|
| Rejestracja nowego użytkownika | 2 | 16 | [registration.feature](features/registration.feature) |
| Logowanie do systemu | 3 | 21 | [login.feature](features/login.feature) |
| Zakup karnetu | 3 | 14 | [pass_purchase.feature](features/pass_purchase.feature) |
| Rezerwacja slotu czasowego | 3 | 16 | [reservation.feature](features/reservation.feature) |
| Zarządzanie rezerwacjami przez recepcjonistę | 4 | 25 | [receptionist.feature](features/receptionist.feature) |
| Wypożyczanie butów wspinaczkowych | 3 | 27 | [shoes_rental.feature](features/shoes_rental.feature) |

**RAZEM:** 6 funkcji, 18 scenariuszy, 119 kroków testowych

---

## 2. Pokrycie Funkcjonalności Systemu

### 2.1 Moduł Rejestracji i Autoryzacji
- ✓ Rejestracja nowego klienta z walidacją danych
- ✓ Walidacja unikalności nazwy użytkownika
- ✓ Logowanie klienta
- ✓ Logowanie recepcjonisty
- ✓ Obsługa nieprawidłowych danych logowania

### 2.2 Moduł Karnetów
- ✓ Zakup karnetu 10-wejściowego
- ✓ Zakup karnetu 30-dniowego
- ✓ Blokada zakupu dodatkowego karnetu przy aktywnym karnecie

### 2.3 Moduł Rezerwacji
- ✓ Tworzenie rezerwacji przez klienta
- ✓ Walidacja posiadania aktywnego karnetu
- ✓ Przeglądanie dostępnych slotów czasowych
- ✓ Wyświetlanie liczby wolnych miejsc

### 2.4 Moduł Recepcjonisty
- ✓ Potwierdzanie rezerwacji klienta (zmiana statusu na "Confirmed")
- ✓ Odrzucanie rezerwacji (zmiana statusu na "Cancelled")
- ✓ Wyszukiwanie rezerwacji po nazwie użytkownika
- ✓ Sortowanie rezerwacji według statusu "Pending First"

### 2.5 Moduł Wypożyczania Butów
- ✓ Dodawanie nowych butów do inwentarza
- ✓ Wypożyczanie butów klientowi z przypisaniem użytkownika
- ✓ Zwrot wypożyczonych butów

---

## 3. Struktura Testów BDD

### Wzorce Given-When-Then

Testy zostały napisane zgodnie z metodologią BDD (Behavior-Driven Development) używając składni Gherkin:

```gherkin
Feature: Nazwa funkcjonalności
  Jako [rola użytkownika]
  Chcę [co chcę zrobić]
  Aby [cel biznesowy]

  Scenario: Nazwa scenariusza testowego
    Given [warunki początkowe]
    When [akcja wykonana przez użytkownika]
    And [dodatkowa akcja]
    Then [oczekiwany rezultat]
    And [dodatkowa weryfikacja]
```

### Przykład Scenariusza Testowego

```gherkin
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
```

---

## 4. Implementacja Kroków Testowych

### Pliki Step Definitions

| Plik | Cel | Liczba Kroków |
|------|-----|---------------|
| `common_steps.py` | Wspólne akcje (nawigacja, formularze, asercje) | 11 kroków |
| `user_steps.py` | Operacje użytkowników (rejestracja, logowanie) | 12 kroków |
| `pass_steps.py` | Zakup i zarządzanie karnetami | 7 kroków |
| `reservation_steps.py` | Rezerwacje slotów czasowych | 11 kroków |
| `receptionist_steps.py` | Funkcje recepcjonisty | 7 kroków |
| `shoes_steps.py` | Wypożyczanie butów | 10 kroków |

### Przykład Implementacji Kroku

```python
@when('wypełniam pole "{field_name}" wartością "{value}"')
def step_fill_field(context, field_name, value):
    field = context.driver.find_element(By.NAME, field_name)
    field.clear()
    field.send_keys(value)
```

---

## 5. Konfiguracja Środowiska Testowego

### environment.py
Plik `features/environment.py` konfiguruje:
- Inicjalizację przeglądarki Chrome (tryb headless)
- Utworzenie bazy danych testowej
- Automatyczne czyszczenie danych po testach
- Zamknięcie przeglądarki po zakończeniu

### behave.ini
```ini
[behave]
default_format = pretty
show_skipped = false
show_timings = true
color = true
```

---

## 6. Zależności Projektowe

### requirements-acceptance.txt
```
behave==1.2.6
selenium==4.15.2
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Werkzeug==3.0.1
```

---

## 7. Uruchamianie Testów

### Instalacja Zależności
```bash
pip install -r requirements-acceptance.txt
```

### Uruchomienie Wszystkich Testów
```bash
behave
```

### Uruchomienie Konkretnej Funkcji
```bash
behave features/registration.feature
```

### Tryb Dry-Run (Walidacja Struktury)
```bash
behave --dry-run
```

### Generowanie Raportu JSON
```bash
behave --format json --outfile test_results.json
```

---

## 8. Architektura Testów

### Wzorzec Page Object Model (Implicit)
Kroki testowe wykorzystują wzorce lokalizacji elementów:
- `By.NAME` - dla pól formularzy
- `By.LINK_TEXT` - dla linków nawigacyjnych
- `By.XPATH` - dla specyficznych elementów (przyciski, komunikaty)
- `By.ID` - dla identyfikowalnych elementów

### Separacja Warstw
1. **Feature Files** - Język naturalny (polski), opisy biznesowe
2. **Step Definitions** - Implementacja w Pythonie, interakcja z Selenium
3. **Environment Setup** - Konfiguracja środowiska, baza danych, przeglądarka

---

## 9. Najlepsze Praktyki Zastosowane

### BDD Best Practices
✓ Scenariusze napisane językiem biznesowym (polski)  
✓ Każdy scenariusz jest niezależny i może być uruchomiony osobno  
✓ Wykorzystanie `Background` dla wspólnych kroków przygotowawczych  
✓ Czytelne nazwy kroków odzwierciedlające intencje użytkownika  

### Selenium Best Practices
✓ Headless mode dla szybkiego wykonania testów  
✓ Automatyczne czyszczenie danych testowych  
✓ Waity implicit dla stabilności testów  
✓ Izolacja testów poprzez świeżą bazę danych  

### Organizacja Kodu
✓ Grupowanie kroków według funkcjonalności (moduły step definitions)  
✓ Reużywalne kroki w `common_steps.py`  
✓ Parametryzacja kroków dla elastyczności  

---

## 10. Wartość Biznesowa Testów Akceptacyjnych

### Korzyści dla Projektu
1. **Dokumentacja Żywa** - Feature files służą jako dokumentacja systemu
2. **Współpraca** - Język naturalny umożliwia dyskusję z interesariuszami
3. **Regression Testing** - Automatyczne sprawdzanie, czy nowe zmiany nie psują funkcjonalności
4. **Confidence** - Pewność, że system działa zgodnie z wymaganiami

### Pokrycie User Stories
Testy pokrywają główne ścieżki użytkownika:
- Nowy użytkownik rejestruje się i kupuje karnet
- Klient rezerwuje wizytę i przychodzi na siłownię
- Recepcjonista zarządza wejściami i wypożycza buty
- System waliduje reguły biznesowe (karnet, dostępność miejsc)

---

## 11. Możliwości Rozwoju

### Przyszłe Usprawnienia
- [ ] Integracja z CI/CD (GitHub Actions, Jenkins)
- [ ] Generowanie raportów HTML (Allure, Behave HTML)
- [ ] Testy wydajnościowe (liczba równoczesnych użytkowników)
- [ ] Screenshot'y przy błędach testowych
- [ ] Testy API (REST endpoints)
- [ ] Cross-browser testing (Firefox, Edge)

---

## 12. Wnioski

System testów akceptacyjnych dla Boulder Gym Management System:
- **18 scenariuszy** pokrywających wszystkie kluczowe funkcjonalności
- **119 kroków testowych** zaimplementowanych w Pythonie
- **6 modułów** funkcjonalnych przetestowanych end-to-end
- **BDD approach** zapewniający czytelność i współpracę z biznesem

Testy są gotowe do uruchomienia i mogą być włączone do pipeline'u CI/CD dla ciągłej walidacji jakości systemu.

---

**Autor:** GitHub Copilot (Claude Sonnet 4.5)  
**Wersja dokumentu:** 1.0  
**Status:** Kompletny i gotowy do użycia
