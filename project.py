home=pytz.timezone(result)
local_time=datetime.now(home)
current_time=local_time.strftime("%I:%M %p")
clock.config(text=current_time)

#weather
api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid={8a49d853e61614da31e7900027c646dd}"
json_data = requests.get(api).json()

#current
temp = json_data['current']['temp']
humidity = json_data['current']['humidity']
pressure = json_data['current']['pressure']
wind = json_data['current']['wind_speed']
description = json_data['current']['weather'][0]['description']
t.config(text=(temp,"°C"))
h.config(text=(humidity,"%"))
p.config(text=(pressure,"hPa"))
w.config(text=(wind,"m/s"))
d.config(text=description)

#first cell
firstdayimage=json_data['daily'][0][' weather '][0]['icon']
photol = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
firstimage.config(image=photol)
firstimage.image=photol

tempdayl = json_data['daily'][0]['temp']['day']
tempnight1=json_data['daily'][0]['temp']['night']

day1temp.config(text=f"Day:{tempday1Night}\n Night:{tempnightl}")
#second cell
seconddayimage=json_data['daily'][1][' weather '][0]['icon']

img=(Image.open(f"icon/{seconddayimage}@2x.png"))
resized_image=img.resize((50,50))
photo2 = ImageTk.PhotoImage(resized_image)
secondimage.config(image=photo2)
secondimage.image=photo2

tempday2 = json_data['daily'][1]['temp']['day']
tempnight2=json_data['daily'][1]['temp']['night']

day2temp.config(text=f"Day:{tempday2Night}\n Night:{tempnight2}")
#third cell
thirddayimage=json_data['daily'][2][' weather '][0]['icon']

img=(Image.open(f"icon/{thirddayimage}@2x.png"))
resized_image=img.resize((50,50))
photo3 = ImageTk.PhotoImage(resized_image)
thirdimage.config(image=photo3)
thirdimage.image=photo3

tempday3 = json_data['daily'][2]['temp']['day']
tempnight3=json_data['daily'][2]['temp']['night']

day3temp.config(text=f"Day:{tempday3Night}\n Night:{tempnight3}")
#fourth cell
fourthdayimage=json_data['daily'][3][' weather '][0]['icon']

img=(Image.open(f"icon/{fouthdayimage}@2x.png"))
resized_image=img.resize((50,50))
photo4 = ImageTk.PhotoImage(resized_image)
fourthimage.config( image=photo4)
fourthimage.image=photo4

tempdayl = json_data['daily'][3]['temp']['day']
tempnight1=json_data['daily'][3]['temp']['night']

day4temp.config(text=f"Day:{tempday4Night}\n Night:{tempnight4}")
#fifth cell
fifthdayimage=json_data['daily'][4][' weather '][0]['icon']

img=(Image.open(f"icon/{secondaydayimage}@2x.png"))
resized_image=img.resize((50,50))
photo5 = ImageTk.PhotoImage(resized_image)
fifthimage.config( image=photo5)
fifthimage.image=photo5

tempday5 = json_data['daily'][4]['temp']['day']
tempnight5=json_data['daily'][4]['temp']['night']

day5temp.config(text=f"Day:{tempday5Night}\n Night:{tempnight5}")
#sixth cell
sixthdayimage=json_data['daily'][5][' weather '][0]['icon']

img=(Image.open(f"icon/{sixthdaydayimage}@2x.png"))
resized_image=img.resize((50,50))
photo6 = ImageTk.PhotoImage(resized_image)
sixthimage.config( image=photo6)
sixthimage.image=photo6

tempday7 = json_data['daily'][5]['temp']['day']
tempnight7=json_data['daily'][5]['temp']['night']

day7temp.config(text=f"Day:{tempday7Night}\n Night:{tempnight7}")
#seventh cell
seventhdayimage=json_data['daily'][6][' weather '][0]['icon']

img=(Image.open(f"icon/{seventhdaydayimage}@2x.png"))
resized_image=img.resize((50,50))
photo7 = ImageTk.PhotoImage(resized_image)
seventhimage.config( image=photo7)
seventhimage.image=photo7

tempday7 = json_data['daily'][6]['temp']['day']
tempnight7=json_data['daily'][6]['temp']['night']

day7temp.config(text=f"Day:{tempday7Night}\n Night:{tempnight7}")
#days
first=datetime.now()
day1.config(text=first.strftime("%A"))

second = first+timedelta(days=1)
day2.config(text=second.strftime("%A"))

third = first+timedelta(days=2)
day3.config(text=third.strftime("%A"))

fourth = first+timedelta(days=3)
day4.config(text=fourth.strftime("%A"))

fifth = first+timedelta(days=4)
day5.config(text=fifth.strftime("%A"))

sixth = first+timedelta(days=5)
day6.config(text=sixth.strftime("%A"))

seventh = first+timedelta(days=6)
day7.config(text=seventh.strftime("%A"))

#thpwd
t= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=150,y=120)
h= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)
p= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)
w= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)
d= Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)

#first cell
firstframe=Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1=Label(firstframe,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

day1temp=Label(firstframe,bg="#282829",fg="#57adff",font="arial 15 bold")
day1temp.place(x=100,y=50)
#second cell
secondframe=Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=325)

day2=Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10,y=5)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

day2temp=Label(secondframe,bg="#282829",fg="#fff")
day2temp.place(x=2,y=70)
#third cell
thirdframe=Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=325)

day3=Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=10,y=5)

thirdimage=Label(thirdimage,bg="#282829")
thirdimage.place(x=7,y=20)

day3temp=Label(thirdframe,bg="#282829",fg="#fff")
day3temp.place(x=2,y=70)
#fourth cell
fourthframe=Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=505,y=325)

day4=Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=10,y=5)

fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=20)

day4temp=Label(fourthframe,bg="#282829",fg="#fff")
day4temp.place(x=2,y=70)
#fifth cell
fifthframe=Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=325)

day5=Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=10,y=5)

fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=20)

day5temp=Label(fifthframe,bg="#282829",fg="#fff")
day5temp.place(x=2,y=70)
#sixth cell
sixthframe=Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=325)

day6=Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=10,y=5)

sixthimage=Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=20)

day6temp=Label(sixthframe,bg="#282829",fg="#fff")
day6temp.place(x=2,y=70)
#seventh cell
seventhframe=Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=805,y=325)

day7=Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=10,y=5)

seventhimage=Label(seventhframe,bg="#282829")
seventhimage.place(x=7,y=20)

day7temp=Label(seventhframe,bg="#282829",fg="#fff")
day7temp.place(x=2,y=70)
