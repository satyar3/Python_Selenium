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
target_locator = driver.find_element(By.ID, "target_locator")

action_chains.context_click(target_locator).perform()
