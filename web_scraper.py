import pandas as pd 
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.4255&lon=-111.9372')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

# print(week)
items = week.find_all(class_='tombstone-container')
# print(items[0]) 

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp ').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
temps = [item.find(class_='temp').get_text() for item in items]
short_descs = [item.find(class_='short-desc').get_text() for item in items]

# print(period_names)
# print(temps)
# print(short_descs)

weather_stuff = pd.DataFrame(
    {
     'Period': period_names,
     'Short_des': short_descs,
     'Temps': temps,
     })

print(weather_stuff)

weather_stuff.to_csv('Weather.csv')