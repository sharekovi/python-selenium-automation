
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

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH,"//a[text()='Best Sellers']").click()

expected_text = 'Best Sellers'


#Find Elements

driver.find_element((By.XPATH,"//a[@href='/Best-Sellers/zgbs/ref=zg_bs_tab']"))
driver.find_element(By.CSS_SELECTOR,"a[href='/gp/new-releases/ref=zg_bs_tab']")
driver.find_element(By.XPATH,"//a[@href='/gp/movers-and-shakers/ref=zg_bs_tab']")
driver.find_element(By.XPATH,"//a[normalize-space()='Most Wished For']")
driver.find_element(By.XPATH,"//a[normalize-space()='Gift Ideas']")





