# Plan Testów Manualnych - Boulder Gym Application

## Informacje Podstawowe
- **Aplikacja**: Boulder Gym Management System
- **Wersja**: 1.0
- **Data przygotowania**: 27 stycznia 2026
- **Typ testów**: Testy manualne (ręczne)
- **Środowisko**: Localhost (http://127.0.0.1:5000)
- **Przeglądarki**: Chrome, Firefox, Edge

## Cel Testów Manualnych

Manualna weryfikacja funkcjonalności aplikacji z perspektywy użytkownika końcowego, sprawdzenie interfejsu użytkownika, doświadczenia użytkownika (UX) oraz przypadków brzegowych, które mogą nie być pokryte przez testy automatyczne.

---

## TC-001: Rejestracja Nowego Użytkownika (Klient)

**Priorytet**: Wysoki  
**Czas trwania**: ~5 minut  
**Cel**: Weryfikacja procesu rejestracji nowego klienta

### Warunki wstępne:
- Aplikacja uruchomiona
- Baza danych czysta lub użytkownik "testuser123" nie istnieje

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Otwórz http://127.0.0.1:5000 | Wyświetla się strona główna |
| 2 | Kliknij link "Register" | Przekierowanie do /register |
| 3 | Wypełnij pole "Username": `testuser123` | Pole przyjmuje tekst |
| 4 | Wypełnij pole "Email": `test@example.com` | Pole przyjmuje tekst |
| 5 | Wypełnij pole "Password": `Test123!` | Hasło jest maskowane (***) |
| 6 | Wybierz "Role": `Client` | Rozwijana lista pozwala wybrać Client |
| 7 | Kliknij przycisk "Register" | Przekierowanie do /login |
| 8 | Sprawdź komunikat flash | Wyświetla "Registration successful" |

### Warunki końcowe:
- Nowy użytkownik został utworzony w bazie danych
- Hasło jest zahashowane
- Użytkownik może się zalogować nowymi danymi

---

## TC-002: Logowanie Klienta

**Priorytet**: Wysoki  
**Czas trwania**: ~3 minuty  
**Cel**: Weryfikacja procesu logowania dla roli Client

### Warunki wstępne:
- Użytkownik `testuser123` istnieje w bazie (hasło: `Test123!`)
- Użytkownik jest wylogowany

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Otwórz http://127.0.0.1:5000/login | Wyświetla formularz logowania |
| 2 | Wypełnij "Username": `testuser123` | Pole przyjmuje tekst |
| 3 | Wypełnij "Password": `Test123!` | Hasło maskowane |
| 4 | Kliknij "Login" | Przekierowanie do /client/dashboard |
| 5 | Sprawdź komunikat flash | "Welcome back, testuser123!" |
| 6 | Sprawdź nagłówek strony | "Client Dashboard" lub podobny |
| 7 | Sprawdź nawigację | Przyciski: Buy Pass, View Slots, Logout |

### Warunki końcowe:
- Użytkownik jest zalogowany
- Sesja jest aktywna

---

## TC-003: Logowanie z Błędnym Hasłem

**Priorytet**: Średni  
**Czas trwania**: ~2 minuty  
**Cel**: Weryfikacja obsługi błędnego hasła

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Otwórz /login | Formularz logowania |
| 2 | Username: `testuser123` | - |
| 3 | Password: `WrongPassword999` | - |
| 4 | Kliknij "Login" | Pozostaje na /login |
| 5 | Sprawdź komunikat | "Invalid username or password" (czerwony) |

---

## TC-004: Zakup Karnetu 10-Wejściowego

**Priorytet**: Wysoki  
**Czas trwania**: ~5 minut  
**Cel**: Zakup karnetu przez zalogowanego klienta

### Warunki wstępne:
- Użytkownik zalogowany jako klient
- Użytkownik NIE ma aktywnego karnetu

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Z dashboard kliknij "Buy Pass" | Przekierowanie do /client/buy-pass |
| 2 | Sprawdź sekcję "10-Entry Pass" | Widoczna cena 100 PLN, opis |
| 3 | Kliknij przycisk "Get Started" w sekcji 10-Entry | Formularz wysłany |
| 4 | Sprawdź komunikat flash | "Successfully purchased 10-entry pass!" |
| 5 | Wróć do dashboardu | Dashboard pokazuje aktywny karnet |
| 6 | Sprawdź szczegóły karnetu | Typ: 10-entry, Pozostało: 10 wejść |

### Warunki końcowe:
- Karnet zapisany w bazie z `is_active=True`
- Pozostało 10 wejść
- Płatność zarejestrowana (100 PLN)

---

## TC-005: Próba Zakupu Drugiego Karnetu

**Priorytet**: Średni  
**Czas trwania**: ~3 minuty  
**Cel**: Weryfikacja blokady zakupu drugiego aktywnego karnetu

### Warunki wstępne:
- Użytkownik ma już aktywny karnet

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Przejdź do /client/buy-pass | Strona zakupu |
| 2 | Spróbuj kupić dowolny karnet | - |
| 3 | Sprawdź komunikat | "You already have an active pass" (alert lub komunikat) |
| 4 | Sprawdź bazę | Tylko 1 aktywny karnet dla użytkownika |

---

## TC-006: Przeglądanie Dostępnych Slotów

**Priorytet**: Wysoki  
**Czas trwania**: ~4 minuty  
**Cel**: Wyświetlanie listy dostępnych slotów czasowych

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Zaloguj jako klient z karnetem | Dashboard klienta |
| 2 | Kliknij "View Slots" | Przekierowanie do /client/view-slots |
| 3 | Sprawdź listę slotów | Tabela z datami i godzinami |
| 4 | Sprawdź kolumny | Data, Godzina, Maksymalna pojemność |
| 5 | Sprawdź przycisk "Book" | Przy każdym slocie przycisk "Book" |

---

## TC-007: Rezerwacja Slotu

**Priorytet**: Wysoki  
**Czas trwania**: ~5 minut  
**Cel**: Rezerwacja wolnego slotu przez klienta

### Warunki wstępne:
- Klient zalogowany
- Klient ma aktywny karnet z wejściami > 0
- Istnieją dostępne sloty

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Przejdź do /client/view-slots | Lista slotów |
| 2 | Wybierz dowolny slot i kliknij "Book" | Formularz rezerwacji |
| 3 | Kliknij "Confirm Booking" | Przekierowanie |
| 4 | Sprawdź komunikat | "Booking successful!" lub podobny |
| 5 | Sprawdź dashboard | Lista "My Reservations" zawiera nową rezerwację |
| 6 | Sprawdź status | Status: "Pending" |

### Warunki końcowe:
- Rezerwacja w bazie ze statusem "Pending"
- Wejścia z karnetu NIE zostały jeszcze odjęte

---

## TC-008: Próba Rezerwacji Bez Karnetu

**Priorytet**: Średni  
**Czas trwania**: ~3 minuty  
**Cel**: Blokada rezerwacji dla użytkownika bez karnetu

### Warunki wstępne:
- Użytkownik zalogowany BEZ aktywnego karnetu

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Przejdź do /client/view-slots | - |
| 2 | Spróbuj zarezerwować slot | - |
| 3 | Sprawdź komunikat | "You need a valid pass to book an entry" |
| 4 | Sprawdź bazę | Brak nowej rezerwacji |

---

## TC-009: Logowanie Recepcjonisty

**Priorytet**: Wysoki  
**Czas trwania**: ~3 minuty  
**Cel**: Weryfikacja logowania dla roli Receptionist

### Warunki wstępne:
- Użytkownik recepcjonisty istnieje (np. username: `receptionist`, hasło: `admin123`)

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Otwórz /login | Formularz |
| 2 | Username: `receptionist` | - |
| 3 | Password: `admin123` | - |
| 4 | Kliknij "Login" | Przekierowanie do /receptionist/dashboard |
| 5 | Sprawdź nagłówek | "Receptionist Dashboard" |
| 6 | Sprawdź elementy | Tabela rezerwacji, przyciski Confirm/Decline |

---

## TC-010: Potwierdzanie Rezerwacji przez Recepcjonistę

**Priorytet**: Wysoki  
**Czas trwania**: ~5 minut  
**Cel**: Recepcjonista potwierdza wejście klienta

### Warunki wstępne:
- Recepcjonista zalogowany
- Istnieje rezerwacja ze statusem "Pending"
- Klient ma aktywny karnet z wejściami > 0

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Otwórz /receptionist/dashboard | Lista rezerwacji |
| 2 | Znajdź rezerwację ze statusem "Pending" | Wiersz z danymi klienta |
| 3 | Kliknij przycisk "Confirm" przy rezerwacji | Odświeżenie strony |
| 4 | Sprawdź komunikat flash | "Entry confirmed successfully!" |
| 5 | Sprawdź status rezerwacji | Zmieniony na "Confirmed" |
| 6 | Sprawdź kolumnę "Confirmed By" | ID lub nazwa recepcjonisty |
| 7 | Sprawdź karnet klienta | Liczba wejść zmniejszona o 1 |

### Warunki końcowe:
- Status rezerwacji: "Confirmed"
- Wejścia klienta: poprzednia wartość - 1
- Pole `confirmed_by` zawiera ID recepcjonisty

---

## TC-011: Odrzucanie Rezerwacji

**Priorytet**: Średni  
**Czas trwania**: ~3 minuty  
**Cel**: Recepcjonista odrzuca rezerwację

### Warunki wstępne:
- Recepcjonista zalogowany
- Istnieje rezerwacja "Pending"

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Dashboard recepcjonisty | Lista rezerwacji |
| 2 | Znajdź rezerwację "Pending" | - |
| 3 | Kliknij "Decline" | Odświeżenie |
| 4 | Sprawdź komunikat | "Reservation declined" |
| 5 | Sprawdź status | "Declined" |
| 6 | Sprawdź karnet klienta | Wejścia NIE zostały odjęte |

---

## TC-012: Wyszukiwanie Rezerwacji po Username

**Priorytet**: Średni  
**Czas trwania**: ~4 minuty  
**Cel**: Filtrowanie rezerwacji po nazwie użytkownika

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Dashboard recepcjonisty | Lista wszystkich rezerwacji |
| 2 | Wypełnij pole "Search by username": `testuser123` | - |
| 3 | Kliknij "Search" | Lista filtrowana |
| 4 | Sprawdź wyniki | Tylko rezerwacje użytkownika `testuser123` |
| 5 | Wyczyść wyszukiwanie | Ponownie wszystkie rezerwacje |

---

## TC-013: Sortowanie Rezerwacji (Pending First)

**Priorytet**: Niski  
**Czas trwania**: ~3 minuty  
**Cel**: Sortowanie według statusu

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Dashboard recepcjonisty | Lista rezerwacji |
| 2 | Znajdź pole/przycisk "Sort" lub dropdown | - |
| 3 | Wybierz "Pending First" | Lista sortowana |
| 4 | Sprawdź kolejność | Rezerwacje "Pending" na górze |

---

## TC-014: Dodawanie Butów do Inwentarza

**Priorytet**: Średni  
**Czas trwania**: ~4 minuty  
**Cel**: Recepcjonista dodaje nową parę butów

### Warunki wstępne:
- Recepcjonista zalogowany

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Przejdź do /receptionist/manage-shoes | Strona zarządzania butami |
| 2 | Wypełnij "Size": `42` | - |
| 3 | Kliknij "Add Shoes" | Odświeżenie |
| 4 | Sprawdź komunikat | "Shoes added successfully" |
| 5 | Sprawdź tabelę inwentarza | Nowy wpis: rozmiar 42, status: Available |

---

## TC-015: Wypożyczanie Butów Klientowi

**Priorytet**: Średni  
**Czas trwania**: ~5 minut  
**Cel**: Przypisanie butów do klienta

### Warunki wstępne:
- Recepcjonista zalogowany
- Istnieją buty ze statusem "Available"
- Istnieje użytkownik klient

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Strona /receptionist/manage-shoes | Lista butów |
| 2 | Znajdź buty "Available" | - |
| 3 | Przy butach wypełnij pole "Username": `testuser123` | - |
| 4 | Kliknij przycisk "Rent" | Odświeżenie |
| 5 | Sprawdź komunikat | "Shoes rented successfully" |
| 6 | Sprawdź status butów | Zmieniony na "Rented" |
| 7 | Sprawdź kolumnę "Rented To" | `testuser123` |

---

## TC-016: Zwrot Wypożyczonych Butów

**Priorytet**: Średni  
**Czas trwania**: ~3 minuty  
**Cel**: Recepcjonista odbiera buty od klienta

### Warunki wstępne:
- Buty są wypożyczone (status: "Rented")

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Strona manage-shoes | Lista butów |
| 2 | Znajdź buty "Rented" | Kolumna "Rented To" wypełniona |
| 3 | Kliknij przycisk "Return" | Odświeżenie |
| 4 | Sprawdź komunikat | "Shoes returned successfully" |
| 5 | Sprawdź status | Zmieniony na "Available" |
| 6 | Sprawdź "Rented To" | Pole puste (NULL) |

---

## TC-017: Wylogowanie Użytkownika

**Priorytet**: Średni  
**Czas trwania**: ~2 minuty  
**Cel**: Poprawne zakończenie sesji

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Będąc zalogowanym, kliknij "Logout" | Przekierowanie do /login |
| 2 | Spróbuj dostać się do /client/dashboard | Przekierowanie do /login (brak dostępu) |
| 3 | Sprawdź komunikat | "Please log in to access this page" |

---

## TC-018: Responsywność - Urządzenia Mobilne

**Priorytet**: Niski  
**Czas trwania**: ~10 minut  
**Cel**: Sprawdzenie działania na małych ekranach

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Otwórz DevTools (F12) | - |
| 2 | Włącz tryb urządzenia mobilnego | Symulacja telefonu |
| 3 | Wybierz iPhone 12 Pro (390x844) | - |
| 4 | Przejdź przez stronę rejestracji | Formularz czytelny, przyciski klikalne |
| 5 | Zaloguj się | Dashboard działa poprawnie |
| 6 | Sprawdź tabele | Tabele przewijalne lub responsywne |
| 7 | Sprawdź nawigację | Menu/przyciski dostępne |

---

## TC-019: Wydajność - Równoczesne Rezerwacje

**Priorytet**: Niski  
**Czas trwania**: ~15 minut  
**Cel**: Zachowanie podczas wielu użytkowników

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Otwórz aplikację w 3 różnych przeglądarkach | - |
| 2 | Zaloguj 3 różnych klientów | Każdy ma swoją sesję |
| 3 | Wszyscy próbują zarezerwować TEN SAM slot | - |
| 4 | Sprawdź rezultat | Rezerwacje są tworzone (max capacity nie przekroczone) |
| 5 | Sprawdź bazę danych | Integralność danych zachowana |

---

## TC-020: Bezpieczeństwo - Próba Dostępu Bez Uprawnień

**Priorytet**: Wysoki  
**Czas trwania**: ~5 minut  
**Cel**: Weryfikacja autoryzacji

### Kroki testowe:

| Krok | Akcja | Oczekiwany Rezultat |
|------|-------|-------------------|
| 1 | Zaloguj jako klient | Dashboard klienta |
| 2 | W przeglądarce wpisz URL: /receptionist/dashboard | Przekierowanie lub błąd 403 |
| 3 | Sprawdź komunikat | "Unauthorized" lub przekierowanie do /login |
| 4 | Wyloguj się | - |
| 5 | Bez logowania spróbuj wejść na /client/buy-pass | Przekierowanie do /login |

---

## Podsumowanie Przypadków Testowych

| ID | Nazwa | Priorytet | Moduł |
|----|-------|-----------|-------|
| TC-001 | Rejestracja nowego użytkownika | Wysoki | Autentykacja |
| TC-002 | Logowanie klienta | Wysoki | Autentykacja |
| TC-003 | Błędne hasło | Średni | Autentykacja |
| TC-004 | Zakup karnetu 10-entry | Wysoki | Karnety |
| TC-005 | Blokada drugiego karnetu | Średni | Karnety |
| TC-006 | Przeglądanie slotów | Wysoki | Rezerwacje |
| TC-007 | Rezerwacja slotu | Wysoki | Rezerwacje |
| TC-008 | Rezerwacja bez karnetu | Średni | Rezerwacje |
| TC-009 | Logowanie recepcjonisty | Wysoki | Autentykacja |
| TC-010 | Potwierdzanie rezerwacji | Wysoki | Recepcja |
| TC-011 | Odrzucanie rezerwacji | Średni | Recepcja |
| TC-012 | Wyszukiwanie rezerwacji | Średni | Recepcja |
| TC-013 | Sortowanie rezerwacji | Niski | Recepcja |
| TC-014 | Dodawanie butów | Średni | Buty |
| TC-015 | Wypożyczanie butów | Średni | Buty |
| TC-016 | Zwrot butów | Średni | Buty |
| TC-017 | Wylogowanie | Średni | Autentykacja |
| TC-018 | Responsywność | Niski | UI/UX |
| TC-019 | Wydajność | Niski | Wydajność |
| TC-020 | Bezpieczeństwo | Wysoki | Bezpieczeństwo |

**ŁĄCZNIE: 20 przypadków testowych**

---

## Środowisko Testowe

### Konfiguracja
- **OS**: Windows / Linux / macOS
- **Przeglądarki**: 
  - Chrome (wersja 120+)
  - Firefox (wersja 120+)
  - Edge (wersja 120+)
- **Rozdzielczości**:
  - Desktop: 1920x1080
  - Tablet: 768x1024
  - Mobile: 390x844

### Dane Testowe
```
Klient:
Username: testuser123
Password: Test123!
Email: test@example.com

Recepcjonista:
Username: receptionist
Password: admin123
Email: reception@bouldergym.com
```

---

## Kryteria Akceptacji

### Testy Zakończone Sukcesem Jeśli:
✅ Wszystkie przypadki testowe z priorytetem WYSOKI przeszły  
✅ Min. 80% przypadków ŚREDNICH przeszło  
✅ Nie znaleziono błędów krytycznych (blokerów)  
✅ UI jest responsywne i czytelne  
✅ Dane są zapisywane poprawnie w bazie  

### Błędy Krytyczne (Blokujące wdrożenie):
- Brak możliwości logowania
- Niemożność zakupu karnetu
- Niedziałające potwierdzanie wejść przez recepcjonistę
- Utrata danych użytkownika
- Błędy bezpieczeństwa (dostęp bez autoryzacji)

---

## Harmonogram Testów

1. **Dzień 1**: TC-001 do TC-008 (funkcje klienta)
2. **Dzień 2**: TC-009 do TC-013 (funkcje recepcjonisty)
3. **Dzień 3**: TC-014 do TC-016 (zarządzanie butami)
4. **Dzień 4**: TC-017 do TC-020 (bezpieczeństwo, wydajność, responsywność)

**Szacowany czas**: 4 dni robocze (zakładając 2-3 godziny testów dziennie)

---

## Narzędzia Wspierające

- **DevTools** - inspekcja elementów, tryb mobilny
- **Screenshot/Screen Recorder** - dokumentowanie błędów
- **DB Browser for SQLite** - sprawdzanie bazy danych
- **Postman** (opcjonalnie) - testowanie endpointów API

---

**Autor**: GitHub Copilot  
**Ostatnia aktualizacja**: 27 stycznia 2026
