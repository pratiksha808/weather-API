import tkinter as tk
from tkinter import *
from typing import final
import requests
import time

def getweather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=9d370fa4af20a0697f663dbe75941970"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))
    
    final_info = condition + "\n" +str(temp) + "C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset 
    Label1.config(text = final_info)
    Label2.config(text = final_data)




canvas = tk.Tk()
canvas.geometry("1920x1080")
canvas.title("weather App API")
bg = PhotoImage(file='weather')

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getweather)

Label1 = tk.Label(canvas, font = t)
Label1.pack()
Label2 = tk.Label(canvas, font = f)
Label2.pack()
Label3 = Label(canvas, image=bg)
Label3.pack()

canvas.mainloop()

