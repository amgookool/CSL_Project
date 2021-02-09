#This module will be used to create the callable functions from the buttons and will be the buffer between data sendding and receiving data from backend
import tkinter as tk
import tkinter.messagebox as MessageBox




def btn_func(): # the function that was assigned to the button that was created in the notify page
    print("this is the button function that executes in the command line")
    MessageBox.showinfo("Hello World!","This is an Error Box")
    