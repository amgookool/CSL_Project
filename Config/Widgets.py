from textwrap import fill
import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, END
import PIL.ImageTk as ImageTk
from PIL import Image
from sqlalchemy.sql.expression import column, table, text
from Config.Functions import *
from Config.Database import Medhistory_Table, database_delete, insert_TMedhistory, insert_Tarrival, insert_Tpatient, patient_keys, medical_history_keys, home_arrival_keys


class Display_Table(tk.Frame):
    def __init__(self, window_name=None):
        record_data = display_table()  # data to show on table
        headings = record_data[0]
        record_data.pop(0)

        tk.Frame.__init__(self, window_name)
        self.table_frame = tk.Frame(window_name)

        # Creating style for table
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        self.table_scrollbar = tk.Scrollbar(self)
        self.table_scrollbar.pack(side="right", fill="y")

        # Creating the table
        self.table = ttk.Treeview(
            self, selectmode="browse", yscrollcommand=self.table_scrollbar.set
        )
        self.table.pack()
        self.table.bind("<B1-Motion>", "")
        # Configure scrollbar
        self.table_scrollbar.config(command=self.table.yview)

        # Setup of table columns
        self.table["columns"] = headings
        self.table.column("#0", width=0, stretch=False)  ##Phantom Column
        self.table.column("Patient ID", width=80, anchor="center")
        self.table.column("Name", width=200, anchor="center")
        self.table.column("Age", width=80, anchor="center")
        self.table.column("Medication", width=800, anchor="center")
        self.table.column("Emergency Contact", width=400, anchor="center")
        self.table.column("Emergency Contact Number", width=360, anchor="center")
        # Setup of table headings
        self.table.heading("#0", text="")  # phantom column
        self.table.heading("Patient ID", text=headings[0])
        self.table.heading("Name", text=headings[1])
        self.table.heading("Age", text=headings[2])
        self.table.heading("Medication", text=headings[3])
        self.table.heading("Emergency Contact", text=headings[4])
        self.table.heading("Emergency Contact Number", text=headings[5])
        
        self.update_button = tk.Button(self, text="Update Record", activebackground="grey")
        self.view_button = tk.Button(self,command=self.view_record, text="View Record", activebackground="grey")
        self.delete_button = tk.Button(self,command=self.delete_record, text="Delete Record", activebackground="grey")
        self.add_button = tk.Button(self,command = self.add_record, text="Add Record", activebackground="grey")
        self.clear_button = tk.Button(self, text="Clear fields", activebackground="grey")
        
        self.add_button.pack(side="left",anchor="ne")
        self.update_button.pack(side="left",anchor="ne")
        self.view_button.pack(side="left",anchor="ne")
        self.delete_button.pack(side="left",anchor="ne")
        self.clear_button.pack(side="left",anchor="ne")
        # displaying the records from database
        display_count = 1
        for records in record_data:
            self.table.insert(
                parent="",
                index="end",
                iid=display_count,
                text="",
                values=(records[0],records[1],records[2],records[3],records[4],records[5],),)
            display_count += 1
    
    def delete_record(self):
        selection = self.table.selection()[0]
        database_delete(selection)
        self.table.delete(selection)
    
    def view_record(self):
        selection = self.table.selection()[0]
        data = View_data_backend(int(selection))
        all_data = []
        patient_record = data[0]
        patient_medhistory = data[1]
        patient_arrival = data[2]
        patient_medhistory = patient_medhistory[2:]
        patient_arrival = patient_arrival[2:]
        all_data.append(patient_record)
        all_data.append(patient_medhistory)
        all_data.append(patient_arrival)
        name = str(patient_record[1] + ' ' + patient_record[2])
        self.toplevel_window = tk.Toplevel()
        self.toplevel_window.geometry('1920x1080')
        self.toplevel_window.title('Patient Record: {}'.format(name))
        self.data = View_Data_database(window_name = self.toplevel_window,data =all_data)

    def add_record(self):
        table_length =len(self.table.get_children())
        new_entry = table_length+1
        data = get_user_input_database(entry_id = new_entry)
        self.table.insert(parent = '',index = 'end',iid = new_entry,text='',values = (data[0],data[1],data[2],data[3],data[4],data[5],),)


class Patient_data_label(tk.LabelFrame):
    def __init__(self, window_name=None, text="Patient Data",bg='white'):
        tk.LabelFrame.__init__(self, window_name, text=text,bg=bg)
        self.pack(fill="both",expand=True)
        self.patient_info = Elder_Info_Frame(self)
        self.patient_info.pack(side="top",fill="both",expand=True)


class Elder_Info_Frame(tk.Frame):
    global in_patient_data
    in_patient_data = []
    global in_med_history
    in_med_history = []
    global in_home_arrival
    in_home_arrival=[]
    def __init__(self, window_name=None):
        tk.Frame.__init__(self, window_name)
        self.pack(fill="both",expand=True)
        
        for thing in range(16):
            tk.Label(self, text=patient_table_labels[thing]).grid(row=thing+2, column=0, pady=5, sticky='w')
            self.p_data = tk.Entry(self, width=50)
            self.p_data.grid(row=thing+2, column=1, pady=7,padx=10)
            in_patient_data.append(self.p_data)
        
        for thing in range(17):
            check_button_data = tk.IntVar()
            tk.Label(self, text=medhistory_table_labels1[thing]).grid(row=thing+2, column=2, pady=7, padx=2, sticky='w')
            self.med_data1 = tk.Checkbutton(self,variable=check_button_data)
            self.med_data1.grid(row=thing+2, column=3, pady=7, padx=3)
            in_med_history.append(check_button_data)
        for thing in range(16):
            check_button_data = tk.IntVar()
            tk.Label(self, text=medhistory_table_labels2[thing]).grid(row=thing+2, column=4, pady=7, padx=2, sticky='w')
            self.med_data2 = tk.Checkbutton(self,variable=check_button_data)
            self.med_data2.grid(row=thing+2, column=5, pady=7, padx=3)
            in_med_history.append(check_button_data)
        for thing in range(4):
            tk.Label(self, text=medhistory_table_labels3[thing]).grid(row=thing+2, column=6, pady=7, padx=2, sticky='w')
            self.med_data3 = tk.Entry(self)
            self.med_data3.grid(row=thing+2, column=7, pady=7, padx=2)
            in_med_history.append(self.med_data3)
        count = 0
        for thing in range(10):
            check_button_data = tk.IntVar()
            if thing < 6:
                tk.Label(self, text=arrival_table_labels1[thing]).grid(row=thing+2, column=8,pady=5, padx=2, sticky='w')
                self.arrival_data1 = tk.Entry(self)
                self.arrival_data1.grid(row=thing+2, column=9,pady=5,padx=2)
                in_home_arrival.append(self.arrival_data1)
            elif thing > 5 and thing <= 10 :
                tk.Label(self,text=arrival_table_labels2[thing - 6]).grid(row=thing+2, column=8, padx=2,sticky='w')
                self.arrival_data2 = tk.Checkbutton(self,variable=check_button_data)
                self.arrival_data2.grid(row=thing+2, column= 9,padx=2)
                in_home_arrival.append(check_button_data)



class View_Data_database(tk.Frame):
    def __init__(self, window_name=None,data=type(list)):
        tk.Frame.__init__(self, window_name)
        self.pack(side='top',fill='both',expand=True)

        patient_data = data[0]
        patient_medhist_data = data[1]
        patient_arrival_data = data[2]
        for count in range(16):
            if count % 3 == 0:
                row = get_row_p_table(patient_table_labels[count])
                col = get_col_p_table(patient_table_labels[count])
                self.heading = tk.Label(self,text = patient_table_labels[count])
                self.heading.grid(row = row , column = col,padx = 1 , pady=5,sticky='w')
                
                self.data = tk.Label(self,text=patient_data[count])
                self.data.grid(row = row, column = col+1,padx =10,pady = 5,sticky = 'w' )

            elif count % 3 == 1:
                row = get_row_p_table(patient_table_labels[count])
                col = get_col_p_table(patient_table_labels[count])
                self.heading = tk.Label(self,text = patient_table_labels[count])
                self.heading.grid(row = row , column = col,padx = 1 , pady=5,sticky='w')
                
                self.data = tk.Label(self,text=patient_data[count])
                self.data.grid(row = row, column = col+1,padx =10,pady = 5,sticky = 'w' )

            elif count % 3 == 2:
                row = get_row_p_table(patient_table_labels[count])
                col = get_col_p_table(patient_table_labels[count])
                self.heading = tk.Label(self,text = patient_table_labels[count])
                self.heading.grid(row = row , column = col,padx = 1 , pady=5,sticky='w')
                
                self.data = tk.Label(self,text=patient_data[count])
                self.data.grid(row = row, column = col+1,padx =10,pady = 5,sticky = 'w' )
        count1 = 0
        count2 = 0
        row1 =0 
        row2 =0
        for count in range(38):
            if count < 17:
                self.headings = tk.Label(self,text=medhistory_table_labels1[count])
                self.headings.grid(row = row1+6, column = 0,padx = 1,pady =2)
            
                self.data = tk.Label(self,text=patient_medhist_data[count])
                self.data.grid(row = row1+6 , column = 1,padx = 1,pady = 2,sticky='w')
                row1 += 1
            elif count > 16 and count < 32:
                self.headings = tk.Label(self,text=medhistory_table_labels2[count1])
                self.headings.grid(row = row2+6 ,column = 2,padx = 1,pady =2)
            
                self.data = tk.Label(self,text=patient_medhist_data[count])
                self.data.grid(row = row2+6 ,column = 3,padx = 1,pady =2,sticky='w')
                count1 += 1
                row2 += 1
            elif count > 32 and count < 37:
                self.headings = tk.Label(self,text=medhistory_table_labels3[count2])
                self.headings.grid(row = row1+6, column = 0, padx = 1 , pady = 2)
                
                self.data = tk.Label(self,text=patient_medhist_data[count])
                self.data.grid(row = row1+6, column = 1, padx = 1 , pady = 2,sticky='w')
                count2 += 1
                row1 += 1
        row3 = 0
        row4 =0
        col1 = 0
        col2 = 1
        count0 = 0
        for count in range(10):
            if count < 6 :
                self.heading = tk.Label(self,text=arrival_table_labels1[count])
                self.heading.grid(row = row3,column= col1+6,padx=2,pady=3)

                self.data = tk.Label(self,text=patient_arrival_data[count])
                self.data.grid(row = row3, column = col2+6,padx=2,pady=3,sticky = 'w')
                row3 += 1
            
            elif count > 4:
                self.heading = tk.Label(self,text=arrival_table_labels2[count0])
                self.heading.grid(row = row4, column = col1+8,padx=2,pady=3)

                self.data = tk.Label(self,text=patient_arrival_data[count])
                self.data.grid(row = row4, column = col2+8,padx=2,pady=3,sticky = 'w')
                count0 += 1
                row4 += 1


def get_user_input_database(entry_id = type(int)):
    patient_table_database = []
    insert_patient = []
    medical_history_database = []
    insert_medical = []
    home_arrval_database = []
    insert_arrival = []
    for data in in_patient_data:
        patient_table_database.append(data.get())
    for data in in_med_history:
        medical_history_database.append(data.get())
    for data in in_home_arrival:
        home_arrval_database.append(data.get())

    for data in patient_table_database:
        if len(data) == 0:
            val = '-'
            insert_patient.append(val)
        else:
            insert_patient.append(data)
    
    for data in patient_table_database:
        insert_medical.append(int(data))
        insert_arrival.append(int(data))
        break
    
    for data in medical_history_database:
        if data == int(1) or data == int(0) :
            if data == 1:
                val = 'Y'
                insert_medical.append(val)
            elif data == 0:
                val = 'N'
                insert_medical.append(val)
        elif len(str(data)) == 0:
            val = '-'
            insert_medical.append(val)
        else:
            insert_medical.append(data)

    for data in home_arrval_database:
        if data == int(1) or data == int(0) :
            if data == 1:
                val = 'Y'
                insert_arrival.append(val)
            elif data == 0:
                val = 'N'
                insert_arrival.append(val)
        elif len(str(data)) == 0:
            val = '-'
            insert_arrival.append(val)
        else:
            insert_arrival.append(data)

    p_keys = patient_keys
    med_keys = medical_history_keys
    arr_keys = home_arrival_keys
    patient_data = dict(zip(p_keys, insert_patient))
    med_history = dict(zip(med_keys,insert_medical))
    arrival_info = dict(zip(arr_keys,insert_arrival))
    del home_arrval_database
    del medical_history_database
    del patient_table_database
    
    p_table = metadata.tables['Patient_Data']
    med_table = metadata.tables['Medical_History']
    arrival_table = metadata.tables['Home_Arrival']
    insert_Tpatient(patient_data = patient_data,connection = connection)
    insert_TMedhistory(med_history = med_history,connection = connection)
    insert_Tarrival(arrival_info =arrival_info,connection = connection)

    sql_query = sql.select(
    [
    p_table.c.Patient_ID,  
    p_table.c.First_Name, 
    p_table.c.Last_Name,
    p_table.c.Age,
    p_table.c.Medication,
    arrival_table.c.Emergency_Contact,
    arrival_table.c.Emergency_Contact_Number    
    ]).where(p_table.c.Patient_ID == arrival_table.c.Elder_ID ).where(p_table.c.Patient_ID == entry_id)
    q_result = connection.execute(sql_query)
    mytuple = ()
    for row in q_result:    
        p_id = row[0]
        f_name = row[1]
        l_name = row[2]
        age = row[3]
        meds = row[4]
        emerg_person = row[5]
        emerg_contact = row[6]
        full_name = f_name + " " + l_name
        mytuple = (p_id,full_name,age,meds,emerg_person,emerg_contact)
    return mytuple
