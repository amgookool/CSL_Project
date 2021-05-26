import sqlalchemy as sql
from Config.Database import engine,connection,metadata, patient_keys, medical_history_keys,home_arrival_keys,general_insert
import tkinter as tk


def display_table():
  p_table = metadata.tables['Patient_Data']
  arrival_table = metadata.tables['Home_Arrival']
  sql_query = sql.select(
    [
    p_table.c.Patient_ID,  
    p_table.c.First_Name, 
    p_table.c.Last_Name,
    p_table.c.Age,
    p_table.c.Medication,
    arrival_table.c.Emergency_Contact,
    arrival_table.c.Emergency_Contact_Number    
    ]).where(p_table.c.Patient_ID == arrival_table.c.Elder_ID )
  q_result = connection.execute(sql_query)
  display_data =[("Patient ID" , "Name","Age","Medication","Emergency Contact","Emergency Contact Number")]
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
    display_data.append(mytuple)
  return display_data


def View_data_backend(id=type(int)):
  patient_info = []
  p_table = metadata.tables['Patient_Data']
  med_history_table = metadata.tables['Medical_History']
  arrival_table = metadata.tables['Home_Arrival']
  
  select_query = p_table.select().where(p_table.c.Patient_ID == id)
  query_result = connection.execute(select_query)
  for row in query_result:
    patient_info.append(row)
  
  select_query = med_history_table.select().where(med_history_table.c.Elder_ID ==id)
  query_result = connection.execute(select_query) 
  for row in query_result:
    patient_info.append(row) 
    
  select_query = arrival_table.select().where(arrival_table.c.Elder_ID ==id)
  query_result = connection.execute(select_query) 
  for row in query_result:
    patient_info.append(row)
  return patient_info


def get_row_p_table(label):
    row = 0
    if str(label) == 'Patient ID: ' or str(label) == 'First Name: ' or str(label) == 'Last Name: ':
        row = 0
    elif str(label) == 'Date of Birth: ' or str(label) =='Age: ' or str(label) =='Address: ':
        row = 1
    elif str(label) == str(label) =='Occupation: ' or str(label) =='Hospitalisation: ' or str(label) =='Diet: ':
        row = 2
    elif str(label) == str(label) =='Medication: ' or str(label) =='Side Effects: ' or str(label) =='Last Doctor Visit: ':
        row = 3
    elif str(label) == str(label) =='Surgeries: ' or str(label) =='Allergies: ' or str(label) =='Clinic: ':
        row = 4
    else:
        row = 5
    return row


def get_col_p_table(label):
    col = 0
    if str(label) == 'Patient ID: ' or str(label) == 'Date of Birth: ' or str(label) == 'Occupation: 'or str(label) == 'Medication: ' or str(label) == 'Surgeries: ' or str(label) == 'General Practitioner: ':
        col = 0
    elif str(label) == 'First Name: ' or str(label) =='Age: ' or str(label) == 'Hospitalisation: ' or str(label) == 'Side Effects: ' or str(label) == 'Allergies: ' :
        col = 2
    elif str(label) == str(label) =='Last Name: ' or str(label) =='Address: ' or str(label) =='Diet: ' or str(label) =='Last Doctor Visit: ' or str(label) =='Clinic: ':
        col = 4
    return col




patient_table_labels = [
    "Patient ID: ",
    "First Name: ",
    "Last Name: ",
    "Date of Birth: ",
    "Age: ",
    "Address: ",
    "Occupation: ",
    "Hospitalisation: ",
    "Diet: ",
    "Medication: ",
    "Side Effects: ",
    "Last Doctor Visit: ",
    "Surgeries: ",
    "Allergies: ",
    "Clinic: ",
    "General Practitioner: "
]

medhistory_table_labels1 = [
    "Heart Disease: ",
    "Lung Disease",
    "Parkinson Disease: ",
    "Alzheimers Disease: ",
    "Respiration Disease: ",
    "Circulatory Disease: ",
    "Nervous Disease: ",	
    "Gull Bladder: ",
    "Gull Stone"	
    "Kidney Stone: ",	
    "Kidney: ",
    "Liver: ",	
    "Asthmatic: ",
    "Diabetic: ",	
    "Mental Disorder: ",
    "Arthritis: ",	
    "Cancer: ",
    "Hypertensive: ",
]

medhistory_table_labels2 = [
    "Blood Pressure: ",
    "Allergies Diabetic: ",
    "Hemorrhage/Stroke: ",	
    "Eye Problem: ",
    "Cataract: ",	
    "Hearing Problem: ",	
    "Hearing Aid Used: ",	
    "Walking Disability: ",	
    "Walking Aid used: ",	
    "Glaucoma: ",
    "Present Medication: ",
    "Aid Disease: ",	
    "Pampers Users: ",	
    "Broken Limbs: ",	
    "Violent Behaviour: ",	
    "Bowl Movements Problem: ",	
]

medhistory_table_labels3 = [
    "Food Likes: ",	
    "Food Dislikes: ",	
    "Patient bath type and temperature: ",	
    "Other Health Problems: ",
]

arrival_table_labels1 = [
    "Arrival Date: ",
    "Next of Kin: ",
    "Contact Number: ",
    "Emergency Contact: ",
    "Emergency Contact Number:" ,
    "Family Doctor: "
]

arrival_table_labels2 = [
    "Agreement Signed: ",
    "Completed Patient Form: ",
    "Interim Fees Paid: ",
    "Future Payments Made: "
]
