from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon main page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when(' Select department alexa skills')
def select_dept(context):
    context.app.header.select_dept()


@when(' Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Search for echo dot')
def search_for_echo_dot(context):
    context.app.verify_all_departments_options()


@then('verify correct department shown')
def verify_department_shown(context):
    context.app.verify_dept()


@then('Verify Spanish option present')
def verify_spanish_lang_present(context):
    context.app.header.verify_spanish_lang_present()
