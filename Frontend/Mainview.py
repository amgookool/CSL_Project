import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
from functools import partial 


class MainView(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        

        photo = PhotoImage(file = r"C:\Users\Joshua.M.Rampersad\Desktop\elec\ECNG 2005\Project csl\test interentcode\369-3699390_notification-png-notification-icon-png-free-clipart.png") 
        photoimage = photo.subsample(3, 3) 
        b1 = tk.Button(buttonframe, text="Home", command=p1.lift,pady=0,padx=2,font=("Courier", 14, 'bold'))
        b2 = tk.Button(buttonframe, text="Records", command=p2.lift,pady=0,padx=2,font=("Courier", 14, 'bold'))
        b3 = tk.Button(buttonframe, text="Notifications",command=p3.lift,pady=0,padx=2,font=("Courier", 14, 'bold'))
        b4 = tk.Button(buttonframe, text="Add A New Record",command=p4.lift,pady=0,padx=2,font=("Courier",14, 'bold'))
        b5 = tk.Button(buttonframe, text="Edit Records",command=p5.lift,pady=0,padx=2,font=("Courier",14, 'bold'))


        L5 = Label(buttonframe,text='MCSC',font=("Courier", 30, 'bold'))
        L5.pack(side="left", pady=5, padx=10)
        
        #Notifications
        b3.pack(side="right",padx=10)
        #editrecord
       # b5.pack(side="right",pady=5,padx=10)
        #Add A New Record
       # b4.pack(side="right",pady=5,padx=10)
         #Recordsbutton
        b2.pack(side="right",padx=10)
         #Home button
        b1.pack(side="right",padx=10)
        p1.show()
