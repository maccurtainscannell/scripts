from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains 
import time


driver = webdriver.Chrome()

#open strava

driver.get("https://www.strava.com/athlete/training")

#find email box

usr=input("Enter your password")
pwd=input("Enter your password")

username_box = driver.find_element(By.ID, 'email')
username_box.send_keys(usr)

password_box = driver.find_element(By.ID, 'password')
password_box.send_keys(pwd)
password_box.submit()

time.sleep(3)

for page in range(4):

    # Get all the elements available with name 'edit'

    edit_buttons = driver.find_elements(By.XPATH, '//button[text()="Edit"]')
    sport_dropdowns = driver.find_elements(By.ID, 'type')

    shoe_dropdowns= driver.find_elements(By.ID, 'athlete_gear_id')
    save_buttons = driver.find_elements(By.XPATH, '//button[text()="Save"]')

    iteration = 0

    for activity in range(20):

        print(iteration)
        edit_button = edit_buttons[activity]
        edit_button.click()
        print('Click edit')

        sport_dropdown = Select(sport_dropdowns[activity])
    
        print(sport_dropdown.first_selected_option.get_attribute("value"))
        if sport_dropdown.first_selected_option.get_attribute("value") == 'Run':

            shoe_dropdown=Select(shoe_dropdowns[activity])
            print('Open dropdown')
            shoe_dropdown.select_by_visible_text("ASICS Gel Noosa Tri 14")

        time.sleep(1)

        save_button = save_buttons[activity]
        print('Click save')
        save_button.click()

        time.sleep(1)

        iteration = iteration + 1
        
    next_page_button = driver.find_elements(By.XPATH, '//button[@class="btn btn-default btn-sm next_page"]')
    next_page_button[0].click()

time.sleep(30)
