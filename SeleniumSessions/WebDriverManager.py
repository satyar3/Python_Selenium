from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser_name = input("Enter the Browser Name : ")

if browser_name.casefold() == 'chrome':
    # Set up ChromeDriver with Service and WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
else:
    raise Exception('Driver Not Defined')

# Navigate to Google
driver.get("https://google.com")
print(f'Page Title is {driver.title}')

# Quit the driver
driver.quit()
