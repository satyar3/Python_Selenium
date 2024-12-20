from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

# There should be an attribute type="file"
driver.find_element(By.NAME, 'upfile').send_keys('path_to_file')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
