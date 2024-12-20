from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://google.com")

try:
    search_bar_input = driver.find_element(By.NAME, 'q')
    search_bar_input = driver.find_element(By.ID, 'q')
    search_bar_input = driver.find_element(By.XPATH, 'q')
    search_bar_input = driver.find_element(By.TAG_NAME, 'q')
    search_bar_input = driver.find_element(By.LINK_TEXT, 'q')
    search_bar_input = driver.find_element(By.PARTIAL_LINK_TEXT, 'q')
    search_bar_input = driver.find_element(By.CSS_SELECTOR, 'q')
    search_bar_input = driver.find_element(By.CLASS_NAME, 'q')
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
search_bar_input.send_keys("Learn Python Selenium")


print(f'Page Title is {driver.title}')

driver.quit()