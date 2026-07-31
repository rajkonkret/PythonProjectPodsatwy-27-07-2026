import openpyxl
from openpyxl.worksheet import worksheet

# pip install openpyxl

# działania na plikch excel, formatowanie, stylizacja, wykresy

workbook = openpyxl.load_workbook('sales.xlsx')
worksheet = workbook.active

print(worksheet)  # <Worksheet "Arkusz1">
