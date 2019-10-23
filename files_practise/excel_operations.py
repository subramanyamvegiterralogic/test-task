import xlwt
from xlwt import Workbook
wb= Workbook()
file_name='add_items2.xls'
sheet1 = wb.add_sheet('Sheet1')
sheet1.write(1,0,'AMARAVATHI')
sheet1.write(2,0,'BANGALORE')
sheet1.write(3,0,'CHENNAI')
sheet1.write(4,0,'KOCHI')
sheet1.write(5,0,'TRIVENDRAM')
wb.save(file_name)