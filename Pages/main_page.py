# from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):

    def open_main_page(self):
        self.open_url('https://www.amazon.com/')



# ORDERS_BTN = (By.ID, 'nav-orders')
# SEARCH_BTN = (By.ID, 'nav-search-submit-button')

# def open_main_page(self):
# self.open_url('https://www.amazon.com/')

# def find_elements(self, *locator):
# return self.driver.find_elements(*self.ORDERS_BTN)

# def click(self, *locator):
# self.driver.find_element(*self.SEARCH_BTN).click()

# ORDERS_BTN = (By.ID, 'nav-orders')
# SEARCH_BTN = (By.ID, 'nav-search-submit-button')
