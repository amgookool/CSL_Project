# This module  is the initial setup of our database and tables
import sqlalchemy as sql 

table_names =['Patient_table', 'Identifications_table','Medical_History_table'] #python list of table names

# Creating the engine that holds the connection to the database
engine = sql.create_engine('sqlite:///Backend/elder_database.db', echo=None)

# metadata holds all the data to send/retreive to/from the database
metadata = sql.MetaData()

# Creating the Patient(Elder) Table object
patients = sql.Table(table_names[0], metadata,
                     sql.Column('patientID', sql.Integer, primary_key=True),
                     sql.Column('first_name', sql.String, nullable=False),
                     sql.Column('last_name', sql.String, nullable=False),
                     sql.Column('date_of_birth', sql.Date, nullable=False),
                     sql.Column('gender', sql.String, nullable=False),
                     sql.Column('marital_status', sql.String, nullable=False),
                     sql.Column('first_name', sql.String, nullable=False),)

# Creating a new table object which consists of all the identification forms of a patient
ids = sql.Table(table_names[1], metadata,
                sql.Column('id_number', sql.Integer, primary_key=True),
                sql.Column('tablePatient_id', sql.Integer,sql.ForeignKey("Patient_table.patientID")),
                sql.Column('driver_permit', sql.String, nullable=True),
                sql.Column('national_id', sql.String, nullable=True),
                sql.Column('passport_number', sql.String, nullable=True),)

# Creating a new table object which consists of the medical history of a patient and their medication dosage and frequency
medHistory = sql.Table(table_names[2], metadata,
                       sql.Column('medRecord_id', sql.Integer, primary_key=True),
                       sql.Column('tablePatient_id', sql.Integer,sql.ForeignKey("Patient_table.patientID")),
                       sql.Column('medical_history', sql.String, nullable=False),
                       sql.Column('dosage', sql.String, nullable=False),
                       sql.Column('frequency', sql.Integer, nullable=False),)

# commiting the table objects into the database through the engine which hold the connection to the database
metadata.create_all(engine)


