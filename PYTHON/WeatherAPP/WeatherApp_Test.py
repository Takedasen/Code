import requests
from datetime import datetime
import tkinter as tk

API_KEY = "bda0bb1159cd72004aa8f820b2d18065"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
KELVIN = 273.15


def format_time_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


def get_weather_info(city_name):
    weather_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
    response = requests.get(weather_url)
    return response.json()


def format_weather_info(weather_info, city_name):
    if weather_info["cod"] != 200:
        return f"Weather in '{city_name}' not found!\nPlease enter a valid city name."

    temp = int(weather_info["main"]["temp"] - KELVIN)
    feels_like_temp = int(weather_info["main"]["feels_like"] - KELVIN)
    pressure = weather_info["main"]["pressure"]
    humidity = weather_info["main"]["humidity"]
    wind_speed = weather_info["wind"]["speed"] / 3.6
    sunrise = weather_info["sys"]["sunrise"]
    sunset = weather_info["sys"]["sunset"]
    timezone = weather_info["timezone"]
    cloudy = weather_info["clouds"]["all"]
    description = weather_info["weather"][0]["description"]
    sunrise_time = format_time_for_location(sunrise + timezone)
    sunset_time = format_time_for_location(sunset + timezone)

    return (
        f"Weather in: {city_name}\n\n"
        f"Temperature: {temp}°C\n"
        f"Feels like: {feels_like_temp}°C\n"
        f"Pressure: {pressure} hPa\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed:.2f} m/s\n"
        f"Sunrise: {sunrise_time}\n"
        f"Sunset: {sunset_time}\n"
        f"Clouds: {cloudy}%\n"
        f"Additional Info: {description}"
    )


def show_weather():
    city_name = city_value.get()
    weather_info = get_weather_info(city_name)
    weather = format_weather_info(weather_info, city_name)
    tfield.delete("1.0", "end")
    tfield.insert("1.0", weather)


root = tk.Tk()
root.geometry("800x650")
root.resizable(0, 0)
root.config(bg="#0a0a0a")
root.title("Weather App")

city_value = tk.StringVar()

city_head = tk.Label(
    root, text="Enter a city", font="Calibri 18 bold", bg="#0a0a0a", fg="white"
)
city_head.pack(pady=20)

inp_city = tk.Entry(
    root,
    textvariable=city_value,
    width=24,
    font="Calibri 18",
    bg="black",
    fg="white",
    insertbackground="white",
)
inp_city.pack()

check_weather_button = tk.Button(
    root,
    text="Check Weather",
    font="Calibri 18 bold",
    bg="red",
    fg="black",
    activebackground="white",
    padx=10,
    pady=10,
    command=show_weather,
)
check_weather_button.pack(pady=30)

weather_now = tk.Label(
    root, text="Current Weather Info", font="Calibri 18 bold", bg="#0a0a0a", fg="white"
)
weather_now.pack(pady=10)

tfield = tk.Text(
    root,
    width=60,
    height=11,
    font="Calibri 18",
    bg="black",
    fg="white",
    padx=10,
    pady=10,
)

tfield.pack()

root.bind("<Return>", lambda event: show_weather())

root.mainloop()
