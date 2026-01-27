from behave import given, when, then
from selenium.webdriver.common.by import By
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from models import db, Shoes, User
from app import app

@when('przechodzę do strony zarządzania butami')
@given('przechodzę do strony zarządzania butami')
def step_go_to_shoes_management(context):
    context.driver.get(context.base_url + '/receptionist/shoes')
    time.sleep(1)

@when('klikam na formularz dodawania butów')
def step_click_add_shoes_form(context):
    pass

@then('buty rozmiaru "{size}" powinny być widoczne w liście')
def step_shoes_visible_in_list(context, size):
    page_source = context.driver.page_source
    assert size in page_source

@given('w inwentarzu są dostępne buty ID "{shoe_id}"')
@given('że w inwentarzu są dostępne buty ID "{shoe_id}"')
def step_shoes_available_in_inventory(context, shoe_id):
    with app.app_context():
        shoe = Shoes.query.get(int(shoe_id))
        if not shoe:
            shoe = Shoes(id=int(shoe_id), size=9.0, is_available=True)
            db.session.add(shoe)
            db.session.commit()

@given('użytkownik "{username}" istnieje')
@given('że użytkownik "{username}" istnieje')
def step_user_exists_for_shoes(context, username):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username, email=f'{username}@example.com', role='client')
            user.set_password('test123')
            db.session.add(user)
            db.session.commit()

@when('wypełniam formularz wypożyczenia')
def step_fill_rent_form(context):
    for row in context.table:
        if 'shoe_id' in row.headings:
            shoe_id_field = context.driver.find_element(By.NAME, 'shoe_id')
            shoe_id_field.clear()
            shoe_id_field.send_keys(row['shoe_id'])
        if 'username' in row.headings:
            username_field = context.driver.find_element(By.NAME, 'username')
            username_field.clear()
            username_field.send_keys(row['username'])



@then('buty powinny mieć status "{status}"')
def step_shoes_have_status(context, status):
    time.sleep(1)
    context.driver.refresh()
    time.sleep(1)
    page_source = context.driver.page_source
    assert status in page_source

@then('w kolumnie "Rented By" powinienem zobaczyć "{username}"')
def step_see_rented_by_username(context, username):
    page_source = context.driver.page_source
    assert username in page_source

@given('buty ID "{shoe_id}" są wypożyczone przez "{username}"')
@given('że buty ID "{shoe_id}" są wypożyczone przez "{username}"')
def step_shoes_rented_by_user(context, shoe_id, username):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        shoe = Shoes.query.get(int(shoe_id))
        if shoe and user:
            shoe.is_available = False
            shoe.current_renter_id = user.id
            db.session.commit()

@when('wypełniam pole "shoe_id" wartością "{value}" w formularzu zwrotu')
def step_fill_return_shoe_id(context, value):
    form = context.driver.find_element(By.XPATH, "//form[contains(@action, 'shoes') or .//button[contains(text(), 'Return')]]")
    shoe_id_field = form.find_element(By.NAME, 'shoe_id')
    shoe_id_field.clear()
    shoe_id_field.send_keys(value)


