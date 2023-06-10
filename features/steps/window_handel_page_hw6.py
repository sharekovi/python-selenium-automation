from selenium.webdriver.common.by import By
from behave import given, when, then

from selenium.webdriver.support import expected_conditions as EC

NOTICE_LINK = (By.CSS_SELECTOR, ".help-display-cond.help-display-cond-hidden.help-display-cond-rule-platform"
                                "-DesktopBrowser.help-display-cond-rule-platform-MobileBrowser.help-display-cond-rule"
                                "-platform-PhoneAppAndroid.help-display-cond-rule-platform-TabletAppAndroid["
                                "href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref'
                       '=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:', context.original_window)
    print('All Windows', context.original_window_handels)


@when('Click on Amazon Privacy Notice link')
def click_notice_link(context):
    context.driver.find_element(*NOTICE_LINK).click()


@when('Switch to the new opened window')
def switch_new_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    print('After window opened, all window:', all_windows)
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    context.driver.wait.until(
        EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))


@then('User can close new window')
def close_new_window(context):
    context.driver.close()
    all_windows = context.driver.window_handles
    print('After window closed, all windows:', all_windows)


@then('Return back to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
