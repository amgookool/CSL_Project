# This python module sets up the pages and the main view window
import tkinter as tk
from tkinter import ttk
import PIL.ImageTk as  ImageTk
from PIL import Image 
from Frontend.Pages import *




class MainWindow:
    def __init__(self, main_window):
#initializing the window from when we passed the tkinter window variable in our main.py
        self.main_window = main_window
        main_window.title("Motherly Care Database System")
        main_window.geometry("1920x1080")
        # main_window.iconbitmap("") specifies the icon for window title
        self.nav_bar = ttk.Notebook(main_window)
        self.nav_bar.pack()
        self.home_page = HomePage(self.nav_bar)
        self.record_page = RecordPage(self.nav_bar)
        self.notify_page = NotifyPage(self.nav_bar)
        self.home_page.config(width=1920, height=1080)
        self.record_page.pack()
        self.home_page.pack()
        self.nav_bar.add(self.home_page,text="Home")
        self.nav_bar.add(self.record_page,text="Records")
        self.nav_bar.add(self.notify_page,text="Notifications")
        
        
            













#Setting the items(labels,buttons,entry,etc) into the window class       
       # self.label = tk.Label(main_window, text="This is our label")
        #self.label.pack()  # places label in the window
        #self.greet_button = tk.Button(main_window, text="Greet", command=self.greet)
        #self.greet_button.pack()  # places greet_button tk.button in the window
        #self.close_button = tk.Button(
        #    main_window, text="Close", command=main_window.quit
        #)
        #self.close_button.pack()
       
    def greet(self):
        print("Greetings!")





 



"""
  we have put the label and both buttons inside the main window, so they are the main window’s children in the tree. 
  We use the pack method on each widget to position it inside its parent
  the 'command' keyword parameter when constructing each button to specify the function which should handle each button’s click events – both of these functions are object methods.
  """
