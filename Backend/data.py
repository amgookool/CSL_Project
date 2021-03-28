import openpyxl
from openpyxl import load_workbook
file = load_workbook('Data_Records/Datasheet.xlsx')


def get_data(sheet_name):
    sheet = file.get_sheet_by_name(sheet_name)
    sheet_rows = sheet.rows
    headings = [cell.value for cell in next(sheet_rows)]
    sheet_rows_data = []
    for row in sheet_rows:
        row_data = {}
        for heading, cell in zip(headings,row):
            row_data[heading] = cell.value
            sheet_rows_data.append(row_data)
    return(sheet_rows_data)
    

patient_data = get_data("Sheet2")

medical_history = get_data("Sheet3")

home_arrival = get_data("Sheet4")





