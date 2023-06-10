from pages.base_page import Page

class Header(Page):
    ORDERS_BTN = (By.ID, 'nav-orders')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def search_for_product(self):
        self.input_('table',*self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)





