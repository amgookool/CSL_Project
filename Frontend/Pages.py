import tkinter as tk
from tkinter import ttk
from Frontend.Widgets import *




def image_loader(self=type(tk.Frame),path=type(str),width=type(int),height=type(int)):
    self.pack(fill="both",expand=1)
    load = Image.open(path)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(self,image=render)
    return img.pack()




class HomePage(tk.Frame):
  def __init__(self,note_frame=None):
    tk.Frame.__init__(self,note_frame)
    self.note_frame = note_frame
    self.pack(fill="both",expand=11280)
    self.load= Image.open("resources/homepagepic.jpg")
    self.render =ImageTk.PhotoImage(self.load)
    self.img = tk.Label(self,image=self.render)
    self.img.place(x=0,y=0)
    
    
    




class RecordPage(tk.Frame):
  def __init__(self,note_frame=None):
    tk.Frame.__init__(self,note_frame)
    self.note_frame = note_frame
    self.search_frame = search_bar_frame(self)
    




class NotifyPage(tk.Frame):
  def __init__(self,note_frame=None):
    tk.Frame.__init__(self,note_frame)
    self.notify_frame = note_frame
 
 
 
 
 
 
    
    