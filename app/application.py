from pages.header import Header
from pages.main_page import MainPage
from pages.search_results import SearchResultsPage


class Application:

    def __int__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)

        app = Application()
        app.header.search_for_product()
        app.main_page.open_main_page()
        app.search_results_page.verify_search_results()
