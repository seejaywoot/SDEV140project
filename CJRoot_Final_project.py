'''
Author: CJ Root
Date: 12/13/2024
Program: tuningprogram.py
Version: 7.0
'''

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from PIL import Image,ImageTk
root = tk.Tk()

#Design of Custom GUI Window
root.overrideredirect(True)         #Shutoff title bar
root.geometry('1000x600+600+600')    #New window size
backGround = '#333333'            #Background color of title bar
contentColor = '#7f7f7f'        #Background color of window
titleBar = Frame(root, bg=backGround, relief='raised', bd=0)    #New frame for title bar
closeButton = Button(titleBar, text='X', command=root.destroy, bg=backGround, 
                     padx=5, pady=2, activebackground='red', bd=0, 
                     font='bold', fg='white', activeforeground='white')     #Create close button for title bar
titleWindow = 'Automotive Engine Tuning Program'      #Window title
titleName = Label(titleBar, text=titleWindow, font='bold', bg=backGround, fg='white')
window = Canvas(root, bg='#7f7f7f', highlightbackground='#333333', highlightthickness=4)    #Canvas for the main area of the window
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
#Build the Frame to Display Output Info
frame = tk.Frame(window, width=800, height=200, bg='#7f7f7f', highlightbackground='#333333', highlightthickness=5)
frame.place(x=105, y=350)

#Create entry boxes
def engineMake(event):
    engMake = entry2.get()
    
def numCylinders(event):                      
    numCylinders = entry4.get()

#Displacement in Cubic Inches Input
def validateDisInput(P):        #Validate only numbers can be inputed and a certain amount
        if P == "" or P.isdigit() and len(P) <= 3 and int(P) <= 900:
            return True
        return False

vcmd = (window.register(validateDisInput), '%P')
entry1 = tk.Entry(window, bg = 'white', highlightbackground='#333333', highlightthickness=2, validate='key', validatecommand=vcmd)
entry1.place(x=107, y=125)

#Make of Engine Input
options = ['BMW', 'Chevy', 'Cummins', 'Dodge', 'Ford', 'Honda', 'Jeep', 'Kia', 'Mazda', 'Nissan', 'Toyota', 'VW', 'Yamaha', 'Other']
frame = tk.Frame(window, width=69, height=25, highlightbackground='#333333', highlightthickness=2)
frame.place(x=378, y=123)
entry2 = ttk.Combobox(window, width=7, height=10, textvariable=engineMake, values=options,state='readonly')
entry2.bind('<<ComboboxSelected>>', engineMake)
entry2.place(x=380, y=125)

#Firing Order Input
def validateFireInput(P):       #Validate only numbers can be inputed and a certain amount and one of each number
        if P == "" or P.isdigit() and 1 <= len(P) <= 8:
            if all(char in '12345678' for char in P) and len(P) == len(set(P)):
                return True
        return False
    
vcmd = (window.register(validateFireInput), '%P')
entry3 = tk.Entry(window, bg = 'white', highlightbackground='#333333', highlightthickness=2, validate='key', validatecommand=vcmd)
entry3.place(x=560, y=125)

#Cylinder Number Input
frame = tk.Frame(window, width=45, height=25, highlightbackground='#333333', highlightthickness=2)
frame.place(x=849, y=123)
entry4 = ttk.Combobox(window, width=3, height=10, values=list(range(1,17)),state='readonly')
entry4.bind('<<ComboboxSelected>>', numCylinders)
entry4.place(x=851, y=125)
    
def mainMessage():      #Retrieving data to output
    engMessage = entry2.get()
    displaceMessage = entry1.get()
    cylnumMessage = entry4.get()
    firingMessage = entry3.get()
    label15.config(text='Your '+cylnumMessage+' cylinder '+ engMessage +' engine has a displacement of '+ displaceMessage +' cubic inches with a firing order of '+ firingMessage+'.', font='kokila 10 bold', bg = '#7f7f7f')
    

def checkEntries(*args):   #Checks to make sure there is an entry for ever input on main window before button is turned on to submit info 
    if entry1.get() and entry2.get() and entry3.get() and entry4.get():
        submitButton.config(state=tk.NORMAL)
    else:
        submitButton.config(state=tk.DISABLED)

entry1.bind('<KeyRelease>', checkEntries)
entry2.bind('<<ComboboxSelected>>', checkEntries)
entry3.bind('<KeyRelease>', checkEntries)
entry4.bind('<<ComboboxSelected>>', checkEntries)
submitButton = tk.Button(window, text="Submit",font='kokila 14 bold', command=mainMessage, state=tk.DISABLED)
submitButton.config(command=lambda: [mainMessage(), enableDownloadButton()])
submitButton.place(x=440, y=180)
checkEntries()
label15 = tk.Label(window, text='',bg='#7f7f7f')
label15.place(x=120, y=360)

#Images to display and position correctly
image = Image.open('crank.png')  
image = image.resize((100, 100), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
imageLabel = tk.Label(window, image=photo, bg='#7f7f7f')
imageLabel.image = photo
imageLabel.place(x=20, y=170)
image2 = Image.open('engine.png')
image2 = image2.resize((100, 100), Image.LANCZOS)
photo2 = ImageTk.PhotoImage(image2)
imageLabel2 = tk.Label(window, image=photo2, bg='#7f7f7f')
imageLabel2.image = photo2
imageLabel2.place(x=870, y=170) 

#Create and open other windows, created the same way as main window.

def fuelingWindow():    #Window for the fueling input
    fuelingWindow = Toplevel(window)
    fuelingWindow.overrideredirect(True)
    fuelingWindow.geometry('400x300+300+300')
    backGround = '#333333'
    contentColor = '#7f7f7f'
    titleBar2 = Frame(fuelingWindow, bg=backGround, relief='raised', bd=0)
    closeButton = Button(titleBar2, text='X', command=fuelingWindow.destroy, 
                     bg=backGround, padx=5, pady=2, activebackground='red', 
                     bd=0, font='bold', fg='white', activeforeground='white')
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
    #Inputs for fueling info 
    #Inputs number of injectors on the engine
    label5 = tk.Label(window2, text='Number of Injectors', font='kokila 12 bold', bg = '#7f7f7f')
    label5.place(x=25, y=25)
    def numInjectors(event):
        numInjectors = entry5.get()
    
    frame = tk.Frame(window2, width=45, height=25, highlightbackground='#333333', highlightthickness=2)
    frame.place(x=250, y=25)
    entry5 = ttk.Combobox(window2, width=3, height=10, values=list(range(1,9)),state='readonly')
    entry5.bind('<<ComboboxSelected>>', numInjectors)
    entry5.place(x=252, y=27)
    #Inputs the size of the injectors
    def validateInjInput(P):        #Validate only numbers can be inputed and a certain amount
        if P == "" or P.isdigit() and len(P) <= 3 and int(P) <= 500:
            return True
        return False
    
    vcmd = (window2.register(validateInjInput), '%P')
    label6 = tk.Label(window2, text='Size of Injectors in lbs', font='kokila 12 bold', bg = '#7f7f7f')
    label6.place(x=25, y=75)
    entry6 = tk.Entry(window2, bg = 'white', highlightbackground='#333333', highlightthickness=2, validate='key', validatecommand=vcmd)
    entry6.place(x=225, y=75)
    #Inputs the fuel pressure needed at fuel rail
    def validatePSIinput(P):        #Validate only numbers can be inputed and a certain amount
        if P == "" or P.isdigit() and len(P) <= 5 and int(P) <= 90000:
            return True
        return False
    
    vcmd = (window2.register(validatePSIinput), '%P')
    label7 = tk.Label(window2, text='Fuel PSI at Rail', font='kokila 12 bold', bg = '#7f7f7f')
    label7.place(x=25, y=125)
    entry7 = tk.Entry(window2, bg = 'white', highlightbackground='#333333', highlightthickness=2, validate='key', validatecommand=vcmd)
    entry7.place(x=225, y=125)

    def mainMessage2():     #Displays the message in the main window of inputed information
        injMessage = entry5.get()
        injSizeMessage = entry6.get()
        fuelPsiMessage = entry7.get()
        label16.config(text='Your fuel table will adjust for having ' + injMessage + 
                ' injectors at a pressure of ' + fuelPsiMessage + 
                ' psi and injectors running at ' + injSizeMessage + ' lbs.', 
                font='kokila 10 bold', bg='#7f7f7f')
    def checkEntries(*args):    #Checks to make sure there is an entry for ever input on fueling Window before button is turned on to submit info
        if entry5.get() and entry6.get() and entry7.get():
            submitButton2.config(state=tk.NORMAL)
        else:
            submitButton2.config(state=tk.DISABLED)
    
    def closeWindow2():     #Closes window once submit is clicked
        fuelingWindow.destroy()
        
    entry5.bind('<<ComboboxSelected>>', checkEntries)
    entry6.bind('<KeyRelease>', checkEntries)
    entry7.bind('<KeyRelease>', checkEntries)
    submitButton2 = tk.Button(window2, text="Submit", command=mainMessage2, state=tk.DISABLED)
    submitButton2.config(command=lambda: [mainMessage2(), enableDownloadButton(), closeWindow2()])
    submitButton2.place(x=330, y=160)
    checkEntries()
    
    #Image to display and position correctly
    image = Image.open('fuelInjector.png')  
    image = image.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    imageLabel = tk.Label(window2, image=photo, bg='#7f7f7f')
    imageLabel.image = photo  
    imageLabel.place(x=45, y=150)

#Label to display in main window   
label16 = tk.Label(window, text='',bg='#7f7f7f')
label16.place(x=120, y=385)    
    
def airflowWindow():    #Window for the idle and airlow input
    airflowWindow = Toplevel(window)
    airflowWindow.overrideredirect(True)
    airflowWindow.geometry('400x300+300+300')
    backGround = '#333333'
    contentColor = '#7f7f7f'
    titleBar3 = Frame(airflowWindow, bg=backGround, relief='raised', bd=0)
    closeButton = Button(titleBar3, text='X', command=airflowWindow.destroy, bg=backGround, 
                     padx=5, pady=2, activebackground='red', bd=0, font='bold', 
                     fg='white', activeforeground='white')
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
    ##Inputs for Airflow info 
    #Inputs throttle body size on the engine
    def validateTsizeInput(P):      #Validate only numbers can be inputed and a certain amount
        if P == "" or P.isdigit() and len(P) <= 3 and int(P) <= 250:
            return True
        return False
    
    vcmd = (window3.register(validateTsizeInput), '%P')
    label8 = tk.Label(window3, text='Throttle body size in MM', font='kokila 12 bold', bg = '#7f7f7f')
    label8.place(x=20, y=65)
    entry8 = tk.Entry(window3, bg = 'white', highlightbackground='#333333', highlightthickness=2, validate='key', validatecommand=vcmd)
    entry8.place(x=220, y=65)
    #Inputs mass air flow hertz scale for the mass air flow to know how much air is being pulled into engine
    label9 = tk.Label(window3, text='Mass Air Flow Hertz Scale', font='kokila 12 bold', bg = '#7f7f7f')
    label9.place(x=20, y=20)
    
    def mafAir(event):
        mafAir = entry9.get()
           
    frame = tk.Frame(window3, width=57, height=25, highlightbackground='#333333', highlightthickness=2)
    frame.place(x=245, y=20)
    entry9 = ttk.Combobox(window3, width=5, height=10, values=list(range(14000,18001, 50)),state='readonly')
    entry9.bind('<<ComboboxSelected>>', mafAir)
    entry9.place(x=247, y=22)
    #Inputs the max RPM the user would like
    def validateRPMinput(P):        #Validate only numbers can be inputed and a certain amount and to a certain range
        if P == "" or P.isdigit() and len(P) <= 5 and int(P) <= 14999:
            return True
        return False
    
    vcmd = (window3.register(validateRPMinput), '%P')
    label10 = tk.Label(window3, text='Max RPM', font='kokila 12 bold', bg = '#7f7f7f')
    label10.place(x=20, y=105)
    entry10 = tk.Entry(window3, bg = 'white', highlightbackground='#333333', highlightthickness=2, validate='key', validatecommand=vcmd)
    entry10.place(x=220, y=105)
    #Inputs the idle range the user would like
    def validateIdleRinput(P):      #Validate only numbers can be inputed and a certain amount and to a certain range
        if P == "" or (P.isdigit() and len(P) <= 4 and int(P) <= 1999):
            return True
        return False
    
    vcmd = (window3.register(validateIdleRinput), '%P')
    label11 = tk.Label(window3, text='Desired Idle Range', font='kokila 12 bold', bg = '#7f7f7f')
    label11.place(x=20, y=145)
    entry11 = tk.Entry(window3, bg = 'white', highlightbackground='#333333', highlightthickness=2, validate='key', validatecommand=vcmd)
    entry11.place(x=220, y=145)
    
    def mainMessage3():     #Displays the message in the main window of inputed information
        tbSizeMessage =entry8.get()
        mafMessage = entry9.get()
        rpmMessage = entry10.get()
        idleMessage = entry11.get()
        label17.config(text= 'Your idle will be set at '+idleMessage+' RPM with a range of +/- 50RPM and a redline RPM of '+rpmMessage+',\n' 
                 'and the ECU will factor your airflow from your throttle body size of '+tbSizeMessage+'mm, and MAF hertz at '+mafMessage+'.', 
                 font='kokila 10 bold', bg = '#7f7f7f') 
    def checkEntries(*args):        #Checks to make sure there is an entry for ever input on airflow Window before button is turned on to submit info
        if entry8.get() and entry9.get() and entry10.get() and entry11.get():
            submitButton3.config(state=tk.NORMAL)
        else:
            submitButton3.config(state=tk.DISABLED)

    def closeWindow3():     #Closes window once submit is clicked
        airflowWindow.destroy()
        
    entry8.bind('<KeyRelease>', checkEntries)
    entry9.bind('<<ComboboxSelected>>', checkEntries)
    entry10.bind('<KeyRelease>', checkEntries)
    entry11.bind('<KeyRelease>', checkEntries)
    submitButton3 = tk.Button(window3, text="Submit", command=mainMessage3, state=tk.DISABLED)
    submitButton3.config(command=lambda: [mainMessage3(), enableDownloadButton(), closeWindow3()])
    submitButton3.place(x=330, y=215)
    checkEntries()
    
    #Image to display and position correctly
    image = Image.open('airflow.png')  
    image = image.resize((80, 80), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    imageLabel = tk.Label(window3, image=photo, bg='#7f7f7f')
    imageLabel.image = photo  
    imageLabel.place(x=75, y=170)

#Label to display in main window 
label17 = tk.Label(window, text='',bg='#7f7f7f')
label17.place(x=120, y=405)

def sparkWindow():      #Window for the timing input
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
    #Inputs for timing info 
    #Inputs idle timing the user would like on the engine
    def idleTiming(event):
        idleTiming = entry12.get()
    
    label12 = tk.Label(window4, text='Timing at Idle', font='kokila 12 bold', bg = '#7f7f7f')
    label12.place(x=25, y=25)  
    frame = tk.Frame(window4, width=51, height=25, highlightbackground='#333333', highlightthickness=2)
    frame.place(x=250, y=25)
    entry12 = ttk.Combobox(window4, width=4, height=10, values=list(range(15,26)), state='readonly')
    entry12.bind('<<ComboboxSelected>>', idleTiming)
    entry12.place(x=252, y=27)
    #Inputs cruise timing the user would like on the engine
    def cruiseTiming(event):
        cruiseTiming = entry13.get()
    
    label13 = tk.Label(window4, text='Timing at Cruise', font='kokila 12 bold', bg = '#7f7f7f')
    label13.place(x=25, y=75)  
    frame = tk.Frame(window4, width=51, height=25, highlightbackground='#333333', highlightthickness=2)
    frame.place(x=250, y=75)
    entry13 = ttk.Combobox(window4, width=4, height=10, values=list(range(25,41)), state='readonly')
    entry13.bind('<<ComboboxSelected>>', cruiseTiming)
    entry13.place(x=252, y=77)
    #Inputs wide open throttle timing the user would like on the engine
    def wotTiming(event):
        wotTiming = entry14.get()
    
    label14 = tk.Label(window4, text='Timing at Wide Open Throttle', font='kokila 12 bold', bg = '#7f7f7f')
    label14.place(x=25, y=125)  
    frame = tk.Frame(window4, width=51, height=25, highlightbackground='#333333', highlightthickness=2)
    frame.place(x=250, y=125)
    entry14 = ttk.Combobox(window4, width=4, height=10, values=list(range(20,31)), state='readonly')
    entry14.bind('<<ComboboxSelected>>', wotTiming)
    entry14.place(x=252, y=127)
    
    def mainMessage4():     #Displays the message in the main window of inputed information
        idleTmessage =entry12.get()
        cruiseTmessage = entry13.get()
        wotTmessage = entry14.get()
        label18.config(text='Your timing table will be configured by the ECU with idle timing set at ' + idleTmessage + ', cruise timing set at ' + cruiseTmessage + ',\n' +
                'and wide open throttle timing at ' + wotTmessage + ', all in degrees of timing from 0 degrees TDC.', 
                font='kokila 10 bold', 
                bg='#7f7f7f')
    def checkEntries(*args):        #Checks to make sure there is an entry for ever input on airflow Window before button is turned on to submit info
        if entry12.get() and entry13.get() and entry14.get():
            submitButton4.config(state=tk.NORMAL)
        else:
            submitButton4.config(state=tk.DISABLED)

    def closeWindow4():     #Closes window once submit is clicked
        sparkWindow.destroy()
        
    entry12.bind('<<ComboboxSelected>>', checkEntries)
    entry13.bind('<<ComboboxSelected>>', checkEntries)
    entry14.bind('<<ComboboxSelected>>', checkEntries)
    submitButton4 = tk.Button(window4, text="Submit", command=mainMessage4, state=tk.DISABLED)
    submitButton4.config(command=lambda: [mainMessage4(), enableDownloadButton(), closeWindow4()])
    submitButton4.place(x=330, y=155)
    checkEntries()
    
    #Image to display and position correctly
    image = Image.open('sparkPlug.png')  
    image = image.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    imageLabel = tk.Label(window4, image=photo, bg='#7f7f7f')
    imageLabel.image = photo  
    imageLabel.place(x=45, y=150)
    
#Label to display in main window     
label18 = tk.Label(window, text='',bg='#7f7f7f')
label18.place(x=120, y=440)

def downloadWindow():       #Download to ECU window
    downloadWindow = Toplevel(window)
    downloadWindow.overrideredirect(True)
    downloadWindow.geometry('400x300+300+300')
    backGround = '#333333'
    contentColor = '#7f7f7f'
    titleBar5 = Frame(downloadWindow, bg=backGround, relief='raised', bd=0)
    closeButton = Button(titleBar5, text='X', command=downloadWindow.destroy,bg=backGround, padx=5, pady=2, activebackground='red', bd=0, font='bold', fg='white', activeforeground='white')
    titleWindow5 = 'Download Tune to ECU'
    titleName5 = Label(titleBar5, text=titleWindow5, font='bold', bg=backGround, fg='white')
    window5 = Canvas(downloadWindow, bg='#7f7f7f', highlightbackground='#333333', highlightthickness=4)
    titleBar5.pack(expand=0, fill=X)
    titleName5.pack(side=LEFT)
    closeButton.pack(side=RIGHT)
    window5.pack(expand=1, fill=BOTH)
    xAxis = None
    yAxis = None

    def moveWindow5(event):
        downloadWindow.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    
    def moveHovering5(event):
        global closeButton
        closeButton['bg'] = 'red'

    def returnNormal5(event):
        global closeButton
        closeButton['bg'] = backGround

    titleBar5.bind('<B1-Motion>', moveWindow5)
    closeButton.bind('<Enter>', moveHovering5)
    closeButton.bind('<Leave>', returnNormal5)

    global progress_var    #Progress bar for download and when completed window pops up for completion then close program
    def startDownload():
        for i in range(101):
            progressVar.set(i)
            window5.update_idletasks()
            window5.after(50)
        messagebox.showinfo('Download Complete', 'The download has been completed successfully, Thank you for using our tuning program!')   
        downloadWindow.destroy()
        root.destroy()
    progressVar = tk.IntVar()
    progressBar = ttk.Progressbar(window5, variable=progressVar, maximum=100)
    progressBar.pack(pady=20)
    downloadMessage = tk.Label(window5, text='PLEASE DO NOT UNHOOK DURING DOWNLOAD...', font='kokila 11 bold', fg='#FF91A4', bg='#7f7f7f')
    downloadMessage.pack(pady=10)
    startButton = tk.Button(window5, text='Start ECU Download', font='kokila 12 bold', command=startDownload)
    startButton.pack(pady=10)
    
    #Images to display
    image = Image.open('tuneCable.png')  
    image = image.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    imageLabel = tk.Label(downloadWindow, image=photo, bg='#7f7f7f')
    imageLabel.image = photo
    imageLabel.place(x=75, y=180)
    image2 = Image.open('ecu.png')
    image2 = image2.resize((100, 100), Image.LANCZOS)
    photo2 = ImageTk.PhotoImage(image2)
    imageLabel2 = tk.Label(downloadWindow, image=photo2, bg='#7f7f7f')
    imageLabel2.image = photo2
    imageLabel2.place(x=200, y=180) 
    
#Buttons for clickable windows in main window
button = tk.Button(root, text='Fueling', font='kokila 16 bold', command=fuelingWindow)
button.place(x=150, y=300)
button = tk.Button(root, text='Airflow', font='kokila 16 bold', command=airflowWindow)
button.place(x=440, y=300)
button = tk.Button(root, text='Spark', font='kokila 16 bold', command=sparkWindow)
button.place(x=750, y=300)
buttonD = tk.Button(root, text="Start Download", font='kokila 14 bold', command=downloadWindow, state=tk.DISABLED)
buttonD.place(x=405, y=530) 

#Validate that all 4 submit buttons are clicked before you can download to ECU
clickedButtons = 0
def enableDownloadButton():
    global clickedButtons
    clickedButtons += 1
    if clickedButtons == 4:
        buttonD.config(state=tk.NORMAL)

root.mainloop()