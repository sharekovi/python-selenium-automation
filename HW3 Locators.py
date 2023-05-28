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




#By Xpath

driver.find_element(By.XPATH,"//*[@aria-label='Amazon']")
driver.find_element(By.XPATH,"//input[@type='text']")
driver.find_element(By.XPATH,"//h1[text()='Create account']")
driver.find_element(By.XPATH,"//input[@type='email']")
driver.find_element(By.XPATH,"//input[@type='password']")
driver.find_element(By.XPATH,"//input[@name='passwordCheck']")
driver.find_element(By.XPATH,"//a[contains(text(),'Sign in')] ")
driver.find_element(By.XPATH,"//*[@class='a-alert-content']")
driver.find_element(By.XPATH,"//a[contains(text(),'Conditions of Use')]")
driver.find_element(By.XPATH,"//a[contains(text(),'Privacy Notice')] ")

#By ID
driver.find_element(By.ID,'continue')



