import tkinter as tk
from tkinter import ttk
import PIL.ImageTk as ImageTk
from PIL import Image

titles = [
    "First Name:",
    "Last Name:",
    "Date of Birth:",
    "Sex:",
    "Driver's Permit Number:",
    "National ID Number:",
    "Passport Number:",
    "Next of Kin:",
    "Diagnosis:",
    "Intravenous Therapy",
    "Injections",
    "Insulin",
]


class search_bar_widget:
    def __init__(self,frame=type(tk.Frame),bar_name=type(str),lbl_side=type(str),lbl_padx=type(int),lbl_pady=type(int),entr_side=type(str),entr_padx=type(int),entr_pady=type(int)):
        search_box_frame = tk.Frame(frame)
        search_box_frame.pack()
        label = tk.Label(master=frame, text=bar_name)
        entry = tk.Entry(master=frame)
        label.pack(side=lbl_side, padx=lbl_padx, pady=lbl_pady)
        entry.pack(side=entr_side, padx=entr_padx,pady=entr_pady)
          

class search_bar_frame:
    def __init__(self, window_name):
        frame = tk.Frame(window_name)
        frame.pack()
        self.first_name = search_bar_widget(frame,titles[0],"left",10,10,"left",10,10)
        self.last_name = search_bar_widget(frame,titles[1],"left",10,10,"left",10,10)
        self.dob = search_bar_widget(frame,titles[2],"left",10,10,"left",10,10)
        self.sex = search_bar_widget(frame,titles[3],"left",10,10,"left",10,10)
        self.driverP = search_bar_widget(frame,titles[4],"left",10,10,"left",10,10)
        self.nat_id = search_bar_widget(frame,titles[5],"left",10,10,"left",10,10)
        self.passport = search_bar_widget(frame,titles[6],"left",10,10,"left",10,10)
        self.next_of_kin = search_bar_widget(frame,titles[7],"left",10,10,"left",10,10)
        self.diagnosis = search_bar_widget(frame,titles[8],"left",10,10,"left",10,10)
        self.therapy = search_bar_widget(frame,titles[9],"left",10,10,"left",10,10)
        self.injections = search_bar_widget(frame,titles[10],"left",10,10,"left",10,10)
        self.insulin= search_bar_widget(frame,titles[11],"left",10,10,"left",10,10)
        

