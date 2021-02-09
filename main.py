import tkinter as tk

from Frontend.Framework import *

root_view = tk.Tk() #Creating the GUI window

main_window = MainWindow(root_view) # passing the root view window into the main view class to  execute all properties of MainWindow which contains frames,buttons,labels,etc to the window when running

#Interface with the Database here





root_view.mainloop()  # runs the window until user closes the program