# This python module sets up the pages and the main view window
import tkinter as tk
from tkinter import ttk
import PIL.ImageTk as ImageTk
from PIL import Image
from Config.Widgets import *



class MainWindow:  # Creating the window class which contains all of our frames(Framework Python File)...we would set the sizing of the frames here
    def __init__(self, main_window):
        self.main_window = main_window  # initializing the window from when we passed the tkinter window variable in our main.py
        self.main_window.title("Motherly Care Database System")  # setting window title
        self.main_window.geometry("1920x1080")  # setting the window size

        self.nav_bar = ttk.Notebook(self.main_window)
        self.nav_bar.pack()
        
        self.homepage = HomePage(self.nav_bar)
        self.homepage.config(width = 1920, height = 1080)
        self.homepage.pack()
        
        self.recordpage = RecordPage(self.nav_bar)
        self.recordpage.config(width =1920, height = 1080)
        self.recordpage.pack()
        
        self.nav_bar.add(self.homepage, text = "Home")
        self.nav_bar.add(self.recordpage, text = "Records")

        
class HomePage(tk.Frame):
    def __init__(self,window_name = None):
        tk.Frame.__init__(self,window_name)
        self.pack(fill='both',expand=True)
        
        self.load_img = Image.open('Config/homepagepic.jpg')
        self.render = ImageTk.PhotoImage(self.load_img)
        self.img = tk.Label(self,image = self.render)
        self.img.pack(fill='both',expand=True)
        

class RecordPage(tk.Frame):
    def __init__(self,window_name = None):
        tk.Frame.__init__(self,window_name)
        self.pack(fill='both',expand = True)
        self.display_table = Display_Table(self)

        self.data_field = Patient_data_label(self)

        self.display_table.pack(side="top", fill="x")
        self.data_field.pack(side="bottom",fill="both")