from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.set_page_load_timeout(10)

driver.get('http://www.londonfreelance.org/courses/frames/index.html')

frame_element = driver.find_element(By.NAME, 'main')

driver.switch_to.frame(frame_element)

# Switch to 3rd Frame or Index 2
driver.switch_to.frame(2)

# Switch to a frame having name = main
driver.switch_to.frame('main')

headerValue = driver.find_element(By.CSS_SELECTOR, 'body > h2').text
print(f'Header Value {headerValue}')

# Driver will be back to the main page
driver.switch_to.default_content()

# Driver till be back to only the parent frame
driver.switch_to.parent_frame()

driver.quit()
