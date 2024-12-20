from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.set_page_load_timeout(10)

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")

driver.find_element(By.XPATH, "//h2[text()='JavaScript Alert']//following-sibling::button")

alert = driver.switch_to.alert

print(f'Alert text {alert.text}')

alert.accept()
alert.dismiss()
alert.send_keys("Some_text")

driver.switch_to.default_content()

driver.quit()
