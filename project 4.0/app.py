from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from tkinter import messagebox
import pyttsx3
import threading
import speech_recognition as sr
root = Tk()
root.title("Sky Watch")
root.geometry("1000x500+200+100")
root.resizable(False, False)
# For voice 
engine = pyttsx3.init()
engine.setProperty('rate', 120)

def speak_weather(city_searched, weather_condition, temperature_searched):
    engine.say(f"The current weather condition for {city_searched} is {weather_condition} with temperature of {temperature_searched:.2f} degree Celsius")
    engine.runAndWait()

# Background image placeholders (replace with your image paths)
background_image_default = PhotoImage(file="weather/default.png")
background_image_clear = PhotoImage(file="weather/clear_sky.png") 
background_image_mist = PhotoImage(file="weather/mist.png")  # New image for mist
background_image_haze = PhotoImage(file="weather/haze.png")  # New image for haze
background_image_overcast_clouds = PhotoImage(file="weather/overcast_clouds.png")  # New image for overcast clouds
background_image_scattered_clouds = PhotoImage(file="weather/scattered_clouds.png")  # New image for scattered clouds
background_image_rainy = PhotoImage(file="weather/rainy.png")  # New image for rainy
background_image_snow = PhotoImage(file="weather/snow.png")  # New image for snow

# Create initial background label
background_label = Label(root, image=background_image_default)
background_label.place(x=0, y=0, relwidth=1.0, relheight=1.0)


def getWeather(city=None):
    if city is None:
        city = text_field.get()
    try:
        city = text_field.get()
        geolocator = Nominatim(user_agent="geoapiExcercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # API Key (replace with your own)
        api_key = "8a49d853e61614da31e7900027c646dd"
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        json_data = requests.get(api).json()
        temperature = json_data['main']['temp'] - 273.15
        t.config(text=f"Temperature: {temperature:.2f}°C")
        c.config(text=f"Weather: {json_data['weather'][0]['main']}")
        w.config(text=f"Wind Speed: {json_data['wind']['speed']} m/s")
        h.config(text=f"Humidity: {json_data['main']['humidity']}%")
        d.config(text=f"Description: {json_data['weather'][0]['description']}")
        p.config(text=f"Pressure: {json_data['main']['pressure']} hPa")

        # Change background based on weather condition
        weather_condition = json_data['weather'][0]['description'].lower()
        city_searched = json_data['name'].lower()
        temperature_searched = temperature
        if (weather_condition == "clear sky"):
            background_label.config(image=background_image_clear)            
        elif weather_condition in ["mist", "fog", "light fog", "heavy fog", "moderate fog", "smoke"]:
            background_label.config(image=background_image_mist)
        elif(weather_condition == "haze"):
            background_label.config(image=background_image_haze)
        elif weather_condition in ["overcast clouds","heavy clouds"]:
            background_label.config(image=background_image_overcast_clouds)
        elif weather_condition in ["scattered clouds", "partial clouds", "moderate clouds", "few clouds","broken clouds"]:
            background_label.config(image=background_image_scattered_clouds)
        elif weather_condition in["heavy intensity rain","rainy", "moderate rain", "heavy rain", "light rain", "shower rain"]:
            background_label.config(image=background_image_rainy)
        elif weather_condition in ["snow", "moderate snow", "heavy snow", "light snow", "shower snow", "shower snow"]:
            background_label.config(image=background_image_snow)
        else:
            background_label.config(image=background_image_default)
        threading.Thread(target=speak_weather, args=(city_searched, weather_condition, temperature_searched)).start()

    except Exception as e:
        messagebox.showerror("Weather Forecasting Application", f"Error: {e}")

def voice_search():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for city name...")
        audio = recognizer.listen(source)
        try:
            city = recognizer.recognize_google(audio)
            print(f"You said: {city}")
            text_field.delete(0, END)
            text_field.insert(0, city)
            getWeather(city)
        except sr.UnknownValueError:
            messagebox.showerror("Voice Search", "Sorry, I could not understand the audio.")
        except sr.RequestError:
            messagebox.showerror("Voice Search", "Could not request results from the speech recognition service.")


text_field = Entry(root, font=("arial", 14), bg="#808080", fg="white")
text_field.place(x=400, y=22)

text_field.bind("<Return>", lambda event: getWeather(text_field.get()))


image_search_icon = PhotoImage(file="search1.png")
voice_search_icon=PhotoImage(file="voice.png")

image_search_icon = image_search_icon.subsample(10, 10)
voice_search_icon= voice_search_icon.subsample(10,10)
search_icon_button = Button(root, image=image_search_icon, borderwidth=0, cursor="hand2", command=getWeather)
search_icon_button.place(x=599, y=23)
voice_search_button = Button(root, image=voice_search_icon, command=voice_search)
voice_search_button.place(x=622 ,y=23)

# Logo here
image_logo = PhotoImage(file="weather_logo1.png")
weather_logo = Label(image=image_logo)
weather_logo.place(x=915, y=10)

# Time
name = Label(root, font=("arial", 15, "bold"),bg = "#ebebeb", fg="black")
name.place(x=50, y=100)
clock = Label(root, font=("Merriweather", 20),bg = "#ebebeb", fg="black")
clock.place(x=50, y=130)

# LABEL
label1 = Label(root, text="WIND", font=("Merriweather", 20, "bold"), fg="black")
label1.place(x=50, y=350)

label2 = Label(root, text="HUMIDITY", font=("Merriweather", 20, "bold"), fg="black")
label2.place(x=270, y=350)  

label3 = Label(root, text="DESCRIPTION", font=("Merriweather", 20, "bold"), fg="black")
label3.place(x=450, y=350)


label4 = Label(root, text="PRESSURE", font=("Merriweather", 20, "bold"), fg="black")
label4.place(x=720, y=350)  


t = Label(font=("arial", 16, "bold"),bg = "#ebebeb" , fg="red")
t.place(x=700, y=200)
c = Label(font=("arial", 16, "bold"),bg = "#ebebeb", fg="black")
c.place(x=700, y=250)
# LABEL
w = Label(text="...", font=("arial", 14),bg = "#ebebeb", fg="black")
w.place(x=50, y=380)  

h = Label(text="...", font=("arial", 14),bg = "#ebebeb", fg="black")
h.place(x=270, y=380)  

d = Label(text="...", font=("arial", 14),bg = "#ebebeb", fg="black")
d.place(x=450, y=380)
  

p = Label(text="...", font=("arial", 14),bg = "#ebebeb", fg="black")
p.place(x=720, y=380)

root.mainloop()
