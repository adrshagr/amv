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


#second cell

#third cell

#fourth cell

#fifth cell

#sixth cell

#seventh cell


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

#second cell
secondframe=Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=325)

day2=Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10,y=5)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

#third cell
thirdframe=Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=325)

day3=Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=10,y=5)

thirdimage=Label(thirdimage,bg="#282829")
thirdimage.place(x=7,y=20)

#fourth cell
fourthframe=Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=505,y=325)

day4=Label(fouthframe,bg="#282829",fg="#fff")
day4.place(x=10,y=5)

fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=20)

#fifth cell
fifthframe=Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=325)

day5=Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=10,y=5)

fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=20)

#sixth cell
sixthframe=Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=325)

day6=Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=10,y=5)

sixthimage=Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=20)

#seventh cell
seventhframe=Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=805,y=325)

day7=Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=10,y=5)

seventhimage=Label(seventhframe,bg="#282829")
seventhimage.place(x=7,y=20)


