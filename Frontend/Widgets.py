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


class search_bar_widget: #Creating the search bar widget which is a frame that hold a label and entry tkinter class
    #initializing includes passing the frame as well as the sizing for the label and entry classes that are within the frame
    def __init__(self,frame=type(tk.Frame),bar_name=type(str),lbl_side=type(str),lbl_padx=type(int),lbl_pady=type(int),entr_side=type(str),entr_padx=type(int),entr_pady=type(int)):
        search_box_frame = tk.Frame(frame) #initalizing the search_box_frame that will be part of the parent frame
        search_box_frame.pack()#packing the search box in the frame that was passed  
        label = tk.Label(master=frame, text=bar_name) #adding a label to the search bar using the title passed as input for text
        entry = tk.Entry(master=frame) #adding an entry to the search bar using the title passed as input for text
        label.pack(side=lbl_side, padx=lbl_padx, pady=lbl_pady) #packing the label into the parent frame
        entry.pack(side=entr_side, padx=entr_padx,pady=entr_pady) #packing the entry field into the parent frame
          

class search_bar_frame: # this frame holds all the search bar widget frames that we want to create
    def __init__(self, window_name): #initialize the class and we want to pass the window/frame that we are loading the search bar frame to
        frame = tk.Frame(window_name) #creating the frame that hold the entries
        frame.pack() #packing the frame on the application
        #the following are the data labels and their fields 
        self.first_name = search_bar_widget(frame,titles[0],"left",13,10,"left",10,10)
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
        

