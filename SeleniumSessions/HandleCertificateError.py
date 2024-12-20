from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://expired.badssl.com")
print(driver.find_element(By.TAG_NAME,'h1').text)