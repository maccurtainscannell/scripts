#SO article here https://stackoverflow.com/questions/35184153/writing-a-script-to-download-files-from-a-website-python-selenium

#Installed selenium
#Downloaded ChromeDriver - note that I'm on version 80 because current version of Chrome is Chrome 80. 
#Might need updating later

from selenium import webdriver
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome('/Applications/chromedriver', options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
driver.get("https://www.met.ie/climate/available-data/historical-data")


search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()
