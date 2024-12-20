from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://google.com")
element = driver.find_element(By.NAME, 'q')

driver.execute_script('arguments[0].click()', element)

# Scroll to element when it's visible
driver.execute_script("arguments[0].scrollIntoView()", element)

position = driver.execute_script('return document.scrollLeft+=100')
print("Position 1 --> "+str(position))

position = driver.execute_script('return document.scrollTop+=100')
print("Position 2 --> "+str(position))


# Refresh The page
driver.execute_script('history.go(0);')