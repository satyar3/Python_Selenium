from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.set_page_load_timeout(10)
driver.delete_all_cookies()
driver.maximize_window()

driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')

multi_select_dropdown = driver.find_element(By.ID, 'justAnInputBox')
multi_select_dropdown.click()

choice_list = driver.find_elements(By.CSS_SELECTOR, '.comboTreeItemTitle')

print(f'Choice list size : {len(choice_list)}')

for choice in choice_list:
    print(f'Choice is : {choice.text}')


def click_on_given_list(list_of_item: list):
    for each_choice in choice_list:
        if each_choice.text in list_of_item:
            each_choice.click()
            list_of_item.remove(each_choice.text)

    if len(list_of_item) == 0:
        print(f'All choices has been selected')
    else:
        [print(f'Left with choices {i}') for i in list_of_item]


click_on_given_list(['choice 1', 'choice 2 1', 'choice 6 1', 'choice 6 1 A'])

driver.quit()
