import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

API_KEY = '87bdf6d0e9a777fb4a03cf74f28e5922'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    
    if weather.get('cod') != 200:
        messagebox.showerror("Error", "City not found.")
        return
    
    temp = weather['main']['temp']
    humidity = weather['main']['humidity']
    description = weather['weather'][0]['description']
    icon_code = weather['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    
    temp_label.config(text=f"Temperature: {temp}°C")
    humidity_label.config(text=f"Humidity: {humidity}%")
    description_label.config(text=f"Weather: {description}")
    
    icon_response = requests.get(icon_url)
    icon_image = Image.open(io.BytesIO(icon_response.content))
    icon_photo = ImageTk.PhotoImage(icon_image)
    icon_label.config(image=icon_photo)
    icon_label.image = icon_photo

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack()

temp_label = tk.Label(root, text="Temperature:")
temp_label.pack()

humidity_label = tk.Label(root, text="Humidity:")
humidity_label.pack()

description_label = tk.Label(root, text="Weather:")
description_label.pack()

icon_label = tk.Label(root)
icon_label.pack()

root.mainloop()
