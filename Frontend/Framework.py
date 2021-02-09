# This python module sets up the pages and the main view window
import tkinter as tk
from tkinter import ttk
import PIL.ImageTk as  ImageTk
from PIL import Image 
from Frontend.Pages import *




class MainWindow: #Creating the window class which contains all of our frames(Framework Python File)...we would set the sizing of the frames here 
    def __init__(self, main_window):
        self.main_window = main_window #initializing the window from when we passed the tkinter window variable in our main.py
        main_window.title("Motherly Care Database System") # setting window title
        main_window.geometry("1920x1080") #setting the window size
        # main_window.iconbitmap("") #specifies the icon for window title (put all images in the resources folder)
        
        #Navigation bar which holds all of our pages(Pages python file) 
        self.nav_bar = ttk.Notebook(main_window) #instantiating the navigation bar 
        self.nav_bar.pack() #packing the nav bar into the window
        
        self.home_page = HomePage(self.nav_bar) #creating the home page using the HomePage class (Pages Python File)
        self.home_page.config(width=1920, height=1080) # setting the size of the home page on the window
        self.home_page.pack() #packing the home page into the Navigation bar 
        
        self.record_page = RecordPage(self.nav_bar) #creating the records page using the RecordsPage class (Pages Python File)
        self.record_page.config(width=1920, height=1080) # setting the size of the record page on the window
        self.record_page.pack()#packing the home page into the Navigation bar
        
        self.notify_page = NotifyPage(self.nav_bar)
        self.home_page.config(width=1920, height=1080) # setting the size of the notifications page on the window
        self.notify_page.pack()#packing the home page into the Navigation bar
        
        
        
        self.nav_bar.add(self.home_page,text="Home") # adding the home page to the navigation bar
        self.nav_bar.add(self.record_page,text="Records") # adding the records page to the navigation bar
        self.nav_bar.add(self.notify_page,text="Notifications") # adding the notifications page to the navigation bar
        
        
            



