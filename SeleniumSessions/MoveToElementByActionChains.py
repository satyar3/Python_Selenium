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
target_locator = driver.find_element(By.ID, "some_locator")

action_chains.move_to_element(target_locator).perform()