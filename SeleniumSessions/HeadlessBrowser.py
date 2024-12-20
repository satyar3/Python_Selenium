from selenium import webdriver

# Create ChromeOptions instance
chrome_options = webdriver.ChromeOptions()

# Enable headless mode explicitly
chrome_options.add_argument("--headless")  # Ensures headless mode
chrome_options.add_argument("--disable-gpu")  # Required for headless on Windows
chrome_options.add_argument("--window-size=1920,1080")  # Optional: Set window size

# Pass options to the Chrome driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://google.com")

# Print the page title
print(f"Page title is: {driver.title}")
driver.quit()
