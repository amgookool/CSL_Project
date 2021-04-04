from openpyxl import load_workbook
from datetime import datetime as dt

file = 'Backend/Datasheet.xlsx'


def get_data(file_name,sheet_name):
  wb = load_workbook(file_name)
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
  
  
  
patient_data = get_data(file,"Sheet2")
    
med_history = get_data(file,"Sheet3")

arrival_info = get_data(file,"Sheet4")




for data in arrival_info:
    Elder_ID =int(data.get("Patient ID"))
    Arrival_Date = str(data.get("Arrival Date"))
    Next_of_Kin = str(data.get("Next of Kin"))
    Contact_Number = str(data.get("Contact #"))
    Emergency_Contact = str(data.get("Emergency Contact "))
    Emergency_Contact_Number = str(data.get("Emergency Contact #"))
    Family_Doctor = str(data.get("Family Doctor"))
    Agreement_Signed = str(data.get("Agreement Sign "))
    Completed_Patient_Form = str(data.get("Completed Patient Form "))
    Interim_Fees_Paid = str(data.get("Interim Fees Paid "))
    Arrangements_for_future_payments_made = str(data.get("Arrangements for future payments made "))
    


 