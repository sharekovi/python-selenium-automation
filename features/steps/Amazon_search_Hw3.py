from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon main page')
def open_amazon(context):
   context.driver .get('https://www.amazon.com/')

   @when('Click on orders')
   def click_orders(context):
      context.driver .find_element(By.ID, 'nav-orders').click()

      @then('Verify Sign in page opens')
      def verify_signin_opens(context):

         actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

         assert actual_text == 'Sign in', f'Expected Sign in header but {actual_text}'



         #assert actual_text == context.expected_text, f'Expected {expected_text} but got {actual_text}'

         context.driver.find_element(By.ID, 'ap_email')

         





