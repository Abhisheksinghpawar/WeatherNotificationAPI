city = "Bhopal"

import requests
import time
from plyer import notification
import math

while True:

    json_data = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q={}".format(city)).json()
    Weather = json_data['main']
    t = Weather["temp"] - 275
    f = Weather["feels_like"] - 275
    h = Weather["humidity"]

    t = math.floor(t)
    f = math.floor(f)
    h = math.floor(h)

    tm = time.strftime("%H:%M", time.localtime())
    
    title = "{} at {}".format(city,time.strftime("%H:%M", time.localtime()))
    
    message = "Weather {}°C \n Feels like {}°C\n Humidity {}%".format(t,f,h)

    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\Abhishek\E Drive\Padhai\Programming\Python\Progs\Iconsmind-Outline-Glass-Water.ico",
        timeout = 5
        )
    time.sleep(60)#Sec
