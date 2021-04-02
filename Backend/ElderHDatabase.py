# This module  is the initial setup of our database and tables and contains functions that allow us to C.R.U.D.
from itertools import zip_longest # this module allows us to zip lists of data as tuples to iterate over(helps in manipulating data)
import sqlalchemy as sql  # importing sqlalchemy interpreter
from sqlalchemy.sql.sqltypes import BigInteger, TEXT, Text

def patient_table_insert ():
    insert = Patient_Table.insert()
    '''
    for item in patient_data:
        insert.values(
           Patient_ID = item.get("Patient_ID"),
           First_Name = item.get("First_Name"),
           Last_Name = item.get("Last_Name"),
           Date_of_Birth = item.get("Date_of_Birth"),
           Age = item.get("Age"),
           Address = item.get("Address"),
           Occupation = item.get("Occupation"),
           Hospitalization = item.get("Hospitalization"),
           Diet = item.get("Diet"),
           Medication = item.get("Medication"),
           Side_Effects=item.get("Side_Effects"),  # Side effects
           Last_Doctor_Visit = item.get("Last_Doctor_Visit"),  # Last Doctor visit
           Surgeries = item.get("Surgeries"),
           Allergies = item.get("Allergies"),
           Clinic = item.get("Clinic"),
           General_Practitioner = item.get("General_Practitioner"))
           '''


# Setup of the database .db file and creating the necessary tools to interact with database base with python SQLAlchemy
engine = sql.create_engine("sqlite:///Backend/elder_database.db", echo=False)  # Creating the engine that holds the connection to the database

connection = engine.connect()  # Creating the connection to the database in the engine

metadata = sql.MetaData() # metadata holds all the data to send/retreive to/from the database

Patient_Table = sql.Table( #Creation of Patient Table
    'Patient_Data', metadata,
    sql.Column("Patient_ID", sql.BIGINT, primary_key=True),  # Patient ID
    sql.Column("First_Name", sql.TEXT, nullable=False),  # First Name
    sql.Column("Last_Name", sql.TEXT, nullable=False),  # last name
    sql.Column("Date_of_Birth", sql.DATE, nullable=False),  # Date of birth
    sql.Column("Age", sql.INTEGER, nullable=False),  # Age
    sql.Column("Address", sql.TEXT, nullable=False),  # Address
    sql.Column("Occupation", sql.TEXT, nullable=False),  # Occupation
    sql.Column("Hospitalization", sql.CHAR, nullable=False),  # Hospitalization
    sql.Column("Diet", sql.CHAR, nullable=False),  # Diet
    sql.Column("Medication", sql.TEXT, nullable=False),  # medication
    sql.Column("Side_Effects", sql.CHAR, nullable=False),  # Side effects
    sql.Column("Last_ Doctor_Visit", sql.DATE, nullable=False),  # Last Doctor visit
    sql.Column("Surgeries", sql.TEXT, nullable=False),  # Surgeries
    sql.Column("Allergies", sql.CHAR, nullable=True),  # Allergies
    sql.Column("Clinic", sql.CHAR, nullable=True),  # Clinic
    sql.Column("General_Practitioner", sql.TEXT, nullable=False))

Medhistory_Table = sql.Table( #Creation of medical history table
    'Medical_History',metadata,
    sql.Column("Medical_ID", sql.INTEGER, nullable=False, primary_key=True),
    sql.Column(
        "Patient_ID",
        sql.BIGINT,
        sql.ForeignKey(Patient_Table.c.Patient_ID),
        nullable=False,
    ),
    sql.Column("Heart_Disease", sql.CHAR, nullable=True),
    sql.Column("Lung_Disease", sql.CHAR, nullable=True),
    sql.Column("Parkinson_Disease", sql.CHAR, nullable=True),
    sql.Column("Alzheimer_Disease ", sql.CHAR, nullable=True),
    sql.Column("Respiration_Disease", sql.CHAR, nullable=True),
    sql.Column("Circulatory_Disease", sql.CHAR, nullable=True),
    sql.Column("Nervous_Disease", sql.CHAR, nullable=True),
    sql.Column("Gull_Bladder", sql.CHAR, nullable=True),
    sql.Column("Gull_Stone", sql.CHAR, nullable=True),
    sql.Column("Kidney_Stone", sql.CHAR, nullable=True),
    sql.Column("Kidney", sql.CHAR, nullable=True),
    sql.Column("Liver", sql.CHAR, nullable=True),
    sql.Column("Asthmatic", sql.CHAR, nullable=True),
    sql.Column("Diabetic", sql.CHAR, nullable=True),
    sql.Column("Mental Disorder", sql.CHAR, nullable=True),
    sql.Column("Arthritis", sql.CHAR, nullable=True),
    sql.Column("Cancer", sql.CHAR, nullable=True),
    sql.Column("Hypertensive", sql.CHAR, nullable=True),
    sql.Column("Blood_Pressure", sql.CHAR, nullable=True),
    sql.Column("Allergies_Diabetic", sql.CHAR, nullable=True),
    sql.Column("Stroke", sql.CHAR, nullable=True),
    sql.Column("Eye_Problem", sql.CHAR, nullable=True),
    sql.Column("Cataract", sql.CHAR, nullable=True),
    sql.Column("Hearing_Problem", sql.CHAR, nullable=True),
    sql.Column("Hearing_Aid_Used", sql.CHAR, nullable=True),
    sql.Column("Walking_Disability", sql.CHAR, nullable=True),
    sql.Column("Walking_Aid_Used", sql.CHAR, nullable=True),
    sql.Column("Glaucoma", sql.CHAR, nullable=True),
    sql.Column("Present_Medication", sql.CHAR, nullable=True),
    sql.Column("Aid_Disease", sql.CHAR, nullable=True),
    sql.Column("Pampers_Users", sql.CHAR, nullable=True),
    sql.Column("Broken_Limbs", sql.CHAR, nullable=True),
    sql.Column("Violent_Behavior", sql.CHAR, nullable=True),
    sql.Column("Bowel_Movements_Problem", sql.CHAR, nullable=True),
    sql.Column("Food_Likes", sql.TEXT, nullable=True),
    sql.Column("Food_Dislikes", sql.TEXT, nullable=True),
    sql.Column("Bath_Temperature", sql.TEXT, nullable=True),
    sql.Column("Other_Health_Problems", sql.TEXT, nullable=True))

Home_arrival_table = sql.Table( #Creation of home_arrival table
    "Home_Arrival", metadata,
    sql.Column("Home_ID", sql.INTEGER, nullable=False, primary_key=True),
    sql.Column(
        "Patient_ID",
        sql.BIGINT,
        sql.ForeignKey(Patient_Table.c.Patient_ID),
        nullable=False,
    ),
    sql.Column("Arrival_Date", sql.DATE, nullable=True),
    sql.Column("Next_of_Kin", sql.DATE, nullable=True),
    sql.Column("Contact_Number", sql.DATE, nullable=True),
    sql.Column("Emergency_Contact", sql.DATE, nullable=True),
    sql.Column("Emergency_Contact_Number", sql.DATE, nullable=True),
    sql.Column("Family_Doctor", sql.DATE, nullable=True),
    sql.Column("Agreement_Signed", sql.DATE, nullable=True),
    sql.Column("Completed_Patient_Form", sql.DATE, nullable=True),
    sql.Column("Interim_Fees_Paid", sql.DATE, nullable=True),
    sql.Column("Arrangements_for_future_payments_made", sql.DATE, nullable=True))

metadata.create_all(engine) 


ins = Patient_Table.insert()
i =0

# patient_keys = patient_data[0].keys()
# medical_history_keys = medical_history[0].keys()
# home_arrival_keys = home_arrival[0].keys()

# num = 0
# for heading in patient_keys:
#     print("heading {} : {}".format(num, heading))
#     num = num + 1

"""
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
"""
