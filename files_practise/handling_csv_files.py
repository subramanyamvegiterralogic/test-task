import csv
file_name = 'employee_csv.csv'
def write_to_csv():
    try:
        with open(file_name,'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['EID','ENAME','CITY'])
            n = int(input('Enter No.of Empoyees\t:\t'))
            for i in range(n):
                eid = input('Enter Employee ID\t:\t')
                ename = input('Enter Employee Name\t:\t')
                city = input('Enter Employee City\t:\t')
                writer.writerow([eid, ename, city])
    except Exception as e:
        print(e)


def read_from_csv():
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            for line in data:
                for word in line:
                    print(word,'\t',end='')
                print()
    except Exception as e:
        print(e)


from zipfile import *
def zipping_files():
    f = ZipFile('files.zip','w',ZIP_DEFLATED)
    f.write(file_name)
    f.write('indian_cricket_captains.txt')
    f.close()


def un_zipping_files():
    f=ZipFile('files.zip','r', ZIP_STORED)
    file_names = f.namelist()
    for name in file_names:
        print('Name : ',name)


import pandas as pd
import os
def read_from_excel():
    file_name = 'add_items.xls'
    data = pd.read_excel(os.path.abspath(file_name), sheet_name='Sheet1')
    shop_id_list= data['shop_id']
    item_name_list= data['item_name']
    item_amount_list= data['item_amount']
    print(shop_id_list)
    print(item_name_list)
    print(item_amount_list)


# write_to_csv()
# read_from_csv()
# zipping_files()
# un_zipping_files()
read_from_excel()