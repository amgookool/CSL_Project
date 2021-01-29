# This module  is the initial setup of our database and tables
from itertools import zip_longest
import sqlalchemy as sql
from sqlalchemy.sql.schema import MetaData  # importing sqlalchemy interpreter
from Backend.FakeData import *  # importing the raw data for the database


# Create a list of table names that are in the database
table_names = ['Patient_table', 'Identifications_table',
               'Medical_History_table']

# Creating the engine that holds the connection to the database
engine = sql.create_engine('sqlite:///Backend/elder_database.db', echo=True)
# Creating the connection to the database in the engine
connection = engine.connect()
# metadata holds all the data to send/retreive to/from the database
metadata = sql.MetaData()


# Creating the Patient(Elder) Table object
def Patient_Table(table_name, engine, metadata):
    patients = sql.Table(table_name, metadata,
                         sql.Column('PatientID', sql.Integer,
                                    primary_key=True),
                         sql.Column('First_Name', sql.TEXT, nullable=False),
                         sql.Column('Last_Name', sql.TEXT, nullable=False),
                         sql.Column('Date_of_Birth', sql.TEXT, nullable=False),
                         sql.Column('Gender', sql.Text, nullable=False),
                         sql.Column('Marital_Status', sql.Text, nullable=True),
                         sql.Column('NextKin', sql.TEXT, nullable=True),)
    metadata.create_all(engine)
    return patients


patients = Patient_Table(table_names[0], engine, metadata)


# Creating a new table object which consists of all the identification forms of a patient
def Identification_Table(table_name, engine, metadata):
    ids = sql.Table(table_name, metadata,
                    sql.Column('ID_Number', sql.Integer, primary_key=True),
                    sql.Column('Patient_ID', sql.Integer, sql.ForeignKey(
                        "{}.PatientID".format(table_names[0]))),
                    sql.Column('Driver_Permit', sql.TEXT, nullable=True),
                    sql.Column('National_ID', sql.TEXT, nullable=True),
                    sql.Column('Passport_Number', sql.TEXT, nullable=True),)
    metadata.create_all(engine)
    return ids

identification = Identification_Table(table_names[1],engine,metadata)

def Medical_history_Table(table_name,engine,metadata):# Creating a new table object which consists of the medical history of a patient and their medication dosage and frequency
    medHistory = sql.Table(table_name, metadata,
                       sql.Column('Record_ID', sql.Integer,
                                  primary_key=True),
                       sql.Column('Patient_ID', sql.Integer, sql.ForeignKey(
                           "{}.PatientID".format(table_names[0]))),
                       sql.Column('Medical_History',
                                  sql.TEXT, nullable=False),
                       sql.Column('Dosage', sql.TEXT, nullable=False),
                       sql.Column('Frequency', sql.Integer, nullable=False),)
    metadata.create_all(engine)
    return medHistory

medicalHistory = Medical_history_Table(table_names[2],engine,metadata)


# RAW DATA
dob = date_of_birth
dp = driver_permit
passport = passport_number
nat_id = national_id
nok = next_of_kin
medhist = medical_history



# use the zip function to zip the contents in each list in relation to the iterator and then format that tuple as a list
patient_data = zip_longest(
    first_names, last_names, dob, gender, marital_status, nok)

id_data = zip_longest(dp, nat_id, passport)
temp = []
for item in dosage:
    temp.append(str(item))
dosage = temp

med_hist_data= zip_longest(medhist,dosage,frequency)


def insert_record_patient_table(patient_record):
    for (a, b, c, d, e, f) in patient_record:
        query_insert = patients.insert().values({"First_Name": (a), "Last_Name": (b), "Date_of_Birth":(c), "Gender": (d), "Marital_Status":(e), "NextKin":(f)})
        connection.execute(query_insert)

insert_record_patient_table(patient_data)

def insert_record_identification_table(patient_record):
    for (a,b,c) in patient_record:
        query_insert = identification.insert().values({"Driver_Permit":a,"National_ID":b,"Passport_Number":c})
        connection.execute(query_insert)
insert_record_identification_table(id_data)

def insert_record_Medical_History_table(patient_record):
    for (a,b,c) in patient_record:
        query_insert = medicalHistory.insert().values({"Medical_History":a,"Dosage":b,"Frequency":c})
        connection.execute(query_insert)
insert_record_Medical_History_table(med_hist_data)


