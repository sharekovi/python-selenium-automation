from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL = (By.ID, 'ap_email')

    def verify_sign_opens(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
        self.verify_sign_opens('sign in',*SignInPage)
        self.find_element(*self.EMail)
