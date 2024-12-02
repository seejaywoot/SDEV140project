'''
Author: CJ Root
Date: 11/27/2024
Program: tuningprogram.py
Version: 3.0
'''

from tkinter import *
import tkinter as tk
from tkinter import ttk
root = Tk()

#Shutoff title bar
root.overrideredirect(True)
#New window size
root.geometry('1000x600+600+600')
#Background color of title bar
backGround = '#333333'
#Background of window
contentColor = '#7f7f7f'
#New frame for title bar
titleBar = Frame(root, bg=backGround, relief='raised', bd=0)
#Create close button for title bar
closeButton = Button(titleBar, text='X', command=root.destroy,bg=backGround, padx=5, pady=2, activebackground='red', bd=0, font='bold', fg='white', activeforeground='white')
#Window title
titleWindow = 'Automotive Engine Tuning Program'
titleName = Label(titleBar, text=titleWindow, font='bold', bg=backGround, fg='white')
#Canvas for the main area of the window
window = Canvas(root, bg='#7f7f7f', highlightbackground='#333333', highlightthickness=4)
#Align the widgets for title bar
titleBar.pack(expand=0, fill=X)
titleName.pack(side=LEFT)
closeButton.pack(side=RIGHT)
window.pack(expand=1, fill=BOTH)
xAxis = None
yAxis = None

#Bind title bar motion to the move with the window 
def moveWindow(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def moveHovering(event):
    global closeButton
    closeButton['bg'] = 'red'

def returnNormal(event):
   global close_button
   closeButton['bg'] = backGround

titleBar.bind('<B1-Motion>', moveWindow)
closeButton.bind('<Enter>', moveHovering)
closeButton.bind('<Leave>', returnNormal)

#Labels inside main window
headerLabel = tk.Label(window, text='Welcome to our tuning program & thanks for choosing Root Tuning!', font = 'elephant 14 bold', bg = '#7f7f7f', fg = 'black')
headerLabel.place(x=130, y=5)
label1 = tk.Label(window, text='Displacement in Cubic Inches', font='kokila 12 bold', bg = '#7f7f7f')
label1.place(x=60, y=100)
label2 = tk.Label(window, text='Make of Engine', font='kokila 12 bold', bg = '#7f7f7f')
label2.place(x=350, y=100)
label3 = tk.Label(window, text='Firing Order', font='kokila 12 bold', bg = '#7f7f7f')
label3.place(x=575, y=100)
label4 = tk.Label(window, text='Number of Cylinders', font='kokila 12 bold', bg = '#7f7f7f')
label4.place(x=790, y=100)

#Create entry boxes
def numCylinders(event):                      
    label4 = numCyl.get()
   
def engineMake(event):
    label2 = engMake.get()

#Displacement in Cubic Inches Input
entry1 = tk.Entry(window, bg = 'white', highlightbackground='#333333', highlightthickness=2)
entry1.place(x=107, y=125)

#Make of Engine Input
options = ['BMW', 'Chevy', 'Cummins', 'Dodge', 'Ford', 'Honda', 'Jeep', 'Kia', 'Mazda', 'Nissan', 'Toyota', 'VW', 'Yamaha', 'Other']
engMake = tk.StringVar()
frame = tk.Frame(window, width=69, height=25, highlightbackground='#333333', highlightthickness=2)
frame.place(x=378, y=123)
entry2 = ttk.Combobox(window, width=7, height=10, textvariable=engMake, values=options)
entry2.bind('<<ComboboxSelected>>', engineMake)
entry2.place(x=380, y=125)

#Firing Order Input
entry3 = tk.Entry(window, bg = 'white', highlightbackground='#333333', highlightthickness=2)
entry3.place(x=560, y=125)

#Cylinder Number Input
frame = tk.Frame(window, width=45, height=25, highlightbackground='#333333', highlightthickness=2)
frame.place(x=849, y=123)
entry4 = ttk.Combobox(window, width=3, height=10, values=list(range(1,9)))
entry4.bind('<<ComboboxSelected>>', numCylinders)
entry4.place(x=851, y=125)

#Create and open other windows, created the same way as main window.
def fuelingWindow():
    fuelingWindow = Toplevel(window)
    fuelingWindow.overrideredirect(True)
    fuelingWindow.geometry('400x300+300+300')
    backGround = '#333333'
    contentColor = '#7f7f7f'
    titleBar2 = Frame(fuelingWindow, bg=backGround, relief='raised', bd=0)
    closeButton = Button(titleBar2, text='X', command=fuelingWindow.destroy,bg=backGround, padx=5, pady=2, activebackground='red', bd=0, font='bold', fg='white', activeforeground='white')
    titleWindow2 = 'Fueling'
    titleName2 = Label(titleBar2, text=titleWindow2, font='bold', bg=backGround, fg='white')
    window2 = Canvas(fuelingWindow, bg='#7f7f7f', highlightbackground='#333333', highlightthickness=4)
    titleBar2.pack(expand=0, fill=X)
    titleName2.pack(side=LEFT)
    closeButton.pack(side=RIGHT)
    window2.pack(expand=1, fill=BOTH)
    xAxis = None
    yAxis = None

    def moveWindow2(event):
        fuelingWindow.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    
    def moveHovering2(event):
        global closeButton
        closeButton['bg'] = 'red'

    def returnNormal2(event):
        global closeButton
        closeButton['bg'] = backGround

    titleBar2.bind('<B1-Motion>', moveWindow2)
    closeButton.bind('<Enter>', moveHovering2)
    closeButton.bind('<Leave>', returnNormal2)

def airflowWindow():
    airflowWindow = Toplevel(window)
    airflowWindow.overrideredirect(True)
    airflowWindow.geometry('400x300+300+300')
    backGround = '#333333'
    contentColor = '#7f7f7f'
    titleBar3 = Frame(airflowWindow, bg=backGround, relief='raised', bd=0)
    closeButton = Button(titleBar3, text='X', command=airflowWindow.destroy,bg=backGround, padx=5, pady=2, activebackground='red', bd=0, font='bold', fg='white', activeforeground='white')
    titleWindow3 = 'Airflow'
    titleName3 = Label(titleBar3, text=titleWindow3, font='bold', bg=backGround, fg='white')
    window3 = Canvas(airflowWindow, bg='#7f7f7f', highlightbackground='#333333', highlightthickness=4)
    titleBar3.pack(expand=0, fill=X)
    titleName3.pack(side=LEFT)
    closeButton.pack(side=RIGHT)
    window3.pack(expand=1, fill=BOTH)
    xAxis = None
    yAxis = None

    def moveWindow3(event):
        airflowWindow.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    
    def moveHovering3(event):
        global closeButton
        closeButton['bg'] = 'red'

    def returnNormal3(event):
        global closeButton
        closeButton['bg'] = backGround

    titleBar3.bind('<B1-Motion>', moveWindow3)
    closeButton.bind('<Enter>', moveHovering3)
    closeButton.bind('<Leave>', returnNormal3)

def sparkWindow():
    sparkWindow = Toplevel(window)
    sparkWindow.overrideredirect(True)
    sparkWindow.geometry('400x300+300+300')
    backGround = '#333333'
    contentColor = '#7f7f7f'
    titleBar4 = Frame(sparkWindow, bg=backGround, relief='raised', bd=0)
    closeButton = Button(titleBar4, text='X', command=sparkWindow.destroy,bg=backGround, padx=5, pady=2, activebackground='red', bd=0, font='bold', fg='white', activeforeground='white')
    titleWindow4 = 'Spark'
    titleName4 = Label(titleBar4, text=titleWindow4, font='bold', bg=backGround, fg='white')
    window4 = Canvas(sparkWindow, bg='#7f7f7f', highlightbackground='#333333', highlightthickness=4)
    titleBar4.pack(expand=0, fill=X)
    titleName4.pack(side=LEFT)
    closeButton.pack(side=RIGHT)
    window4.pack(expand=1, fill=BOTH)
    xAxis = None
    yAxis = None

    def moveWindow4(event):
        sparkWindow.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    
    def moveHovering4(event):
        global closeButton
        closeButton['bg'] = 'red'

    def returnNormal4(event):
        global closeButton
        closeButton['bg'] = backGround

    titleBar4.bind('<B1-Motion>', moveWindow4)
    closeButton.bind('<Enter>', moveHovering4)
    closeButton.bind('<Leave>', returnNormal4)

#Buttons for clickable windows
button = tk.Button(root, text='Fueling', font='kokila 16 bold', command=fuelingWindow)
button.place(x=150, y=300)
button = tk.Button(root, text='Airflow', font='kokila 16 bold', command=airflowWindow)
button.place(x=440, y=300)
button = tk.Button(root, text='Spark', font='kokila 16 bold', command=sparkWindow)
button.place(x=750, y=300)

root.mainloop()
