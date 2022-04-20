from tkinter import *
from tkinter.ttk import *

import requests 
root=Tk()
root.title('Weather App')
def findWeather():
    city=city_text.get()
    link='https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=22515dbe8047cf659da74a1cae281c2e'
    response=requests.get(link)
    data=response.json()
    placeLabel['text']="{} , {}".format(data['name'],data['sys']['country'])
    tempLabel['text']='Temprature : {} °C'.format(data['main']['temp'])
root.geometry('500x300')
title=Label(root,text='Weather App',font=('bold',15)).place(x=190,y=50)

cityLabel=Label(root,text='Enter the city name:',font=('bold',15)).place(x=150,y=80)
city_text=StringVar()
city_entry=Entry(root,textvariable=city_text)
city_entry.place(x=185,y=120)

goButton=Button(root,text='Go',width=12,command=findWeather)
goButton.place(x=210,y=150)
placeLabel=Label(root,text='',font=('bold',15))
placeLabel.place(x=200,y=190)
tempLabel=Label(root,text='',font=('bold',15))
tempLabel.place(x=200,y=240)
root.mainloop()