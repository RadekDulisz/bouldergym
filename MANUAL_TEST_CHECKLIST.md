# Checklista Testów Manualnych - Boulder Gym

## Informacje o Teście
- **Data testów**: _______________
- **Tester**: _______________
- **Wersja aplikacji**: 1.0
- **Środowisko**: http://127.0.0.1:5000
- **Przeglądarka**: _______________

---

## 🔍 Przygotowanie do Testów

- [ ] Aplikacja uruchomiona (Flask server działa)
- [ ] Baza danych przygotowana (czysta lub z danymi testowymi)
- [ ] Przeglądarka zaktualizowana do najnowszej wersji
- [ ] DevTools dostępne (F12)
- [ ] Notatnik/dokument do zapisywania błędów

---

## 📝 MODUŁ 1: Rejestracja i Autentykacja

### ✅ Rejestracja Nowego Użytkownika
- [ ] Formularz rejestracji się otwiera
- [ ] Wszystkie pola są widoczne (username, email, password, role)
- [ ] Można wypełnić wszystkie pola
- [ ] Hasło jest maskowane (*)
- [ ] Po wysłaniu formularz przekierowuje do /login
- [ ] Komunikat "Registration successful" jest widoczny
- [ ] Nowy użytkownik jest w bazie danych
- [ ] Hasło jest zahashowane (nie w postaci czystego tekstu)

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Logowanie Klienta
- [ ] Formularz logowania się wyświetla
- [ ] Pola username i password działają
- [ ] Przycisk "Login" jest klikalny
- [ ] Po poprawnym logowaniu przekierowanie do /client/dashboard
- [ ] Komunikat powitalny "Welcome back, [username]"
- [ ] Dashboard klienta wyświetla się poprawnie
- [ ] Przyciski nawigacyjne są widoczne (Buy Pass, View Slots, Logout)

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Logowanie z Błędnymi Danymi
- [ ] Błędne hasło: komunikat "Invalid username or password"
- [ ] Nieistniejący username: odpowiedni komunikat błędu
- [ ] Pozostanie na stronie /login po błędzie
- [ ] Pola formularza są wyczyszczone lub zachowują username

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Logowanie Recepcjonisty
- [ ] Możliwość zalogowania jako receptionist
- [ ] Przekierowanie do /receptionist/dashboard
- [ ] Dashboard recepcjonisty wyświetla właściwe elementy
- [ ] Tabela rezerwacji jest widoczna
- [ ] Przyciski Confirm/Decline działają

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 📝 MODUŁ 2: Karnety (Passes)

### ✅ Zakup Karnetu 10-Wejściowego
- [ ] Strona /client/buy-pass się otwiera
- [ ] Sekcja "10-Entry Pass" jest widoczna
- [ ] Cena (100 PLN) jest wyświetlona
- [ ] Przycisk "Get Started" działa
- [ ] Komunikat "Successfully purchased 10-entry pass!"
- [ ] Dashboard pokazuje aktywny karnet
- [ ] Liczba wejść: 10
- [ ] Płatność zapisana w bazie (100 PLN)

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Zakup Karnetu 30-Dniowego
- [ ] Sekcja "30-Day Pass" jest widoczna
- [ ] Cena (150 PLN) jest wyświetlona
- [ ] Przycisk zakupu działa
- [ ] Komunikat sukcesu
- [ ] Karnet w bazie: typ 30-day, data ważności ustawiona
- [ ] Dashboard pokazuje datę wygaśnięcia

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Blokada Zakupu Drugiego Karnetu
- [ ] Użytkownik ma już aktywny karnet
- [ ] Próba zakupu kolejnego
- [ ] Komunikat "You already have an active pass"
- [ ] Drugi karnet NIE został utworzony w bazie
- [ ] Pierwszy karnet pozostaje aktywny

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 📝 MODUŁ 3: Rezerwacje (Reservations)

### ✅ Przeglądanie Dostępnych Slotów
- [ ] Strona /client/view-slots się otwiera
- [ ] Tabela slotów jest widoczna
- [ ] Kolumny: Data, Godzina, Max Capacity
- [ ] Przyciski "Book" przy każdym slocie
- [ ] Dane są aktualne i poprawne

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Rezerwacja Slotu (z Karnetem)
- [ ] Klient ma aktywny karnet
- [ ] Kliknięcie "Book" przy slocie
- [ ] Formularz potwierdzenia rezerwacji (jeśli istnieje)
- [ ] Przycisk "Confirm Booking"
- [ ] Komunikat "Booking successful!" lub podobny
- [ ] Rezerwacja pojawia się w "My Reservations"
- [ ] Status rezerwacji: "Pending"
- [ ] Rezerwacja zapisana w bazie
- [ ] Wejścia na karnecie JESZCZE nie zostały odjęte

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Próba Rezerwacji Bez Karnetu
- [ ] Użytkownik NIE ma aktywnego karnetu
- [ ] Próba zarezerwowania slotu
- [ ] Komunikat błędu "You need a valid pass to book an entry"
- [ ] Rezerwacja NIE została utworzona
- [ ] Użytkownik pozostaje na tej samej lub podobnej stronie

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 📝 MODUŁ 4: Funkcje Recepcjonisty

### ✅ Potwierdzanie Rezerwacji (Confirm)
- [ ] Recepcjonista zalogowany
- [ ] Dashboard pokazuje rezerwacje "Pending"
- [ ] Przycisk "Confirm" przy rezerwacji
- [ ] Kliknięcie przycisku
- [ ] Komunikat "Entry confirmed successfully!"
- [ ] Status rezerwacji zmieniony na "Confirmed"
- [ ] Kolumna "Confirmed By" zawiera ID recepcjonisty
- [ ] Wejścia klienta zmniejszone o 1
- [ ] Jeśli 10-entry: entries_remaining - 1
- [ ] Baza danych zaktualizowana poprawnie

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Odrzucanie Rezerwacji (Decline)
- [ ] Rezerwacja "Pending" jest widoczna
- [ ] Przycisk "Decline" działa
- [ ] Komunikat "Reservation declined"
- [ ] Status zmieniony na "Declined"
- [ ] Wejścia klienta NIE zostały odjęte
- [ ] Rezerwacja pozostaje w systemie (nie jest usunięta)

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Wyszukiwanie Rezerwacji po Username
- [ ] Pole wyszukiwania "Search by username" jest widoczne
- [ ] Wpisanie nazwy użytkownika (np. testuser123)
- [ ] Przycisk "Search" działa
- [ ] Lista rezerwacji filtrowana poprawnie
- [ ] Wyświetlane tylko rezerwacje dla tego użytkownika
- [ ] Wyczyszczenie pola pokazuje ponownie wszystkie

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Sortowanie Rezerwacji (Pending First)
- [ ] Opcja sortowania jest dostępna
- [ ] Wybór "Pending First" lub podobny
- [ ] Rezerwacje "Pending" wyświetlane na górze listy
- [ ] Pozostałe rezerwacje poniżej
- [ ] Sortowanie działa poprawnie

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 📝 MODUŁ 5: Zarządzanie Butami (Shoes)

### ✅ Dodawanie Butów do Inwentarza
- [ ] Strona /receptionist/manage-shoes się otwiera
- [ ] Formularz dodawania butów jest widoczny
- [ ] Pole "Size" przyjmuje wartość (np. 42)
- [ ] Przycisk "Add Shoes" działa
- [ ] Komunikat "Shoes added successfully"
- [ ] Nowe buty w tabeli inwentarza
- [ ] Status: "Available"
- [ ] Dane zapisane w bazie

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Wypożyczanie Butów Klientowi
- [ ] Buty ze statusem "Available" są widoczne
- [ ] Pole "Username" przy butach do wypożyczenia
- [ ] Wpisanie nazwy użytkownika
- [ ] Przycisk "Rent" działa
- [ ] Komunikat "Shoes rented successfully"
- [ ] Status butów zmieniony na "Rented"
- [ ] Kolumna "Rented To" wypełniona nazwą użytkownika
- [ ] Baza danych zaktualizowana

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Zwrot Butów
- [ ] Buty "Rented" są widoczne
- [ ] Przycisk "Return" przy wypożyczonych butach
- [ ] Kliknięcie przycisku
- [ ] Komunikat "Shoes returned successfully"
- [ ] Status zmieniony na "Available"
- [ ] Kolumna "Rented To" wyczyszczona (NULL)

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 📝 MODUŁ 6: Bezpieczeństwo i Autoryzacja

### ✅ Kontrola Dostępu
- [ ] Klient NIE może wejść na /receptionist/dashboard
- [ ] Przekierowanie do /login lub błąd 403
- [ ] Recepcjonista NIE może kupić karnetu (/client/buy-pass)
- [ ] Niezalogowany użytkownik przekierowany do /login
- [ ] Próba dostępu przez URL blokowana

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Sesje i Wylogowanie
- [ ] Przycisk "Logout" jest widoczny
- [ ] Kliknięcie wylogowuje użytkownika
- [ ] Przekierowanie do /login
- [ ] Próba wejścia na chronioną stronę wymaga ponownego logowania
- [ ] Sesja jest prawidłowo zakończona

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 📝 MODUŁ 7: UI/UX i Responsywność

### ✅ Wygląd i Użyteczność
- [ ] Strony ładują się w rozsądnym czasie (< 3 sekundy)
- [ ] Wszystkie przyciski są klikalne i wyraźne
- [ ] Formularze są czytelne i łatwe w użyciu
- [ ] Komunikaty flash są widoczne i znikają po czasie
- [ ] Kolory i czcionki są spójne
- [ ] Brak błędów 404 na linkach

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

### ✅ Responsywność (DevTools - F12)
- [ ] Otwórz DevTools, włącz tryb urządzenia mobilnego
- [ ] iPhone 12 Pro (390x844):
  - [ ] Formularz logowania działa
  - [ ] Dashboard jest czytelny
  - [ ] Tabele są przewijalne
  - [ ] Przyciski są dostępne
- [ ] iPad (768x1024):
  - [ ] Układ strony poprawny
  - [ ] Wszystkie funkcje działają
- [ ] Desktop 1920x1080:
  - [ ] Pełna funkcjonalność
  - [ ] Optymalne wykorzystanie przestrzeni

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 📝 MODUŁ 8: Integralność Danych

### ✅ Weryfikacja Bazy Danych
- [ ] Otwórz bazę SQLite (DB Browser lub podobne)
- [ ] Sprawdź tabelę `user`: hasła są zahashowane
- [ ] Sprawdź tabelę `pass`: daty są poprawne
- [ ] Sprawdź tabelę `reservation`: statusy są prawidłowe
- [ ] Sprawdź tabelę `payment`: kwoty są poprawne
- [ ] Brak duplikatów, NULL gdzie nie powinno być

**Notatki/Błędy:**
```
_________________________________________________________________
_________________________________________________________________
```

---

## 📊 Podsumowanie Testów

### Statystyki
- **Łączna liczba testowanych punktów**: ________
- **Zaliczone (✅)**: ________
- **Niezaliczone (❌)**: ________
- **Nie przetestowane (⚠️)**: ________
- **Procent sukcesu**: ________%

### Znalezione Błędy

#### Błąd #1
- **Priorytet**: [ ] Krytyczny [ ] Wysoki [ ] Średni [ ] Niski
- **Moduł**: _____________________
- **Opis**: 
```
_________________________________________________________________
_________________________________________________________________
```
- **Kroki do odtworzenia**:
```
1. 
2. 
3. 
```
- **Screenshot/Log**: _____________________

---

#### Błąd #2
- **Priorytet**: [ ] Krytyczny [ ] Wysoki [ ] Średni [ ] Niski
- **Moduł**: _____________________
- **Opis**: 
```
_________________________________________________________________
_________________________________________________________________
```
- **Kroki do odtworzenia**:
```
1. 
2. 
3. 
```

---

#### Błąd #3
- **Priorytet**: [ ] Krytyczny [ ] Wysoki [ ] Średni [ ] Niski
- **Moduł**: _____________________
- **Opis**: 
```
_________________________________________________________________
_________________________________________________________________
```

---

### Rekomendacje

**Co działa dobrze:**
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

**Co wymaga poprawy:**
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

**Sugestie dla programistów:**
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

---

## ✅ Decyzja Końcowa

- [ ] **ZALICZONE** - Aplikacja gotowa do wdrożenia
- [ ] **WARUNKOWO ZALICZONE** - Wymaga drobnych poprawek
- [ ] **NIEZALICZONE** - Krytyczne błędy, wymaga przeróbek

---

**Tester**: ___________________  
**Data**: ___________________  
**Podpis**: ___________________
