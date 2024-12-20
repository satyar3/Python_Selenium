from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://google.com")


links_list = driver.find_elements(By.TAG_NAME,'a')

for link in links_list:
    print(f'Link is : {link.get_attribute("href")}')