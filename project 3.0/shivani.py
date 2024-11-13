from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from tkinter import messagebox
import os  # to check for the existence of image files

root = Tk()
root.title("Sky Watch")
root.geometry("1000x500+200+100")
root.configure(bg="#ebebeb")
root.resizable(False, False)

# Check if image files exist before using them
def check_image_exists(image_path):
    return os.path.exists(image_path)

# Load Image if exists
def load_image(image_path, resize_factor=(10, 10)):
    if check_image_exists(image_path):
        image = PhotoImage(file=image_path)
        return image.subsample(*resize_factor)
    else:
        print(f"Error: Image file '{image_path}' not found.")
        return None

# Get Weather Data
def getWeather():
    try:
        city = text_field.get()  # Get user input from the Entry widget
        if not city:  # If no city is entered, prompt user
            messagebox.showerror("Input Error", "Please enter a city name.")
            return

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        if location is None:  # If no location found
            messagebox.showerror("Error", f"City '{city}' not found.")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        if result is None:  # If timezone is not found
            messagebox.showerror("Error", f"Timezone for city '{city}' not found.")
            return

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Using your API key for OpenWeather
        api_key = "YOUR_API_KEY"  # Replace with your actual key or load it securely
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        json_data = requests.get(api).json()
        
        # Handle case where city is not found in OpenWeather
        if json_data.get("cod") != 200:
            messagebox.showerror("Error", f"Could not retrieve weather data for {city}.")
            return

        # Extract weather details
        temperature = json_data['main']['temp'] - 273.15
        t.config(text=f"Temperature: {temperature:.2f}°C")
        c.config(text=f"Weather: {json_data['weather'][0]['main']}")
        w.config(text=f"Wind Speed: {json_data['wind']['speed']} m/s")
        h.config(text=f"Humidity: {json_data['main']['humidity']}%")
        d.config(text=f"Description: {json_data['weather'][0]['description']}")
        p.config(text=f"Pressure: {json_data['main']['pressure']} hPa")

    except Exception as e:
        messagebox.showerror("Weather Forecasting Application", f"Error: {e}")

# Entry widget for city input
text_field = Entry(root, font=("arial", 14), bg="#ebebeb", fg="black")
text_field.place(x=400, y=22)
text_field.bind("<Return>", lambda event: getWeather())  # Bind Enter key

# Search icon button
image_search_icon = load_image("search1.png", resize_factor=(10, 10))
if image_search_icon:
    search_icon_button = Button(root, image=image_search_icon, borderwidth=0, cursor="hand2", command=getWeather)
    search_icon_button.place(x=599, y=23)

# Weather logo
image_logo = load_image("weather_logo1.png", resize_factor=(10, 10))
if image_logo:
    weather_logo = Label(image=image_logo)
    weather_logo.place(x=400, y=80)

# Time and Weather Data Labels
name = Label(root, font=("arial", 15, "bold"), bg="#ebebeb", fg="black")
name.place(x=50, y=100)
clock = Label(root, font=("Merriweather", 20), bg="#ebebeb", fg="black")
clock.place(x=50, y=130)

label1 = Label(root, text="WIND", font=("Merriweather", 20, "bold"), bg="#ebebeb", fg="black")
label1.place(x=50, y=350)

label2 = Label(root, text="HUMIDITY", font=("Merriweather", 20, "bold"), bg="#ebebeb", fg="black")
label2.place(x=270, y=350)

label3 = Label(root, text="DESCRIPTION", font=("Merriweather", 20, "bold"), bg="#ebebeb", fg="black")
label3.place(x=450, y=350)

label4 = Label(root, text="PRESSURE", font=("Merriweather", 20, "bold"), bg="#ebebeb", fg="black")
label4.place(x=720, y=350)

# Dynamic weather data display
t = Label(font=("arial", 16, "bold"), bg="#ebebeb", fg="red")
t.place(x=700, y=200)
c = Label(font=("arial", 16, "bold"), bg="#ebebeb", fg="black")
c.place(x=700, y=250)

w = Label(text="...", font=("arial", 14), bg="#ebebeb", fg="black")
w.place(x=50, y=380)

h = Label(text="...", font=("arial", 14), bg="#ebebeb", fg="black")
h.place(x=270, y=380)

d = Label(text="...", font=("arial", 14), bg="#ebebeb", fg="black")
d.place(x=450, y=380)

p = Label(text="...", font=("arial", 14), bg="#ebebeb", fg="black")
p.place(x=720, y=380)

root.mainloop()
