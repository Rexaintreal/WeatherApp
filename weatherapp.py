import customtkinter as ctk
import tkinter as tk
from datetime import datetime
import json
import tkintermapview
import requests


class Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("1366x768")
        self.title("Weather App - by Saurabh")
        #settign the max and min size of the window
        self.minsize(width=640, height=480)
        self.maxsize(width=1366, height=768)
        self.grid_rowconfigure(0, weight=1)
        #configuring the grid system
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = Frame(master=self, )
        self.my_frame.grid(row=0,
                           column=0,
                           padx=20,
                           pady=20,
                           sticky="nsew")
        self.entry=ctk.CTkEntry(master=self,
                                placeholder_text="Enter the location",
                                width=1300,
                                font=("",20),
                                height=25,
                                border_width=0,
                                corner_radius=12)
        self.entry.place(relx=0.5,rely=0.075,anchor=tk.CENTER)
        self.map_widget=tkintermapview.TkinterMapView(self,
                                                 width=960,
                                                 height=580,
                                                 corner_radius=14)
        self.map_widget.place(relx=0.62,rely=0.53,anchor=tk.CENTER)
        self.map_widget.set_position(28.7041,77.1025)
        self.map_widget.set_zoom(0)
        self.map_widget.set_address("")
        self.location=ctk.CTkButton(master=self,
                                    width=130,
                                    height=30,
                                    border_width=0,
                                    corner_radius=8,
                                    text="Submit",
                                    font=("",20),
                                    command=self.getLocation)
        self.location.place(relx=0.134, rely=0.90, anchor=tk.CENTER)
        self.textbox=ctk.CTkLabel(self,
                                    width=275,
                                    height=500,
                                    corner_radius=20,
                                    text="",
                                    font=("",20))
        self.textbox.place(relx=0.134,rely=0.5,anchor=tk.CENTER)

    def getLocation(self):
        global weather
        #Getting the location from the user
        add=self.entry.get()
        if "i" in "i":
            self.map_widget.set_address(add)
        #api key of openwheather API
        api_key="your_api_key"
        weather_url='http://api.openweathermap.org/data/2.5/weather?q='+add+'&appid='+api_key
        response = requests.get(weather_url)
        weather_info=response.json()
        if weather_info ['cod'] == 200:
            kelvin=273

            temp = int(weather_info['main']['temp'] - kelvin)  # converting default kelvin value to Celcius
            feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            wind_speed = weather_info['wind']['speed'] * 3.6
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']

            weather = f"\nWeather of: {add}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\n Cloud: {cloudy}%\nInfo: {description}"
            self.textbox.configure(text=weather)
        else:
            self.textbox.configure(text="Not found")

app=App()
app.mainloop()
