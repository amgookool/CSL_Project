# This module  is the initial setup of our database and tables and contains functions that allow us to C.R.U.D.
from Data_Records.data import home_arrival, medical_history, patient_data
# this module allows us to zip lists of data as tuples to iterate over(helps in manipulating data)
from itertools import zip_longest
import sqlalchemy as sql  # importing sqlalchemy interpreter


print(home_arrival[0])
'''
# Create a list of table names that are in the database
table_names = ["Patient_Data",
               "Medical_History",
               "Home_Arrival"]

# Creating the engine that holds the connection to the database
engine = sql.create_engine("sqlite:///Backend/elder_database.db", echo=True)
# Creating the connection to the database in the engine
connection = engine.connect()
# metadata holds all the data to send/retreive to/from the database
metadata = sql.MetaData()


# Creating the Patient(Elder) Table object
def Patient_Table(table_name, engine, metadata):
    patients = sql.Table(
        table_name, metadata,
        sql.Column("PatientID", sql.Integer, primary_key=True),
        sql.Column("First_Name", sql.TEXT, nullable=False),
        sql.Column("Last_Name", sql.TEXT, nullable=False),
        sql.Column("Date_of_Birth", sql.TEXT, nullable=False),
        sql.Column("Gender", sql.Text, nullable=False),
        sql.Column("Marital_Status", sql.Text, nullable=True),
        sql.Column("NextKin", sql.TEXT, nullable=True),
    )
    metadata.create_all(engine)
    return patients


# Creating a new table object which consists of all the identification forms of a patient
def Identification_Table(table_name, engine, metadata):
    ids = sql.Table(
        table_name,
        metadata,
        sql.Column("ID_Number", sql.Integer, primary_key=True),
        sql.Column("Patient_ID", sql.ForeignKey(
            "{}.PatientID".format(table_names[0])),),
        sql.Column("Driver_Permit", sql.TEXT, nullable=True),
        sql.Column("National_ID", sql.TEXT, nullable=True),
        sql.Column("Passport_Number", sql.TEXT, nullable=True),
    )
    metadata.create_all(engine)
    return ids


# Creating a new table object which consists of the medical history of a patient and their medication dosage and frequency
def Medical_history_Table(table_name, engine, metadata):
    medHistory = sql.Table(
        table_name,
        metadata,
        sql.Column("Record_ID", sql.Integer, primary_key=True),
        sql.Column("Patient_ID", sql.ForeignKey(
            "{}.PatientID".format(table_names[0])),),
        sql.Column("Medical_History", sql.TEXT, nullable=False),
        sql.Column("Dosage", sql.TEXT, nullable=False),
        sql.Column("Frequency", sql.Integer, nullable=False),
    )
    metadata.create_all(engine)
    return medHistory


table_patients = Patient_Table(table_names[0], engine, metadata)
table_identification = Identification_Table(table_names[1], engine, metadata)
table_medicalHistory = Medical_history_Table(table_names[2], engine, metadata)


# Defining a function that inserts a record into the patient,identification,medical history table
def insert_record(table_name, patient_record):
    if table_name == table_names[0]:  # Patient Table
        insert_query = table_patients.insert()
        for (a, b, c, d, e, f) in patient_record:
            insert_query = insert_query.values(
                {
                    "First_Name": (a),
                    "Last_Name": (b),
                    "Date_of_Birth": (c),
                    "Gender": (d),
                    "Marital_Status": (e),
                    "NextKin": (f),
                }
            )
            connection.execute(insert_query)

    elif table_name == table_names[1]:  # Identification Table
        insert_query = table_identification.insert()
        for (a, b, c) in patient_record:
            insert_query = insert_query.values(
                {"Driver_Permit": a, "National_ID": b, "Passport_Number": c})
            connection.execute(insert_query)

    elif table_name ==table_names[2]:  # Medical History Table
        insert_query = table_medicalHistory.insert()
        for (a, b, c) in patient_record:
            insert_query = insert_query.values(
                {"Medical_History": a, "Dosage": b, "Frequency": c}
            )
            connection.execute(insert_query)


# Defining a function that takes a query and returns information based on the query Read Functionality


# Defining a function that allows us to update a record field in the datbase using a query

# Defining a function that allows us to deleting a record in the datbase using a query
'''