from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


