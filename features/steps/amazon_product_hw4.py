from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

RESULT_TEXT = (By.XPATH,"//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE =(By.XPATH,'//span[normalize-space()=AmazonFresh Hazelnut Flavored Coffee, Ground, Medium Roast, 12 Ounce]')
PRODUCT_NAME = (By.ID,'productTitle')
ADD_TO_CART_BTN =(By.ID,'add-to-cart-button')
CART = (By.ID,'nav-cart-count')
SEARCH_FIELD= (By.ID,'twotabsearchtextbox')
SEARCH_BTN= (By.ID,'nav-search-submit-button')

@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

    @when('Search for {search_word}')
    def Search_amazon(context,search_word):
       context. driver.find_element (*SEARCH_FIELD).send_keys(search_word)
       context.driver.find_element (*SEARCH_BTN).click()

       @then('Verify search result shown for {expected_result}')
       def verify_search_result(context,expected_result):

           actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

           assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'

           @when('Click on the first product')
           def click_first_product(context):
               context.driver.find_element(*PRODUCT_PRICE).click()

                @when('Store product name')
                def get_product_name(context):
                  context.product_name =  context.driver.find_element(*PRODUCT_NAME).text
                   print(f'Current product: {context.product_name}')
                    @when('click on Add to cart button')
                    def click_add_to_cart(context):
                        context.driver.find_element()
                        @when('Open cart page')
                        def open_cart_page(context):
                            context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
                            @then(f'Verify cart has{expected_count}item(s)')
                            def verify_cart_count(context,expected_count):
                                actual_text = context.driver.find_element(*CART).text
                                assert expected_count == actual_text,f'{expected_count},but got{actual_text}'
                                @then('Verify cart has correct product')
                                def verify_product_name(context):
                                    actual_name = context.driver.find_element(*PRODUCT_NAME).text
                                    assert context.product_name[30] in actual_name,f'Expected{context.product_name}but got {actual_name}'




