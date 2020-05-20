## Combining hotels data and location data for wild swimming (with notes)

# Seem to need to enter curl -L http://pl.ntr/certpt >> ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/Package\ Control.user-ca-bundle in terminal every single time

print("Starting search ...")
print

from bs4 import BeautifulSoup
import requests
import ssl
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import re, urllib2
import pandas as pd


page_link = 'http://www.wildswimming.co.uk/wild-swim-map-uk/?multi_region=wild-swim-map-uk'
# this is the url that we've already determined is safe and legal to scrape from.

page_response = requests.get(page_link, timeout=25)
# here, we fetch the content from the url, using the requests library

page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.

textContent = []
headerContent = []
addressContent = []
latitude = []
longitude = []



# Location

print("Getting swim locations.")
print

integerIndex = 0
while True: 
    
    try:
        text = page_content.find_all("p")[integerIndex].text


    except IndexError as error:
        break

    if integerIndex % 3 == 1:

        textContent.append(text)
        
    integerIndex = integerIndex + 1


# Header Loop
integerIndex = 0
while True:

    try:
        title = page_content.find_all("h3")[integerIndex].text

    except IndexError as error:
        break

    headerContent.append(title)
    integerIndex = integerIndex + 1 



## Clean up and create dataset

# Locations
textIndex = (i for i, val in enumerate(textContent) if re.match(".*Read more", val))
cleanText = textContent[1:min(x for x in textIndex)]

# Google Locations

geolocator = Nominatim()
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

## Add coordinate data

print("Gathering location data.")
print
for place in cleanText:

        r = re.search("km", place)
        if r != None:
            place = place.split(', ')[0:(len(place.split(', '))-1)]

            try:
                location = geolocator.geocode(place + ", United Kingdom")
                addressContent.append(location.address)
                latitude.append(location.latitude)
                longitude.append(location.longitude)

            except urllib2.HTTPError:
                location = "No location data available at this time"
                addressContent.append("No location data available at this time")
                latitude.append("No location data available at this time")
                longitude.append("No location data available at this time")

            except:
                location = "No such location found"
                addressContent.append("No such location found")
                latitude.append("No such location found")
                longitude.append("No such location found")
            
        else:
            try:
                location = geolocator.geocode(place + ", United Kingdom")
                addressContent.append(location.address)
                latitude.append(location.latitude)
                longitude.append(location.longitude)
            except:
                location = "No such location found"
                addressContent.append("No such location found")
                latitude.append("No such location found")
                longitude.append("No such location found")


# Headers

headerIndex = (i for i, val in enumerate(headerContent) if re.match(".*No Records", val))
cleanHeaders = headerContent[0:min(x for x in headerIndex)]


# Dataframe
cleanDF = pd.concat([pd.DataFrame(cleanHeaders),pd.DataFrame(cleanText),
    pd.DataFrame(addressContent), pd.DataFrame(latitude),
    pd.DataFrame(longitude)], axis = 1)

print(cleanDF)

# Import hotels data



# Heathrow coordinates

print(geolocator.geocode("London Heathrow Airport"))

latLHR = 51.471429
longLHR = -0.487932



