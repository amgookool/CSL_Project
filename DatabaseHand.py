# This python module will be used to interact with the database 
from itertools import zip_longest  #this module allows us to zip lists of data as tuples to iterate over(helps in manipulating data)
import sqlalchemy as sql  # importing sqlalchemy interpreter
from Backend.ElderHDatabase import table_names,table_patients , table_identification, table_medicalHistory # these are the tables in the database
from Backend.ElderHDatabase import insert_record
from Data_Records.FakeData import *  # importing the raw data for the database

# Creating the engine that holds the connection to the database
engine = sql.create_engine("sqlite:///Backend/elder_database.db", echo=True)
# Creating the connection to the database in the engine
connection = engine.connect()
# metadata holds all the data to send/retreive to/from the database
metadata = sql.MetaData()


# RAW DATA we got from the Data_records package(Folder)
dob = date_of_birth
dp = driver_permit
passport = passport_number
nat_id = national_id
nok = next_of_kin
medhist = medical_history


# use the zip function to zip the contents in each list in relation to the iterator and then format that tuple as a list
patient_data = zip_longest(first_names, last_names,
                           dob, gender, marital_status, nok)

id_data = zip_longest(dp, nat_id, passport)

list_days=[] 
for days in dosage:
    list_days.append(str(days))
dosage = list_days
print(dosage)
med_hist_data = zip_longest(medhist, dosage, frequency)

insert_record(table_names[0],patient_data)
insert_record(table_names[1],id_data)
insert_record(table_names[2],med_hist_data)



