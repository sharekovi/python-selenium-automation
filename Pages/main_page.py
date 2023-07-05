from Pages.base_page import Page


class MainPage(Page):

    def open_main_page(context):
        context.driver.get('https://www.amazon.com/')
        context.app.main_page_open_main_page()

    def click_orders(context):
        context.app.header.click_orders()
