from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID,'twotabsearchtextbox')
SEARCH_BTN = (By.ID,'nav-search-submit-button')


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

    @when('{search_word}')
    def search_amazon(context,search_word):
        context.driver.find_element(*SEARCH_FIELD).send_key(search_word)
        context.driver.find_element(*SEARCH_BTN).click()


