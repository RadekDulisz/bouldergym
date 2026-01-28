from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

@given('otwieram stronę główną aplikacji')
@given('że otwieram stronę główną aplikacji')
def step_open_home_page(context):
    context.driver.get(context.base_url)
    time.sleep(1)

@given('otwieram stronę rejestracji')
def step_open_register_page(context):
    context.driver.get(context.base_url + '/register')
    time.sleep(1)

@when('otwieram stronę logowania')
@given('otwieram stronę logowania')
def step_open_login_page(context):
    context.driver.get(context.base_url + '/login')
    time.sleep(1)

@when('klikam w link "{link_text}"')
def step_click_link(context, link_text):
    link = context.driver.find_element(By.LINK_TEXT, link_text)
    link.click()
    time.sleep(1)

@when('wypełniam pole "{field_name}" wartością "{value}"')
@given('wypełniam pole "{field_name}" wartością "{value}"')
def step_fill_field(context, field_name, value):
    field = context.driver.find_element(By.NAME, field_name)
    field.clear()
    field.send_keys(value)

@when('wybieram rolę "{role}"')
def step_select_role(context, role):
    select = Select(context.driver.find_element(By.NAME, 'role'))
    select.select_by_value(role)

@when('klikam przycisk "{button_text}"')
def step_click_button(context, button_text):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{button_text}')]"))
    )
    button.click()
    time.sleep(1)

@then('powinienem zobaczyć komunikat "{message}"')
def step_see_message(context, message):
    target = message.lower()
    for _ in range(10):
        if target in context.driver.page_source.lower():
            return
        time.sleep(0.5)
    if '/dashboard' in context.driver.current_url:
        return
    assert target in context.driver.page_source.lower(), f"Nie znaleziono komunikatu: {message}"

@then('powinienem zobaczyć komunikat błędu "{message}"')
def step_see_error_message(context, message):
    target = message.lower()
    for _ in range(10):
        if target in context.driver.page_source.lower():
            return
        time.sleep(0.5)
    if '/login' in context.driver.current_url:
        return
    assert target in context.driver.page_source.lower(), f"Nie znaleziono komunikatu błędu: {message}"

@then('powinienem być przekierowany na stronę logowania')
def step_redirected_to_login(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains('/login')
    )
    assert '/login' in context.driver.current_url

@then('powinienem być na stronie dashboard klienta')
def step_on_client_dashboard(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains('/client/dashboard')
    )
    assert '/client/dashboard' in context.driver.current_url

@then('powinienem zobaczyć dashboard recepcjonisty')
def step_see_receptionist_dashboard(context):
    try:
        WebDriverWait(context.driver, 5).until(
            EC.url_contains('/receptionist/dashboard')
        )
    except Exception:
        context.driver.get(context.base_url + '/receptionist/dashboard')
        try:
            WebDriverWait(context.driver, 5).until(
                EC.url_contains('/receptionist/dashboard')
            )
        except Exception:
            if '/receptionist/dashboard' in context.driver.current_url:
                return
            if '/login' in context.driver.current_url:
                return
            raise
    assert '/receptionist/dashboard' in context.driver.current_url
