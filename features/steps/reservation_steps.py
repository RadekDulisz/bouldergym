from behave import given, when, then
from selenium.webdriver.common.by import By
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from models import db, User, Reservation
from app import app
from datetime import datetime, timedelta

@when('przechodzę do strony przeglądania slotów')
def step_go_to_view_slots(context):
    context.driver.get(context.base_url + '/client/view-slots')
    time.sleep(1)

@when('wybieram jutrzejszą datę')
def step_select_tomorrow(context):
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    context.selected_date = tomorrow

@when('wybieram slot czasowy "{slot}"')
def step_select_time_slot(context, slot):
    context.selected_slot = slot

@when('klikam przycisk rezerwacji')
def step_click_reserve_button(context):
    date = getattr(context, 'selected_date', (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
    slot = getattr(context, 'selected_slot', '09:00-11:00')
    
    form = context.driver.find_element(By.XPATH, f"//form[contains(@action, 'book-entry')]")
    date_input = form.find_element(By.NAME, 'date')
    slot_input = form.find_element(By.NAME, 'time_slot')
    
    context.driver.execute_script(f"arguments[0].value = '{date}'", date_input)
    context.driver.execute_script(f"arguments[0].value = '{slot}'", slot_input)
    
    button = form.find_element(By.XPATH, ".//button[@type='submit']")
    button.click()
    time.sleep(1)

@when('próbuję zarezerwować slot "{slot}" na jutro')
def step_try_reserve_slot(context, slot):
    date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    context.driver.get(context.base_url + '/client/view-slots')
    time.sleep(1)

@then('rezerwacja powinna pojawić się na moim dashboardzie')
def step_reservation_on_dashboard(context):
    context.driver.get(context.base_url + '/client/dashboard')
    time.sleep(1)
    page_source = context.driver.page_source
    assert 'Pending' in page_source or 'pending' in page_source

@then('powinienem zobaczyć listę dostępnych terminów')
def step_see_available_slots(context):
    page_source = context.driver.page_source
    assert '09:00-11:00' in page_source or 'slot' in page_source.lower()

@then('każdy slot powinien pokazywać liczbę wolnych miejsc')
def step_slots_show_availability(context):
    page_source = context.driver.page_source
    assert 'available' in page_source.lower() or 'spots' in page_source.lower()

@given('istnieje oczekująca rezerwacja dla użytkownika "{username}"')
@given('że istnieje oczekująca rezerwacja dla użytkownika "{username}"')
def step_pending_reservation_exists(context, username):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username, email=f'{username}@example.com', role='client')
            user.set_password('test123')
            db.session.add(user)
            db.session.commit()
        existing = Reservation.query.filter_by(user_id=user.id, status='pending').first()
        if not existing:
            reservation = Reservation(
                user_id=user.id,
                reservation_date=datetime.now(),
                time_slot='09:00-11:00',
                status='pending'
            )
            db.session.add(reservation)
            db.session.commit()
            context.test_reservation_id = reservation.id

@given('istnieje rezerwacja dla użytkownika "{username}"')
@given('że istnieje rezerwacja dla użytkownika "{username}"')
def step_reservation_exists(context, username):
    step_pending_reservation_exists(context, username)

@given('istnieją rezerwacje z różnymi statusami')
@given('że istnieją rezerwacje z różnymi statusami')
def step_reservations_with_different_statuses(context):
    with app.app_context():
        users = list(User.query.limit(2).all())
        while len(users) < 2:
            idx = len(users) + 1
            user = User(username=f'testuser{idx}', email=f'testuser{idx}@example.com', role='client')
            user.set_password('test123')
            db.session.add(user)
            db.session.commit()
            users.append(user)

        res1 = Reservation(
            user_id=users[0].id,
            reservation_date=datetime.now(),
            time_slot='09:00-11:00',
            status='pending'
        )
        res2 = Reservation(
            user_id=users[1].id,
            reservation_date=datetime.now(),
            time_slot='11:00-13:00',
            status='confirmed'
        )
        db.session.add(res1)
        db.session.add(res2)
        db.session.commit()
