from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.set_page_load_timeout(10)
driver.delete_all_cookies()
driver.maximize_window()

driver.get("https://spicejet.com")

action_chains = ActionChains(webdriver)
source_locator = driver.find_element(By.ID, "source_locator")
target_locator = driver.find_element(By.ID, "target_locator")

action_chains.move_to_element(source_locator).click_and_hold(source_locator).release(target_locator).perform()

#or

action_chains.drag_and_drop(source_locator, target_locator).perform()