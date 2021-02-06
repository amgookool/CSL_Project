import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
from functools import partial 


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()




class Page1(Page):
   def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=11280)
        
        load = Image.open("homepagepic.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        
      
       
       


class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #label = tk.Label(self, text="This is page 2")
       #label.pack(side="top", fill="both", expand=True)
       #test

       p1 = Page1(self)
       p3 = Page3(self)
       p4 = Page4(self)
       p5 = Page5(self)
       p6 = Page6(self)
       p7 = Page7(self)

       buttonframe = tk.Frame(self)
       container = tk.Frame(self)
       buttonframe.pack(side="top", fill="x", expand=False)
       container.pack(side="top", fill="both", expand=True)

       p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
       #test 
      # tk.Frame.__init__(self, *args, **kwargs)
       #container = tk.Frame(self)
       #p4 = Page4(self)
    
       def pr():
           p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
           return

       #container.pack(side="bottom", fill="both", expand=True)
 
       #TopFrame
       #buttonframe = tk.Frame(self)
       #buttonframe.pack(side="top", fill="x", expand=False)

       #BottomFrame
       buttonframe1 = tk.Frame(self)
       buttonframe1.pack(side="top", fill="x", expand=False)
    
       b = Button( buttonframe, text='Add Record',command=p4.lift)  
       b.pack(side="left",pady=2, padx=2)

       b2 = Button(buttonframe, text='Edit Record',command=p5.lift) 
       b2.pack(side="left",pady=2, padx=2)

       b3 = tk.Button(buttonframe, text='Remove Record',command=p6.lift) 
       b3.pack(side="left",pady=2, padx=2)

       b4 =tk.Button(buttonframe, text='Records',command=p7.lift) 
       b4.pack(side="left",pady=2, padx=2)


      # b4 = tk.Button( buttonframe, text='return',command=p6.lift) 
      # b4.pack(side="top",)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)
  


#addrecord
class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       tk.Frame.__init__(self, *args, **kwargs)
       
       #label = tk.Label(self, text="This is page 4")
       #label.pack(side="top", fill="both", expand=True)
       buttonframe = tk.Frame(self)
       buttonframe.pack(side="top", fill="x",  expand=False)
       buttonframe1 = tk.Frame(self)
       buttonframe1.pack(side="bottom", fill="x", expand=False)
        #string variables 

       x1 = StringVar()
       x2 = StringVar()
       x3 = StringVar()
       x4 = StringVar()
       x5 = StringVar()
       def repord(lable,x1,x2,x3,x4):
           Name = (x1.get())
           Age  = (x2.get())
           Sex  = (x3.get())
           Date = (x4.get())
           Time = (x5.get())
           return


        #SEARCH BAR1
       l1 = Label( buttonframe,text='Name:')
       l1.pack(side="left", pady=10, padx=10)
       e1 = Entry( buttonframe,textvariable=x1)
       e1.pack(side="left", pady=10, padx=10)

        #SEARCH BAR2
       l2 = Label( buttonframe,text='Age:')
       l2.pack(side="left", pady=10, padx=10)
       e2 = Entry( buttonframe,textvariable=x2)
       e2.pack(side="left", pady=10, padx=10)

        #SEARCH BAR3
       l3 = Label( buttonframe,text='Sex:')
       l3.pack(side="left", pady=10, padx=10)
       e3 = Entry( buttonframe,textvariable=x3)
       e3.pack(side="left", pady=10, padx=10)

       #SEARCH BAR4
       l4 = Label( buttonframe,text='Date:')
       l4.pack(side="left", pady=40, padx=10)
       e4 = Entry( buttonframe,textvariable=x4)
       e4.pack(side="left", pady=10, padx=10)

        #SEARCH BAR5
       l5 = Label( buttonframe,text='Time:')
       l5.pack(side="left", pady=40, padx=10)
       e5 = Entry( buttonframe,textvariable=x5)
       e5.pack(side="left", pady=10, padx=10)

       lable = Label( buttonframe)
       lable.pack(side="left", pady=10, padx=10)

       b = Button( buttonframe1, text='Complete')  
       b.pack(side="bottom")

#EDIT rECORDS PAGE 
class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is the edit records page")
       label.pack(side="top", fill="both", expand=True)

#rEMOVE rECORDS PAGE 
class Page6(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is the REMOVE records page")
       label.pack(side="top", fill="both", expand=True)

# rECORDS PAGE 
class Page7(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
      # label = tk.Label(self, text="This is the records page")
     #  label.pack(side="top", fill="both", expand=True)
       buttonframe = tk.Frame(self)
       buttonframe.pack(side="top", fill="x",  expand=False)
          #search bar
       x1 = StringVar()
       x2 = StringVar()
        #SEARCH BAR1
       l1 = Label( buttonframe,text='Patient name:')
       l1.pack()
       e1 = Entry( buttonframe,textvariable=x1)
       e1.pack()

        #SEARCH BAR2
       l2 = Label( buttonframe,text='ID no:')
       l2.pack()
       e2 = Entry( buttonframe,textvariable=x2)
       e2.pack()
       lable = Label( buttonframe)
       lable.pack()




class MainView(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        

        photo = PhotoImage(file = r"C:\Users\Joshua.M.Rampersad\Desktop\elec\ECNG 2005\Project csl\test interentcode\369-3699390_notification-png-notification-icon-png-free-clipart.png") 
        photoimage = photo.subsample(3, 3) 
        b1 = tk.Button(buttonframe, text="Home", command=p1.lift,pady=0,padx=2,font=("Courier", 14, 'bold'))
        b2 = tk.Button(buttonframe, text="Records", command=p2.lift,pady=0,padx=2,font=("Courier", 14, 'bold'))
        b3 = tk.Button(buttonframe, text="Notifications",command=p3.lift,pady=0,padx=2,font=("Courier", 14, 'bold'))
        b4 = tk.Button(buttonframe, text="Add A New Record",command=p4.lift,pady=0,padx=2,font=("Courier",14, 'bold'))
        b5 = tk.Button(buttonframe, text="Edit Records",command=p5.lift,pady=0,padx=2,font=("Courier",14, 'bold'))


        L5 = Label(buttonframe,text='MCSC',font=("Courier", 30, 'bold'))
        L5.pack(side="left", pady=5, padx=10)
        
        #Notifications
        b3.pack(side="right",padx=10)
        #editrecord
       # b5.pack(side="right",pady=5,padx=10)
        #Add A New Record
       # b4.pack(side="right",pady=5,padx=10)
         #Recordsbutton
        b2.pack(side="right",padx=10)
         #Home button
        b1.pack(side="right",padx=10)
        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1280x720")
    root.title('MCSC')
    #home = Page1(root)
    #canvas = Canvas(home, width =1920, height=300)
    #canvas.pack(  side="top", fill="both", expand=True)
    #my_image= PhotoImage(file='C:\\Users\\Joshua.M.Rampersad\\Desktop\\elec\\ECNG 2005\\Project csl\\test interentcode\\3.png')
    # image = image.my_resize(450, 350)
    # canvas.create_image(0,0, anchor=NW,image= my_image) 
    root.mainloop()  