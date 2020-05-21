"""
Installed selenium
Downloaded ChromeDriver - note that I'm on version 80 because current version of Chrome is Chrome 83. 
Might need updating later

Turns out the active portion of the screen is an iframe, so that's at https://cli.fusio.net/cli/climate_data/showdata.php rather than at https://www.met.ie/climate/available-data/historical-data
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome('/Applications/chromedriver', options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
driver.get("https://cli.fusio.net/cli/climate_data/showdata.php")
time.sleep(5)

"""
There are three controls on the data download - data resolution; county; station.

<br />

Data resolution controls whether the data is hourly, daily or monthly. The control values for these three are 1, 9 and 2 respectively

<br />

County controls the county of choice, and also includes buoys (named "Buoys). These are also controlled by numerical parameters, below. However, the dropdown for daily and monthly differs from the dropdown for hourly. We can figure out how we want to do this later, but it seems like maybe we just try all of the counties and let it fail with an exception and continue, given that we do have all the numbers between 1 and 27.

|county|value|
| :- | :- |
|Carlow|10|
|Cavan|24|
|Clare|6|
|Cork|1|
|Donegal|26|
|Dublin|14|
|Galway|19|
|Kerry|2|
|Mayo|21|
|Meath|15|
|Roscommon|20|
|Sligo|22|
|Tipperary|4|
|Westmeath|16|
|Wexford|7|

<br />

Additionally for hourly

|county|value|
| :- | :- |
|Buoys|27|

<br />

Additionally for daily, monthly

|county|value|
| :- | :- |
|Kildare|13|
|Kilkenny|8|
|Laois|11|
|Leitrim|23|
|Limerick|5|
|Longford|18|
|Louth|17|
|Monaghan|25|
|Offaly|12|
|Waterford|3|
|Wicklow|9|


Station is a bit more complex, because the stations depend on county with no overlap. Station codes are 4 digit codes and we could just iterate through them all, but that seems wasteful for only about 100 stations.
"""

resolutions = [1,9,2]
counties = xrange(1,28)
stations = 

for res in resolutions:

    resolution = driver.find_element_by_xpath("//*[@name='stntype'][@value='%d']" % res).click()
    time.sleep(5)
    
    for cty in counties:
    
        county = Seldriverdriver.find_element_by_xpath("//*[@name='countyno']")).select_by_value('%d', % cty)
        time.sleep(5)
        
        #station




time.sleep(5)
driver.quit()

"""
Useful SO articles/other sources:

1. https://stackoverflow.com/questions/35184153/writing-a-script-to-download-files-from-a-website-python-selenium
2. https://dev.to/endtest/a-practical-guide-for-finding-elements-with-selenium-4djf
3. https://www.guru99.com/find-element-selenium.html
4. https://stackoverflow.com/questions/7867537/how-to-select-a-drop-down-menu-value-with-selenium-using-python
"""

# This cell useful for left aliging the table when run in Jupyter. It can be run out of order.

%%html
<style>
  table {margin-left: 0 !important;}
</style>
