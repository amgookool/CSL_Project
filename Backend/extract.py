from openpyxl import load_workbook

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
