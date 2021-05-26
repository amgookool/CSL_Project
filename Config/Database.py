# This module  is the initial setup of our database and tables and contains functions that allow us to C.R.U.D.
from itertools import zip_longest # this module allows us to zip lists of data as tuples to iterate over(helps in manipulating data)
import sqlalchemy as sql
from sqlalchemy.sql.schema import ForeignKeyConstraint  # importing sqlalchemy interpreter
from sqlalchemy.sql.sqltypes import BigInteger, Date, Integer, String, TEXT, Text
from openpyxl import load_workbook



def get_data(sheet_name):
  file = 'Config/Datasheet.xlsx'
  wb = load_workbook(file)
  sheet_name = wb[sheet_name]
  all_rows = list(sheet_name.rows)
  heading_data = []
  person_data = []
  data = []
  i = 1
  for header in all_rows[0]:
    heading_data.append(header.value)
  for cells in all_rows[1:12]:
    if all_rows[i]:
      _data = []
      for cell in cells:
        _data.append(cell.value)
      person_data.append(_data)
    i = i + 1
  for values in person_data:
    _dict = dict(zip(heading_data, values))
    data.append(_dict)
  return data

def insert_Tpatient(patient_data = type(dict), connection = type(sql.engine.base.Connection)):
    insert = Patient_Table.insert().values(
        First_Name = str(patient_data.get("First Name ")),
        Last_Name  = str(patient_data.get("Last Name ")),  
        Date_of_Birth = str(patient_data.get("Date of Birth ")), 
        Age = str(patient_data.get("Age")), 
        Address = str(patient_data.get("Address")),
        Occupation = str(patient_data.get("Occupation")),
        Hospitalization =str(patient_data.get("Hospitalization ")),
        Diet = str(patient_data.get("Diet")),
        Medication = str(patient_data.get("Medication")),
        Side_Effects = str(patient_data.get("Side Effects")),
        Last_Doctor_Visit = str(patient_data.get("Last Doctor Visit")),
        Surgeries = str(patient_data.get("Surgeries")),
        Allergies = str(patient_data.get("Allergies")),
        Clinic = str(patient_data.get("Clinic")),
        General_Practitioner = str(patient_data.get("General Practioner")))
    result = connection.execute(insert)
    return result

def insert_TMedhistory(med_history = type(dict), connection = type(sql.engine.base.Connection)):
    insert = Medhistory_Table.insert().values(
        Elder_ID = int(med_history.get("Patient ID")),
        Heart_Disease = str(med_history.get("Heart Disease")),
        Lung_Disease = str(med_history.get("Lung Disease ")),
        Parkinson_Disease = str(med_history.get("Parkinson Disease")),
        Alzheimer_Disease = str(med_history.get("Alzheimers Disease")),
        Respiration_Disease = str(med_history.get("Respiration Disease")),
        Circulatory_Disease = str(med_history.get("Circulatory Disease")),
        Nervous_Disease = str(med_history.get("Nervous Disease")),
        Gull_Bladder = str(med_history.get("Gull Bladder")),
        Gull_Stone = str(med_history.get("Gull Stone")),
        Kidney_Stone = str(med_history.get("Kidney Stone")),
        Kidney = str(med_history.get("Kidney")),
        Liver = str(med_history.get("Liver")),
        Asthmatic = str(med_history.get("Asthmatic")),
        Diabetic = str(med_history.get("Diabetic")),
        Mental_Disorder = str(med_history.get("Mental Disorder")),
        Arthritis = str(med_history.get("Arthritis")), 
        Cancer = str(med_history.get("Cancer")),
        Hypertensive = str(med_history.get("Hypertensive")),
        Blood_Pressure = str(med_history.get("Blood Pressure")),
        Allergies_Diabetic = str(med_history.get("Allergies Diabetic")),
        Stroke = str(med_history.get("Cerebral Hemorrhage/Stroke")),
        Eye_Problem = str(med_history.get("Eye Problem")), 
        Cataract = str(med_history.get("Cataract")),
        Hearing_Problem = str(med_history.get("Hearing Problem")),
        Hearing_Aid_Used = str(med_history.get("Hearing Aid Used")),
        Walking_Disability = str(med_history.get("Walking Disability")),
        Walking_Aid_Used = str(med_history.get("Walking Aid Used ")),
        Glaucoma = str(med_history.get("Glaucoma")),
        Present_Medication = str(med_history.get("Present Medication")),
        Aid_Disease = str(med_history.get("Aid Disease ")),
        Pampers_Users = str(med_history.get("Pampers Users")),
        Broken_Limbs = str(med_history.get("Broken Limbs")),
        Violent_Behavior = str(med_history.get("Violent Behaviour")),
        Bowel_Movements_Problem = str(med_history.get("Bowel Movements Problem")), 
        Food_Likes = str(med_history.get("Food Likes")),
        Food_Dislikes = str(med_history.get("Food Dislikes")),
        Bath_Temperature = str(med_history.get("Patient bath type and temperature")),
        Other_Health_Problems = str(med_history.get("Other Health Problems"))
    )
    result = connection.execute(insert)
    return result

def insert_Tarrival(arrival_info = type(dict),connection = type(sql.engine.base.Connection)):
    insert = Home_Arrival_Table.insert().values(
    Elder_ID =int(arrival_info.get("Patient ID")),
    Arrival_Date = str(arrival_info.get("Arrival Date")),
    Next_of_Kin = str(arrival_info.get("Next of Kin")),
    Contact_Number = str(arrival_info.get("Contact #")),
    Emergency_Contact = str(arrival_info.get("Emergency Contact ")),
    Emergency_Contact_Number = str(arrival_info.get("Emergency Contact #")),
    Family_Doctor = str(arrival_info.get("Family Doctor")),
    Agreement_Signed = str(arrival_info.get("Agreement Sign ")),
    Completed_Patient_Form = str(arrival_info.get("Completed Patient Form ")),
    Interim_Fees_Paid = str(arrival_info.get("Interim Fees Paid ")),
    Future_Payments_Made = str(arrival_info.get("Arrangements for future payments made ")),
    )
    result = connection.execute(insert)
    return result

def general_insert(dict_list = type(list),Table = type(sql.Table), connection = type(sql.engine.base.Connection)):
    if Table == Patient_Table:
        for data in dict_list:
            insert_Tpatient(data,connection)
    elif Table == Medhistory_Table:
        for data in dict_list:
            insert_TMedhistory(data,connection)
    elif Table == Home_Arrival_Table:
        for data in dict_list:
            insert_Tarrival(data,connection)

def database_delete(id_number = type(int)):
  statement = Patient_Table.delete().\
    where(Patient_Table.c.Patient_ID == id_number)
  connection.execute(statement)
  statement = Medhistory_Table.delete().\
    where(Medhistory_Table.c.Elder_ID == id_number)
  connection.execute(statement)
  statement = Home_Arrival_Table.delete().\
    where(Home_Arrival_Table.c.Elder_ID == id_number)
  connection.execute(statement)


patient_data = get_data("Sheet2")

med_history = get_data("Sheet3")

arrival_info = get_data("Sheet4")

# Setup of the database .db file and creating the necessary tools to interact with database base with python SQLAlchemy
#engine = sql.create_engine("sqlite:///Config/elder_database.db", echo=False)  # Creating the engine that holds the connection to the database
engine = sql.create_engine("sqlite:///Config/elder_database.db", echo=False)
connection = engine.connect()  # Creating the connection to the database in the engine

metadata = sql.MetaData() # metadata holds all the data to send/retreive to/from the database

Patient_Table = sql.Table( #Creation of Patient Table
    'Patient_Data', metadata,
    sql.Column("Patient_ID", Integer, primary_key=True,autoincrement=True),  # Patient ID
    sql.Column("First_Name", String, nullable=False),  # First Name
    sql.Column("Last_Name", String, nullable=False),  # last name
    sql.Column("Date_of_Birth", String, nullable=True),  # Date of birth
    sql.Column("Age", String, nullable=True),  # Age
    sql.Column("Address", String, nullable=True),  # Address
    sql.Column("Occupation", String, nullable=True),  # Occupation
    sql.Column("Hospitalization", String, nullable=True),  # Hospitalization
    sql.Column("Diet", String, nullable=True),  # Diet
    sql.Column("Medication", String, nullable=True),  # medication
    sql.Column("Side_Effects", String, nullable=True),  # Side effects
    sql.Column("Last_Doctor_Visit",String, nullable=True),  # Last Doctor visit
    sql.Column("Surgeries", String, nullable=True),  # Surgeries
    sql.Column("Allergies", String, nullable=True),  # Allergies
    sql.Column("Clinic", String, nullable=True),  # Clinic
    sql.Column("General_Practitioner", String, nullable=True))

Medhistory_Table = sql.Table( #Creation of medical history table
    'Medical_History',metadata,
    sql.Column("Medical_ID",Integer, primary_key=True,autoincrement=True),
    sql.Column("Elder_ID",Integer,sql.ForeignKey("Patient_Data.Patient_ID"),autoincrement=True,),
    sql.Column("Heart_Disease", String, nullable=True),
    sql.Column("Lung_Disease", String, nullable=True),
    sql.Column("Parkinson_Disease", String, nullable=True),
    sql.Column("Alzheimer_Disease", String, nullable=True),
    sql.Column("Respiration_Disease", String, nullable=True),
    sql.Column("Circulatory_Disease", String, nullable=True),
    sql.Column("Nervous_Disease", String, nullable=True),
    sql.Column("Gull_Bladder", String, nullable=True),
    sql.Column("Gull_Stone", String, nullable=True),
    sql.Column("Kidney_Stone", String, nullable=True),
    sql.Column("Kidney", String, nullable=True),
    sql.Column("Liver", String, nullable=True),
    sql.Column("Asthmatic", String, nullable=True),
    sql.Column("Diabetic", String, nullable=True),
    sql.Column("Mental_Disorder", String, nullable=True),
    sql.Column("Arthritis", String, nullable=True),
    sql.Column("Cancer", String, nullable=True),
    sql.Column("Hypertensive", String, nullable=True),
    sql.Column("Blood_Pressure", String, nullable=True),
    sql.Column("Allergies_Diabetic", String, nullable=True),
    sql.Column("Stroke", String, nullable=True),
    sql.Column("Eye_Problem", String, nullable=True),
    sql.Column("Cataract", String, nullable=True),
    sql.Column("Hearing_Problem", String, nullable=True),
    sql.Column("Hearing_Aid_Used", String, nullable=True),
    sql.Column("Walking_Disability", String, nullable=True),
    sql.Column("Walking_Aid_Used", String, nullable=True),
    sql.Column("Glaucoma", String, nullable=True),
    sql.Column("Present_Medication", String, nullable=True),
    sql.Column("Aid_Disease", String, nullable=True),
    sql.Column("Pampers_Users", String, nullable=True),
    sql.Column("Broken_Limbs", String, nullable=True),
    sql.Column("Violent_Behavior", String, nullable=True),
    sql.Column("Bowel_Movements_Problem", String, nullable=True),
    sql.Column("Food_Likes", Text, nullable=True),
    sql.Column("Food_Dislikes", Text, nullable=True),
    sql.Column("Bath_Temperature", Text, nullable=True),
    sql.Column("Other_Health_Problems", Text, nullable=True)
    )

Home_Arrival_Table = sql.Table( #Creation of home_arrival table
    "Home_Arrival", metadata,
    sql.Column("Home_ID", Integer, primary_key=True,autoincrement=True),
    sql.Column("Elder_ID",Integer,sql.ForeignKey("Patient_Data.Patient_ID"),autoincrement=True),
    sql.Column("Arrival_Date", String, nullable=True),
    sql.Column("Next_of_Kin", String, nullable=True),
    sql.Column("Contact_Number", String, nullable=True),
    sql.Column("Emergency_Contact", String, nullable=True),
    sql.Column("Emergency_Contact_Number", String, nullable=True),
    sql.Column("Family_Doctor", String, nullable=True),
    sql.Column("Agreement_Signed", String, nullable=True),
    sql.Column("Completed_Patient_Form", String, nullable=True),
    sql.Column("Interim_Fees_Paid", String, nullable=True),
    sql.Column("Future_Payments_Made", String, nullable=True),
    )

metadata.create_all(engine) 


general_insert(patient_data,Patient_Table,connection)

general_insert(med_history,Medhistory_Table,connection)

general_insert(arrival_info,Home_Arrival_Table,connection)


patient_keys = list(patient_data[0].keys())

medical_history_keys = list(med_history[0].keys())

home_arrival_keys = list(arrival_info[0].keys())

medical_history_keys.pop(1)

home_arrival_keys.pop(1)

