# This module  is the initial setup of our database and tables and contains functions that allow us to C.R.U.D.

# this module allows us to zip lists of data as tuples to iterate over(helps in manipulating data)
from itertools import zip_longest
import sqlalchemy as sql  # importing sqlalchemy interpreter

# Create a list of table names that are in the database
table_names = ["Patient_table",
               "Identifications_table",
               "Medical_History_table"]

# Creating the engine that holds the connection to the database
engine = sql.create_engine("sqlite:///Backend/elder_database.db")#, echo=True) 
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


# By Sajjaad Ramdath:
# Start of Saj code.

#works
def searchPatients(patientid='',firstname='',lastname='',dateofbirth='',gender='',maritalstatus='',nextkin=''):
    engine=sql.create_engine('sqlite:///Backend/elder_database.db')
    connection=engine.connect()
    metadata=sql.MetaData()
    users=sql.Table('Patient_table', metadata, autoload=True, autoload_with=engine)
    select=sql.select([table_patients]).where(sql.or_(
        table_patients.columns.PatientID==patientid,
        table_patients.columns.First_Name==firstname,
        table_patients.columns.Last_Name==lastname,
        table_patients.columns.Date_of_Birth==dateofbirth,
        table_patients.columns.Gender==gender,
        table_patients.columns.Marital_Status==maritalstatus,
        table_patients.columns.NextKin==nextkin,
        ))
    result_proxy = connection.execute(select)
    result_set=result_proxy.fetchall()
    print(result_set)
    return

#need to test with test data
def searchIdentification(idnumber='',patientid='',driverpermit='',nationalid='',passportnumber=''):
    engine=sql.create_engine('sqlite:///Backend/elder_database.db')
    connection=engine.connect()
    metadata=sql.MetaData()
    users=sql.Table('Identifications_Table', metadata, autoload=True, autoload_with=engine)
    select=sql.select([table_identification]).where(sql.or_(
        table_identification.columns.ID_Number==idnumber,
        table_identification.columns.Patient_ID==patientid,
        table_identification.columns.Driver_Permit==driverpermit,
        table_identification.columns.National_ID==nationalid,
        table_identification.columns.Passport_Number==passportnumber,
        ))
    result_proxy = connection.execute(select)
    result_set=result_proxy.fetchall()
    print(result_set)
    return

#not working -> getting PatientID attribute error
def searchMedical(recordid='',patientid='',medicalhistory='',dosage='',frequency=''):
    engine=sql.create_engine('sqlite:///Backend/elder_database.db')
    connection=engine.connect()
    metadata=sql.MetaData()
    users=sql.Table('Medical_History_Table', metadata, autoload=True, autoload_with=engine)
    select=sql.select([table_medicalHistory]).where(sql.or_(
        table_medicalHistory.columns.Record_ID==recordid,
        table_medicalHistory.columns.PatientID==patientid,
        table_medicalHistory.columns.Medical_History==medicalhistory,
        table_medicalHistory.columns.Dosage==dosage,
        table_medicalHistory.columns.Frequency==frequency,
        ))
    result_proxy = connection.execute(select)
    result_set=result_proxy.fetchall()
    print(result_set)
    return

# End of Saj code.
    



# Defining a function that allows us to update a record field in the datbase using a query

# Defining a function that allows us to deleting a record in the datbase using a query
