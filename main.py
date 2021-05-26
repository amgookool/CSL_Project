import tkinter as tk
from Config.Database import *
from Config.Framework import *

root_view = tk.Tk()  #Creating the GUI window

main_window = MainWindow(root_view)  # loading the main window

#Interface with the Database here

root_view.mainloop()  # runs the window until user closes the program
