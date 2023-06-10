from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART = (By.XPATH, "//span[@class='nav-cart-icon nav-sprite']")
PRODUCT_NAME = (By.XPATH, "//span[@class='a-truncate-cut']")


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('//https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name == actual_name, f'Expected {context.product_name} but got {actual_name}'
