from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Global Wait
# Applicable to all the elements

driver.implicitly_wait(10)

driver.get("https://google.com")

# Once one element is loaded in page, then no need to wait for other elements
# In order to nullify -
driver.implicitly_wait(0)
