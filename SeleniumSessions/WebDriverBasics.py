from selenium import webdriver
from selenium.webdriver.common import by
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
print(f'Page Title {driver.title}')

driver.find_element(by.By.NAME, 'q').send_keys("Learn Selenium with Python")
driver.set_page_load_timeout(20)
driver.implicitly_wait(20)


elements_list = driver.find_elements(by.By.CSS_SELECTOR,'li.sbct.PZPZlf .wM6W7d span')
print(f'Element Size {len(elements_list)}')

for element in elements_list:
    print(f'Element Text is {element.text}')
    if element.text == 'selenium training with python':
        element.click()
        print(f'Element clicked with text {element.text}')
        break


time.sleep(5)
driver.quit()
