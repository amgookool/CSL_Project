# This python module will be the middle man between the frontend and backsend of the app
import tkinter as tk

from Frontend.window_setup import *

root_view = tk.Tk()

main_window = MainWindow(root_view) # passing the root view window to execute the class properties of MainWindow which contains buttons,labels,etc to the window when running

#Interface with the Database here





root_view.mainloop()  # runs the window