from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "variation_color_name")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")



@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

    @then('Verify user can click through colors')
    def verify_can_click_colors(context):
        expected_colors = ['black', 'Blue,Over Dye', 'Bright White', 'Dark Blue Vintage','dark Indigo/Rinsed','Dark Khaki Brown']
        actual_colors = []

        colors = context.driver.find_elements(*COLOR_OPTIONS)

        for color in colors[:6]:

            color.click()
            current_color = context.driver.find_element(*CURRENT_COLOR).text
            actual_colors += [current_color]

        assert expected_colors == actual_colors, \
            f'Expected colors {expected_colors} did not match actual {actual_colors}'


