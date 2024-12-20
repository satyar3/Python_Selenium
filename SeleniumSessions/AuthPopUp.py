from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')