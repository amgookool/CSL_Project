import tkinter as tk
from tkinter import ttk
from Frontend.Widgets import *
from Frontend.Functions import *
class HomePage(tk.Frame): # Creating the Home Page which inherits the tk.Frame class which can contain labels,images,buttons,etc
  def __init__(self,note_frame=None): #initializing the Home Page class,self keyword is used to specify that the Homepage class has all these items(buttons,labels,etc)
    tk.Frame.__init__(self,note_frame)  #initializing the tk.Frame class so the Home page class can be the the tk.Frame
    self.note_frame = note_frame #specifying that the tk.Frame class is its own master(parent)
    self.pack(fill="both",expand=1) #packing the class to whatever window is initialized
    
    #loading the homepage image 
    self.load= Image.open("resources/homepagepic.jpg") #searching for the image using the string path 
    self.render =ImageTk.PhotoImage(self.load) #rendering the image to the home page
    self.img = tk.Label(self,image=self.render) #assigning the image to a tkinter label 
    self.img.place(x=0,y=0) #placement of the image in the window
    
    



class RecordPage(tk.Frame):# Creating the Records Page which inherits the tk.Frame class which can contain labels,images,buttons,etc
  def __init__(self,note_frame=None): #initializing the Record Page class,self keyword is used to specify that the Homepage class has all these items(buttons,labels,etc)
    tk.Frame.__init__(self,note_frame) #initializing the tk.Frame class so the Home page class can be the the tk.Frame
    self.note_frame = note_frame #specifying that the tk.Frame class is its own master(parent)
    
    
    self.search_frame = search_bar_frame(self) #Creating the search bar frame using the search_bar_frame class(Widgets Python file)
    



class NotifyPage(tk.Frame): # Creating the Records Page which inherits the tk.Frame class which can contain labels,images,buttons,etc
  def __init__(self,note_frame=None): #initializing the Record Page class,self keyword is used to specify that the Homepage class has all these items(buttons,labels,etc)
    tk.Frame.__init__(self,note_frame) #initializing the tk.Frame class so the Home page class can be the the tk.Frame
    self.note_frame = note_frame #specifying that the tk.Frame class is its own master(parent)
    
    self.message = tk.Label(self,text="This is a message") 
    self.message.pack()
    self.button = tk.Button(self,text="Click Me!",command=btn_func) #this button uses the self.button to call a function upon pressing it 
    self.button.pack()
    
  
  
 
 
 
    
    