from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from tkinter import messagebox
#from PIL import Image, ImageTk 

root = Tk()
root.title("Weather Forecasting Application")
root.geometry("1000x500+200+100")
root.resizable(False, False)

# Entry widget for user input
#text_field = Entry(root, font=("arial", 14))
#text_field.place(x=20, y=20)


# Create a custom search icon image with black color
"""
custom_search_icon_black = Image.new('RGBA', (16, 16), color=(0, 0, 0, 255))  # Black color (R, G, B, Alpha)
custom_search_icon_black.save('custom_search_icon_black.png', 'PNG')

image_search_icon_black = ImageTk.PhotoImage(file="custom_search_icon_black.png")
"""


def getWeather():
    try:
        city = text_field.get()  # Get user input from the Entry widget
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

        # ADD YOUR OPENWEATHERMAP API KEY HERE
        api_key = "45542413ab890ab8e14f84105db2c439"
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        json_data = requests.get(api).json()
        temperature = json_data['main']['temp'] - 273.15
        t.config(text=f"Temperature: {temperature:.2f}°C")
        c.config(text=f"Weather: {json_data['weather'][0]['main']}")
        w.config(text=f"Wind Speed: {json_data['wind']['speed']} m/s")
        h.config(text=f"Humidity: {json_data['main']['humidity']}%")
        d.config(text=f"Description: {json_data['weather'][0]['description']}")
        p.config(text=f"Pressure: {json_data['main']['pressure']} hPa")

    except Exception as e:
        messagebox.showerror("Weather Forecasting Application", f"Error: {e}")




# Entry widget for user input
text_field = Entry(root, font=("arial", 14))
text_field.place(x=400, y=22)
text_field.lower()


# Load the image and resize it
image_search_icon = PhotoImage(file="search1.png")


# Resize the image by a factor of 2 in both x and y directions (you can adjust the values as needed)
image_search_icon = image_search_icon.subsample(10, 10)


# Calculate the size for the icon based on the text_field's height
#text_field_height = text_field.winfo_height()  # Get the height of the text_field
#icon_height = text_field_height - 4  # Adjust the icon height as needed

# Resize the image to match the calculated height
#image_search_icon = image_search_icon.subsample(int(image_search_icon.width() / icon_height), int(image_search_icon.height() / icon_height))

# Create a Button widget with the custom-sized search icon
search_icon_button = Button(root, image=image_search_icon, borderwidth=0, cursor="hand2", command=getWeather)
search_icon_button.place(x=599, y=23)

# Add Weather Logo
image_logo = PhotoImage(file="weather_logo1.png")
weather_logo = Label(image=image_logo)
weather_logo.place(x=400, y=80)

# Add Information Box
"""
image_box = PhotoImage(file="information_box.png")
information_box = Label(image=image_box, width=800, height=100)  
information_box.pack(padx=5, pady=5, side=BOTTOM)
information_box.place(x=40,y=330)
information_box.lower()
"""

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=50, y=100)
clock = Label(root, font=("Merriweather", 20))
clock.place(x=50, y=130)

# LABEL
label1 = Label(root, text="WIND", font=("Merriweather", 20, "bold"), fg="Black")
label1.place(x=50, y=350)

label2 = Label(root, text="HUMIDITY", font=("Merriweather", 20, "bold"), fg="Black")
label2.place(x=270, y=350)  

label3 = Label(root, text="DESCRIPTION", font=("Merriweather", 20, "bold"), fg="Black")
label3.place(x=450, y=350)  

label4 = Label(root, text="PRESSURE", font=("Merriweather", 20, "bold"), fg="Black")
label4.place(x=720, y=350)  


t = Label(font=("arial", 16, "bold"), fg="#ee666d")
t.place(x=700, y=200)
c = Label(font=("arial", 16, "bold"))
c.place(x=700, y=250)
# LABEL
w = Label(text="...", font=("arial", 14))
w.place(x=50, y=380)  

h = Label(text="...", font=("arial", 14))
h.place(x=270, y=380)  

d = Label(text="...", font=("arial", 14))
d.place(x=450, y=380)  

p = Label(text="...", font=("arial", 14))
p.place(x=720, y=380)  

root.mainloop()
