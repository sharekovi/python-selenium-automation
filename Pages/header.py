from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep


class Header(Page):
    ORDERS_BTN = (By.ID, 'nav-orders')
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    DEPT_SELECT = (By.CSS_SELECTOR, "#searchDropdownBox")
    ALEXA_SKILLS = (By.CSS_SELECTOR, "a[aria-label='Alexa Skills']")
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_us']")


def select_dept(self):
    dept_select = self.find_element(*self.DEPT_SELECT)
    select = Select(dept_select)
    select.select_by_value('search-alias=alexa-skills')


def verify_dept(self):
    self.wait_elemet_appear(*self.ALEXA_SKILLS)

    def verify_all_departments_options_present(self):
        self.wait_elemet_appear(*self.ALEXA_SKILL)

    def click_orders(self):
        self.click_orders(*ORDERS_BTN)

    def hover_lang(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()
        sleep = (5)

    def verify_spanish_lang_present(self):
        self.wait_elemet_appear(*self.SPANISH_LANG)
