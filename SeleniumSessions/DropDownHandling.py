from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.delete_all_cookies()
driver.maximize_window()

driver.get("https://demo.guru99.com/test/newtours/register.php")
country = driver.find_element(By.NAME,'country')
select = Select(country)
all_dropdown_values = select.options

print(f'All Countries are {all_dropdown_values}')


select.select_by_value('INDIA')
select.select_by_index(4)
select.select_by_visible_text('ARUBA')



def select_action(func, *args):
    return func(*args)

select_action(select.select_by_value, 'MACAU')

print(f'Is it a Multi Dropdown : {select.is_multiple}')

#select.deselect_all()

