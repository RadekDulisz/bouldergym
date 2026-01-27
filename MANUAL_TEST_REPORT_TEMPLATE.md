# Raport z Testów Manualnych - Boulder Gym Application

## Informacje o Projekcie

| Pole | Wartość |
|------|---------|
| **Nazwa projektu** | Boulder Gym Management System |
| **Wersja aplikacji** | 1.0 |
| **Data testów** | _________________ |
| **Tester** | _________________ |
| **Środowisko testowe** | http://127.0.0.1:5000 |
| **Przeglądarka** | _________________ |
| **System operacyjny** | _________________ |

---

## 1. Streszczenie Wykonawcze

### Cel Testów
```
Celem testów manualnych była weryfikacja poprawności działania aplikacji Boulder Gym 
z perspektywy użytkownika końcowego. Testy obejmowały kluczowe funkcjonalności systemu:
rejestrację, logowanie, zakup karnetów, rezerwacje oraz funkcje recepcjonisty.
```

### Główne Wnioski
```
[Tu wpisz ogólne podsumowanie - czy aplikacja działa dobrze, jakie są główne problemy]

Przykład:
Aplikacja działa stabilnie. Większość funkcjonalności działa zgodnie z oczekiwaniami.
Znaleziono 2 błędy o średnim priorytecie i 1 drobny problem z interfejsem użytkownika.
Zalecane jest wprowadzenie poprawek przed wdrożeniem produkcyjnym.
```

### Status Projektu
- [ ] ✅ **GOTOWE DO WDROŻENIA** - Brak krytycznych błędów
- [ ] ⚠️ **WYMAGA POPRAWEK** - Znaleziono błędy średniego priorytetu
- [ ] ❌ **NIE GOTOWE** - Krytyczne błędy wymagają naprawy

---

## 2. Zakres Testów

### Przetestowane Moduły
- [ ] **Autentykacja** (Rejestracja, Logowanie, Wylogowanie)
- [ ] **Zarządzanie Karnetami** (Zakup, Wyświetlanie)
- [ ] **Rezerwacje** (Tworzenie, Przeglądanie)
- [ ] **Funkcje Recepcjonisty** (Potwierdzanie, Odrzucanie)
- [ ] **Zarządzanie Butami** (Dodawanie, Wypożyczanie, Zwrot)
- [ ] **Bezpieczeństwo** (Kontrola dostępu)
- [ ] **UI/UX** (Responsywność, Użyteczność)

### Przypadki Testowe Wykonane

| ID | Nazwa Przypadku Testowego | Status | Priorytet |
|----|---------------------------|--------|-----------|
| TC-001 | Rejestracja nowego użytkownika | ☐ PASS ☐ FAIL | Wysoki |
| TC-002 | Logowanie klienta | ☐ PASS ☐ FAIL | Wysoki |
| TC-003 | Logowanie z błędnym hasłem | ☐ PASS ☐ FAIL | Średni |
| TC-004 | Zakup karnetu 10-entry | ☐ PASS ☐ FAIL | Wysoki |
| TC-005 | Blokada drugiego karnetu | ☐ PASS ☐ FAIL | Średni |
| TC-006 | Przeglądanie slotów | ☐ PASS ☐ FAIL | Wysoki |
| TC-007 | Rezerwacja slotu | ☐ PASS ☐ FAIL | Wysoki |
| TC-008 | Rezerwacja bez karnetu | ☐ PASS ☐ FAIL | Średni |
| TC-009 | Logowanie recepcjonisty | ☐ PASS ☐ FAIL | Wysoki |
| TC-010 | Potwierdzanie rezerwacji | ☐ PASS ☐ FAIL | Wysoki |
| TC-011 | Odrzucanie rezerwacji | ☐ PASS ☐ FAIL | Średni |
| TC-012 | Wyszukiwanie rezerwacji | ☐ PASS ☐ FAIL | Średni |
| TC-013 | Sortowanie rezerwacji | ☐ PASS ☐ FAIL | Niski |
| TC-014 | Dodawanie butów | ☐ PASS ☐ FAIL | Średni |
| TC-015 | Wypożyczanie butów | ☐ PASS ☐ FAIL | Średni |
| TC-016 | Zwrot butów | ☐ PASS ☐ FAIL | Średni |
| TC-017 | Wylogowanie | ☐ PASS ☐ FAIL | Średni |
| TC-018 | Responsywność | ☐ PASS ☐ FAIL | Niski |
| TC-019 | Wydajność | ☐ PASS ☐ FAIL | Niski |
| TC-020 | Bezpieczeństwo | ☐ PASS ☐ FAIL | Wysoki |

---

## 3. Statystyki Testów

### Ogólne Statystyki

```
Łączna liczba przypadków testowych:        20
Wykonane pomyślnie (PASS):                 ____ ( ___% )
Nieudane (FAIL):                           ____ ( ___% )
Pominięte/Nie przetestowane:               ____ ( ___% )
```

### Znalezione Błędy wg Priorytetu

```
🔴 KRYTYCZNE (Blocker):                    ____
🟠 WYSOKIE (Major):                        ____
🟡 ŚREDNIE (Minor):                        ____
🟢 NISKIE (Trivial):                       ____
─────────────────────────────────────────────
ŁĄCZNIE:                                   ____
```

### Wykres (ASCII)
```
PASS:  ████████████████████ (___%)
FAIL:  ████                  (___%)
SKIP:  ██                    (___%)
```

---

## 4. Szczegółowe Wyniki Testów

### 4.1 Moduł: Autentykacja

#### ✅ TC-001: Rejestracja Nowego Użytkownika
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
[Opisz co zadziałało dobrze lub co poszło nie tak]

Przykład PASS:
Rejestracja działa poprawnie. Użytkownik został utworzony w bazie z zahashowanym hasłem.
Komunikat "Registration successful" wyświetlony. Przekierowanie do /login zadziałało.

Przykład FAIL:
Formularz rejestracji nie waliduje poprawności email. Można wpisać "abc" jako email
i system go zaakceptuje. Brak komunikatu błędu.
```

**Screenshot/Dowód**:
```
[Opcjonalnie: link do screenshota lub opis]
```

---

#### ✅ TC-002: Logowanie Klienta
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-003: Logowanie z Błędnym Hasłem
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

### 4.2 Moduł: Karnety

#### ✅ TC-004: Zakup Karnetu 10-Entry
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-005: Blokada Drugiego Karnetu
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

### 4.3 Moduł: Rezerwacje

#### ✅ TC-006: Przeglądanie Slotów
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-007: Rezerwacja Slotu
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-008: Rezerwacja Bez Karnetu
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

### 4.4 Moduł: Funkcje Recepcjonisty

#### ✅ TC-009: Logowanie Recepcjonisty
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-010: Potwierdzanie Rezerwacji
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-011: Odrzucanie Rezerwacji
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-012: Wyszukiwanie Rezerwacji
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

### 4.5 Moduł: Zarządzanie Butami

#### ✅ TC-014: Dodawanie Butów
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-015: Wypożyczanie Butów
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-016: Zwrot Butów
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

### 4.6 Moduł: Bezpieczeństwo i UI

#### ✅ TC-017: Wylogowanie
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-018: Responsywność
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

#### ✅ TC-020: Bezpieczeństwo (Kontrola Dostępu)
**Status**: ☐ PASS ☐ FAIL  
**Czas wykonania**: ____ minut

**Wynik**:
```
_________________________________________________________________
_________________________________________________________________
```

---

## 5. Raport Błędów

### 🔴 BŁĄD #1

**Priorytet**: ☐ Krytyczny ☐ Wysoki ☐ Średni ☐ Niski  
**Status**: ☐ Otwarty ☐ W naprawie ☐ Naprawiony ☐ Zamknięty

**ID Błędu**: BUG-001  
**Moduł**: _____________________  
**Przypadek testowy**: TC-___

**Krótki opis**:
```
[Jednoliniowy opis problemu]
Przykład: Brak walidacji email w formularzu rejestracji
```

**Szczegółowy opis**:
```
[Dokładny opis co się stało, co powinno się stać]

Przykład:
W formularzu rejestracji pole "Email" przyjmuje dowolny tekst bez sprawdzania 
formatu email (np. "abc", "test@", "@@gmail"). System powinien walidować format
email i wyświetlać komunikat błędu dla niepoprawnych adresów.
```

**Kroki do odtworzenia**:
```
1. Otwórz stronę rejestracji /register
2. Wypełnij pole "Email" wartością "abc"
3. Wypełnij pozostałe pola poprawnymi danymi
4. Kliknij "Register"
5. OCZEKIWANE: Komunikat błędu "Invalid email format"
6. AKTUALNE: Rejestracja się udaje, email zapisany jako "abc"
```

**Oczekiwany rezultat**:
```
System powinien odrzucić rejestrację i wyświetlić komunikat błędu.
```

**Aktualny rezultat**:
```
Rejestracja przebiega pomyślnie mimo niepoprawnego email.
```

**Screenshot/Log**:
```
[Link lub opis]
```

**Wpływ na użytkownika**:
```
Użytkownicy mogą rejestrować się z nieprawidłowymi adresami email, co uniemożliwi
późniejszą komunikację (resetowanie hasła, powiadomienia).
```

**Sugerowane rozwiązanie**:
```
Dodać walidację email po stronie serwera (Flask) oraz klienta (HTML5 type="email")
```

---

### 🟠 BŁĄD #2

**Priorytet**: ☐ Krytyczny ☐ Wysoki ☐ Średni ☐ Niski  
**Status**: ☐ Otwarty ☐ W naprawie ☐ Naprawiony ☐ Zamknięty

**ID Błędu**: BUG-002  
**Moduł**: _____________________  
**Przypadek testowy**: TC-___

**Krótki opis**:
```
_________________________________________________________________
```

**Szczegółowy opis**:
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

**Kroki do odtworzenia**:
```
1. 
2. 
3. 
```

**Oczekiwany rezultat**:
```
_________________________________________________________________
```

**Aktualny rezultat**:
```
_________________________________________________________________
```

---

### 🟡 BŁĄD #3

**Priorytet**: ☐ Krytyczny ☐ Wysoki ☐ Średni ☐ Niski  
**Status**: ☐ Otwarty ☐ W naprawie ☐ Naprawiony ☐ Zamknięty

**ID Błędu**: BUG-003  
**Moduł**: _____________________

**Krótki opis**:
```
_________________________________________________________________
```

**Szczegółowy opis**:
```
_________________________________________________________________
_________________________________________________________________
```

---

## 6. Obserwacje i Uwagi

### 6.1 Pozytywne Aspekty

```
[Co działa dobrze w aplikacji]

Przykład:
✅ Interfejs użytkownika jest intuicyjny i łatwy w nawigacji
✅ Komunikaty flash są widoczne i zrozumiałe
✅ Logowanie i rejestracja działają szybko (< 1 sekunda)
✅ Dashboard recepcjonisty jest czytelny i funkcjonalny
✅ Baza danych zachowuje integralność danych
```

---

### 6.2 Obszary Wymagające Uwagi

```
[Co można poprawić]

Przykład:
⚠️ Brak walidacji niektórych pól formularza
⚠️ Responsywność na urządzeniach mobilnych wymaga poprawy
⚠️ Brak komunikatów ładowania przy długich operacjach
⚠️ Niektóre przyciski są zbyt małe na ekranach dotykowych
```

---

### 6.3 Sugestie Ulepszeń

```
[Pomysły na nowe funkcje lub usprawnienia]

Przykład:
💡 Dodać możliwość resetowania hasła przez email
💡 Implementować paginację dla długich list rezerwacji
💡 Dodać filtrowanie rezerwacji po dacie
💡 Możliwość edycji profilu użytkownika
💡 Dashboard z wykresami (statystyki wejść, popularność slotów)
```

---

## 7. Rekomendacje

### 7.1 Krytyczne Akcje (Przed Wdrożeniem)

```
☐ Naprawić wszystkie błędy KRYTYCZNE
☐ Naprawić błędy WYSOKIE
☐ Przeprowadzić ponowne testy po naprawach
☐ Sprawdzić bezpieczeństwo (SQL injection, XSS)
```

---

### 7.2 Zalecenia Długoterminowe

```
☐ Dodać automatyczne testy regresji
☐ Implementować monitoring błędów (Sentry, Rollbar)
☐ Przygotować dokumentację dla użytkowników końcowych
☐ Przeprowadzić testy wydajnościowe pod obciążeniem
☐ Rozważyć testy A/B dla interfejsu użytkownika
```

---

## 8. Wnioski Końcowe

### Podsumowanie
```
[Ogólne podsumowanie stanu aplikacji]

Przykład:
Aplikacja Boulder Gym Management System została przetestowana w zakresie kluczowych
funkcjonalności. Większość funkcji działa zgodnie z wymaganiami. Znaleziono [X] błędów,
z czego [Y] wymaga natychmiastowej naprawy przed wdrożeniem produkcyjnym.

Interfejs użytkownika jest intuicyjny, ale wymaga drobnych poprawek w responsywności.
Bezpieczeństwo aplikacji jest na zadowalającym poziomie, choć zaleca się audyt
bezpieczeństwa przez specjalistę.

Po wprowadzeniu zalecanych poprawek aplikacja będzie gotowa do wdrożenia.
```

---

### Decyzja o Wdrożeniu

**Rekomendacja testera**:

- [ ] ✅ **ZALECAM WDROŻENIE** - Aplikacja spełnia wymagania, brak krytycznych błędów
- [ ] ⚠️ **WARUNKOWO ZALECAM** - Możliwe wdrożenie po naprawie błędów średniego priorytetu
- [ ] ❌ **NIE ZALECAM** - Krytyczne błędy wymagają naprawy przed wdrożeniem

**Uzasadnienie**:
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

---

## 9. Załączniki

### Logi i Screenshoty
```
[Lista załączonych plików]

- screenshot_login_error.png
- log_database_query.txt
- video_booking_flow.mp4
```

### Dane Testowe Użyte
```
Klient testowy:
  Username: testuser123
  Password: Test123!
  Email: test@example.com

Recepcjonista:
  Username: receptionist
  Password: admin123
```

---

## 10. Podpisy

| Rola | Imię i Nazwisko | Data | Podpis |
|------|-----------------|------|--------|
| **Tester** | _________________ | ____/____/____ | ____________ |
| **Lead QA** | _________________ | ____/____/____ | ____________ |
| **Project Manager** | _________________ | ____/____/____ | ____________ |

---

**Koniec raportu**

---

## Informacje o Dokumencie

- **Wersja raportu**: 1.0
- **Data utworzenia**: 27 stycznia 2026
- **Autor szablonu**: GitHub Copilot
- **Ostatnia modyfikacja**: _________________
