from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
# By Xpath
driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-medium a-text-cent']")
driver.find_element(By.XPATH,"//input[@id='ap_email']")
# By ID
driver.find_element(By.ID,'auth-fpp-link-bottom')
driver.find_element(By.ID,'signInSubmit')
driver.find_element(By.ID,'createAccountSubmit')
# By Xpath
driver.find_element(By.XPATH,"//div[@id='legalTextRow']")