import requests
from datetime import datetime
from tkinter import *

root = Tk()
root.geometry("800x650")
root.resizable(0, 0)
root.config(bg="#0a0a0a")
root.title("Weather App")

city_value = StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def show_weather():
    api_key = "bda0bb1159cd72004aa8f820b2d18065"
    city_name = city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    tfield.delete("1.0", "end")
    if weather_info['cod'] == 200:
        kelvin = 273.15
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] / 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        weather = f"Weather in: {city_name}\n\nTemperature: {temp}°C\nFeels like: {feels_like_temp}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed:.2f} m/s\nSunrise: {sunrise_time}\nSunset: {sunset_time}\nClouds: {cloudy}%\nAdditional Info: {description}"
    else:
        weather = f"Weather in '{city_name}' not found!\nPlease enter a valid city name."
    tfield.insert(INSERT, weather)

#! Interface
city_head = Label(root, text='Enter a city:', font='Calibri 18', bg='#0a0a0a', fg='white')
city_head.pack(pady=20)

inp_city = Entry(root, textvariable=city_value, width=24, font='Calibri 16')
inp_city.pack()

Button(root, command=show_weather, text="Check Weather", font="Calibri 14 bold", bg='red', fg='white', activebackground="white", padx=10, pady=10).pack(pady=30)

weather_now = Label(root, text="Current Weather Info", font='Calibri 20 bold', bg='#0a0a0a', fg='white')
weather_now.pack(pady=10)

tfield = Text(root, width=60, height=11, font='Calibri 14', bg='white', fg='black', padx=10, pady=10)
tfield.pack()

root.bind('<Return>', lambda event: show_weather())

root.mainloop()
