from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@when('przechodzę do dashboardu recepcjonisty')
def step_go_to_receptionist_dashboard(context):
    context.driver.get(context.base_url + '/receptionist/dashboard')
    time.sleep(1)

@when('znajduję rezerwację użytkownika "{username}"')
def step_find_user_reservation(context, username):
    page_source = context.driver.page_source
    assert username in page_source

@then('status rezerwacji powinien zmienić się na "{status}"')
def step_reservation_status_changed(context, status):
    time.sleep(1)
    context.driver.refresh()
    time.sleep(1)
    page_source = context.driver.page_source
    assert status in page_source

@when('przechodzę do strony wyszukiwania rezerwacji')
def step_go_to_search_bookings(context):
    context.driver.get(context.base_url + '/receptionist/search-bookings')
    time.sleep(1)

@when('wpisuję "{text}" w pole wyszukiwania')
def step_enter_search_text(context, text):
    search_field = context.driver.find_element(By.NAME, 'search_term')
    search_field.send_keys(text)

@then('powinienem zobaczyć rezerwacje użytkownika "{username}"')
def step_see_user_reservations(context, username):
    page_source = context.driver.page_source
    assert username in page_source

@when('wybieram sortowanie "{sort_option}"')
def step_select_sorting(context, sort_option):
    select = Select(context.driver.find_element(By.ID, 'sort'))
    select.select_by_visible_text(sort_option)
    time.sleep(2)

@then('rezerwacje ze statusem "{status}" powinny być na górze listy')
def step_pending_reservations_first(context, status):
    rows = context.driver.find_elements(By.XPATH, "//table//tbody//tr")
    if len(rows) > 0:
        first_row = rows[0].text
        assert status in first_row or status.lower() in first_row.lower()
