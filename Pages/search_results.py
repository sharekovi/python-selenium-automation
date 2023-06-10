from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def very_search_result(self):
        expected_result = '"table"'
        actual_result = self.driver.find_element(*self.RESULT_TEXT).text
        assert expected_result == actual_result, \
            f'Error ! Expected {expected_result} bot got actual {actual_result}'
