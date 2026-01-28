from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@when('przechodzę do strony zakupu karnetów')
def step_go_to_buy_pass(context):
    context.driver.get(context.base_url + '/client/buy-pass')
    time.sleep(1)

@when('wybieram karnet "{pass_type}"')
def step_select_pass_type(context, pass_type):
    context.selected_pass = pass_type

@when('klikam przycisk zakupu')
def step_click_purchase_button(context):
    pass_type = getattr(context, 'selected_pass', '10-entry')
    form = context.driver.find_element(By.XPATH, f"//form[input[@name='pass_type' and @value='{pass_type}']]")
    button = form.find_element(By.TAG_NAME, 'button')
    button.click()
    time.sleep(1)

@then('powinienem mieć aktywny karnet "{pass_type}" z {entries} wejściami')
def step_should_have_active_pass(context, pass_type, entries):
    page_source = context.driver.page_source
    assert pass_type in page_source
    assert entries in page_source

@then('powinienem mieć aktywny karnet "{pass_type}"')
def step_should_have_time_pass(context, pass_type):
    page_source = context.driver.page_source
    assert pass_type in page_source

@then('wszystkie przyciski zakupu powinny być wyłączone')
def step_purchase_buttons_disabled(context):
    buttons = context.driver.find_elements(By.XPATH, "//button[contains(text(), 'Buy') or contains(text(), 'Purchase')]")
    for button in buttons:
        assert not button.is_enabled() or 'Already Have a Pass' in button.text

@then('powinienem zobaczyć informację o aktywnym karnecie')
def step_see_active_pass_info(context):
    page_source = context.driver.page_source.lower()
    assert 'active pass' in page_source or 'valid' in page_source
