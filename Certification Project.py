from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import urllib
import requests
from bs4 import BeautifulSoup

'''
Create a python script called googlesearch that provides a command line utility to
perform google search. It gives you the top links (search results) of whatever you want to
search on google
'''
#
# # desktop user-agent
# USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# # mobile user-agent
# MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
#
# query = "hackernoon How To Scrape Google With Python"
# query = query.replace(' ', '+')
# URL = f"https://google.com/search?q={query}"
#
# headers = {"user-agent": USER_AGENT}
# resp = requests.get(URL, headers=headers)
#
# if resp.status_code == 200:
#     soup = BeautifulSoup(resp.content, "lxml")
#     h3 = soup.h3
#     for g in soup.find_all('h3'):
#         print(g.text)
'''
Q2: Create a script called location that return the location parameters of any location you want.
'''
# s_city = "Moscow,RU"
# city_id = 0
# appid = "6e03ca95d92775ea97b56029b1429434"
# try:
#     res = requests.get("http://api.openweathermap.org/data/2.5/find",
#                  params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
#     data = res.json()
#     cities = ["{} ({})".format(d['name'], d['sys']['country'])
#               for d in data['list']]
#     print("city:", cities)
#     city_id = data['list'][0]['id']
#     print('city_id=', city_id)
# except Exception as e:
#     print("Exception (find):", e)
#     pass
'''
Q3: Create a script called weather that return the environmental parameters (temperature (min, max),
windspeed, humidity, cloud, pressure, sunrise and sunset) of any location you want;
after passing arguments (like user api and city id).
'''
# owm = OWM('f8012571c287aae51d76885a56afb3ba')
# mgr = owm.weather_manager()
#
# city = input('Input city: ')
# observation = mgr.weather_at_place(city)
# Weather = observation.weather
#
# print(f'{Weather.status}')
# print(f'{Weather.detailed_status}')
# print(f"Temperature min {Weather.temperature('celsius')['temp_min']}")
# print(f"Temperature max {Weather.temperature('celsius')['temp_max']}")
# print(f"Speed of wind {Weather.wind()['speed']}")
# print(f"Barometric pressure {Weather.barometric_pressure()['press']}")
# print(f"Sunrise {Weather.sunrise_time(timeformat='date')}")
# print(f"Sunset {Weather.sunset_time(timeformat='iso')}")


