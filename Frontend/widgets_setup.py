#This module is for placing the GUI entities into the window_setup python file
from .resources import *
import tkinter as tk

search_bar_titles = [
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


class search_bars:
    def __init__(self, window_name):
        search_frame = tk.Frame(window_name)
        search_frame.pack()
        #Search bar 1
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[0])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 2
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[1])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 3
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[2])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 4
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[3])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 5
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[4])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 6
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[5])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 7
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[6])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 8
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[7])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 9
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[8])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 10
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[9])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 11
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[10])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
        #Search bar 12
        self.label_fname = tk.Label(master=window_name, text=search_bar_titles[11])
        self.entry_fname = tk.Entry(master=window_name)
        self.label_fname.pack(side="left", padx=5, pady=5)
        self.entry_fname.pack(side="left", padx=5, pady=5)
