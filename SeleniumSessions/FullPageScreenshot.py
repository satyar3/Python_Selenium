from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Ensures headless mode
chrome_options.add_argument("--disable-gpu")  # Required for headless on Windows
chrome_options.add_argument("--window-size=1920,1080")  # Optional: Set window size

driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()

# Enable headless mode explicitly
driver.get("https://www.reddit.com")

driver.get_screenshot_as_file("Screenshot.png")

driver.maximize_window()
driver.fullscreen_window()
driver.save_screenshot("Screenshot_Full_page.png")

# Test cases hsould run in headless mode
s = lambda x: driver.execute_script('return document.body.parentNode.scroll' + x)

driver.set_window_size(s('Width'), s('Height'))
driver.find_element(By.TAG_NAME, 'body').screenshot('Screenshot_Full_page_2.png')
