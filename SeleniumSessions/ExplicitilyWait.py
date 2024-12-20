from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://google.com")
driver.find_element(By.NAME, 'q').send_keys("Learn Selenium with Python")

wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#Alh6id')))
wait.until(ec.alvisibility_of_all_elements_located((By.CSS_SELECTOR, '#Alh6id')))

# Wait until alert is present
wait.until(ec.alert_is_present())

wait.until(ec.url_contains("something"))
# Refer to the screenshot for all the method available in the webdriver wait

elements_list = driver.find_elements(By.CSS_SELECTOR, 'li.sbct.PZPZlf .wM6W7d span')
print(f'Element Size {len(elements_list)}')
