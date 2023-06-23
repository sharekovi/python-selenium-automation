from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    ORDERS_BTN = (By.ID, 'nav-orders')
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')

    def click_orders(self):
        self.click_orders(*ORDERS_BTN)
