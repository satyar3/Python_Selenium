from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://google.com")

driver.back()
driver.forward()

cookies = driver.get_cookies()
print(f'All Cookies : {cookies}')
print('Cookie length --> '+len(cookies))

for cookie in cookies:
    print("Cookie --> "+cookie)
    print()