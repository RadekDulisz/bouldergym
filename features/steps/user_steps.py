from behave import given, when, then
from selenium.webdriver.common.by import By
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from models import db, User, Pass
from app import app
from datetime import datetime, timedelta

@given('użytkownik "{username}" już istnieje')
@given('że użytkownik "{username}" już istnieje')
def step_user_exists(context, username):
    with app.app_context():
        existing_user = User.query.filter_by(username=username).first()
        if not existing_user:
            user = User(username=username, email=f'{username}@example.com', role='client')
            user.set_password('test123')
            db.session.add(user)
            db.session.commit()

@given('użytkownik klienta istnieje z danymi')
@given('że użytkownik klienta istnieje z danymi')
def step_client_user_exists_with_data(context):
    username = None
    password = None
    if context.table and len(context.table.rows) >= 2:
        username = context.table.rows[0].cells[-1].strip()
        password = context.table.rows[1].cells[-1].strip()
    else:
        for row in context.table:
            cells = row.cells
            if len(cells) >= 2 and cells[0].strip().lower() == 'username':
                username = cells[1].strip()
            if len(cells) >= 2 and cells[0].strip().lower() == 'password':
                password = cells[1].strip()
    
    if not username:
        username = 'testclient'
    if not password:
        password = 'test123'

    with app.app_context():
        existing_user = User.query.filter_by(username=username).first()
        if not existing_user:
            user = User(username=username, email=f'{username}@example.com', role='client')
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
        context.test_username = username
        context.test_password = password

@given('użytkownik recepcjonisty istnieje z danymi')
@given('że użytkownik recepcjonisty istnieje z danymi')
def step_receptionist_user_exists_with_data(context):
    username = None
    password = None
    if context.table and len(context.table.rows) >= 2:
        username = context.table.rows[0].cells[-1].strip()
        password = context.table.rows[1].cells[-1].strip()
    else:
        for row in context.table:
            cells = row.cells
            if len(cells) >= 2 and cells[0].strip().lower() == 'username':
                username = cells[1].strip()
            if len(cells) >= 2 and cells[0].strip().lower() == 'password':
                password = cells[1].strip()
    
    if not username:
        username = 'receptionist'
    if not password:
        password = 'admin123'

    with app.app_context():
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            existing_user.role = 'receptionist'
            db.session.commit()
        else:
            user = User(username=username, email=f'{username}@example.com', role='receptionist')
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

@given('jestem zalogowany jako klient "{username}"')
@given('że jestem zalogowany jako klient "{username}"')
def step_logged_in_as_client(context, username):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username, email=f'{username}@example.com', role='client')
            user.set_password('test123')
            db.session.add(user)
            db.session.commit()
    
    context.driver.get(context.base_url + '/login')
    context.driver.find_element(By.NAME, 'username').send_keys(username)
    context.driver.find_element(By.NAME, 'password').send_keys('test123')
    context.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    context.current_user = username

@given('jestem zalogowany jako recepcjonista')
@given('że jestem zalogowany jako recepcjonista')
def step_logged_in_as_receptionist(context):
    with app.app_context():
        user = User.query.filter_by(username='receptionist').first()
        if not user:
            user = User(username='receptionist', email='receptionist@example.com', role='receptionist')
            user.set_password('admin123')
            db.session.add(user)
            db.session.commit()
        else:
            user.role = 'receptionist'
            user.set_password('admin123')
            db.session.commit()

    context.driver.get(context.base_url + '/login')
    context.driver.find_element(By.NAME, 'username').send_keys('receptionist')
    context.driver.find_element(By.NAME, 'password').send_keys('admin123')
    context.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

@given('mam aktywny karnet z {entries} wejściami')
@given('że mam aktywny karnet z {entries} wejściami')
def step_have_active_pass(context, entries):
    username = getattr(context, 'current_user', 'testclient')
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=int(entries),
                entries_remaining=int(entries),
                price=100.0,
                is_active=True
            )
            db.session.add(pass_obj)
            db.session.commit()

@given('nie mam aktywnego karnetu')
@given('że nie mam aktywnego karnetu')
def step_no_active_pass(context):
    username = getattr(context, 'current_user', 'testclient')
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            passes = Pass.query.filter_by(user_id=user.id, is_active=True).all()
            for p in passes:
                p.is_active = False
            db.session.commit()

@given('mam już aktywny karnet')
@given('że mam już aktywny karnet')
def step_already_have_pass(context):
    username = getattr(context, 'current_user', 'testclient')
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            existing_pass = Pass.query.filter_by(user_id=user.id, is_active=True).first()
            if not existing_pass:
                pass_obj = Pass(
                    user_id=user.id,
                    pass_type='10-entry',
                    entries_total=10,
                    entries_remaining=5,
                    price=100.0,
                    is_active=True
                )
                db.session.add(pass_obj)
                db.session.commit()
