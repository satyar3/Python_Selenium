from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.set_page_load_timeout(10)
driver.delete_all_cookies()
driver.maximize_window()

driver.get("https://google.com")

action_chains = ActionChains(webdriver)

input_locator = driver.find_element(By.Name, "q")
btn_locator = driver.find_element(By.ID, "some_btn_locator")

action_chains.send_keys_to_element(input_locator, 'Text').perform()
action_chains.click(btn_locator).perform()
