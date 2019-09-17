import openpyxl
import math
wb = openpyxl.load_workbook('heat_map_task.xlsx')
sheet = wb.active
data = []
full_count = 0
for value in sheet.iter_rows(min_row=3, max_row=30, min_col=1, max_col=3, values_only= True):
    if value[0] is not None:
        full_count += value[1]
        data.append(value)
# print(data)
print(full_count)
x = y = (full_count//2) if full_count%2==0 else (full_count//2+1)
print(x,y)