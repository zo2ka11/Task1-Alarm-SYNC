import tkinter
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image

from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread

BackGroundColor = "#ffffff"
color = '#800080'
# window Attribute
window = Tk()
window.title("")
window.geometry('350x200')
window.configure(bg= BackGroundColor)

#Frams
framLine = Frame(window, width=400, height=5, bg= color)
framLine.grid(row=0, column=0)
framBody = Frame(window, width=400, height=400, bg= BackGroundColor)
framBody.grid(row=1, column=0)


def CreatLable(Ltext, a1, b1):
    temp = Label(framBody, text= Ltext, height=1, font=("Ivy 10 bold"), bg=BackGroundColor, fg=color)
    temp.place(x= a1, y= b1)

# Fram Body
image = Image.open('alarm.png')
image.resize((200, 200))
image = ImageTk.PhotoImage(image)
appImage = Label(framBody, height=50, image=image)
appImage.place(x=10, y=10)
CreatLable("Alarm", 150, 20)


hours_Values= ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
min_Values= ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15'
                   , '16', '17', '18', '19', '20', '21', '22', '23', '24'
                   , '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40'
                   , '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56'
                   , '57', '58', '59')
Sec_Values= min_Values
period_Values= ('Am', 'Pm')


selected = IntVar()

def button (B_text, a, b, command, val):
    Bfont = 'arial 10 bold'
    Bvalue = 1,
    back_Color = BackGroundColor
    var = selected
    
    btn = Radiobutton(framBody, font=(Bfont), value = val, text= B_text, bg=back_Color, command= command, variable=var)
    btn.place(x = a, y = b)

CreatLable("Hour", 65, 70)      #Hours Configration
c_Hour = Combobox(framBody, width= 2, font= ('arial 15'))
c_Hour['values'] = hours_Values
c_Hour.current(0)
c_Hour.place(x= 65, y= 95)

CreatLable("Min", 120, 70)      #Minuts Configration
c_Min = Combobox(framBody, width= 2, font= ('arial 15')) 
c_Min['values'] = min_Values
c_Min.current(0)
c_Min.place(x= 120, y= 95)


CreatLable("Sec", 175, 70)      #Second Configration
c_Sec = Combobox(framBody, width= 2, font= ('arial 15')) 
c_Sec['values'] = Sec_Values
c_Sec.current(0)
c_Sec.place(x= 175, y= 95)

CreatLable("Period", 230, 70)      #period Configration
c_Period = Combobox(framBody, width= 3, font= ('arial 15')) 
c_Period['values'] = period_Values
c_Period.current(0)
c_Period.place(x= 230, y= 95)


def activeAlarm():
    indx = Thread(target= alarmTime)
    indx.start()
    
activeBtn = button('Activate', 80, 140, activeAlarm, 1)

def DeactiveAlarm():
    print("Deactivated Alarm: ", selected.get())
    mixer.music.stop()


def soundAlarm():
    mixer.music.load('music.mp3')
    mixer.music.play()
    selected.set(0)
    deactiveBtn = button('Deactivate', 180, 140, DeactiveAlarm, 2)


def alarmTime():
    while True:
        ctrl = selected.get()
        print(ctrl)
        
        now = datetime.now()
        
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")
        
        alarmHour = c_Hour.get()
        alarmMinute = c_Min.get()
        alarmSec = c_Sec.get()
        alarmPeriod = c_Period.get()
        alarmPeriod = str(alarmPeriod).upper()
        
        if ctrl == 1:
            if alarmPeriod == period:
                if alarmHour == hour:
                    if alarmMinute == minute:
                        if alarmSec == second:
                            print("Please Wake Up!!!!")
                            soundAlarm()
        sleep(1)


mixer.init()
window.mainloop()