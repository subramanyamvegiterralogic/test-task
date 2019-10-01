# import openpyxl
import os
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import numpy


def read_excel():
    try:
        # data = pd.read_excel(os.path.abspath(r"add_items.xlsx"))
        # data = pd.read_excel(os.path.abspath("add_items.xls"))
        # df = pd.DataFrame(data, columns=['shop_id','item_name'])
        df = pd.read_excel(os.path.abspath(r"add_items.xls"), sheet_name="Sheet1")
        # print(df.columns)
        shop_id = df['shop_id']
        item_name = df['item_name']
        item_amount = df['item_amount']
        for name,amount,id in zip(item_name,item_amount,shop_id):
            print(id,'\t',amount,'\t',name)
        # print(item_name)
        # print(item_amount)
        # print(shop_id)
        # wb = openpyxl.load_workbook(os.path.abspath("add_items.xlsx"))
        # sheet = wb.active
        # for value in sheet.iter_rows(min_row=3, max_row=sheet.max_row, min_col=1, max_col=3, values_only=True):
        #     print(value)
    except Exception as e:
        print(e)


# def test_sample():
#     wb = openpyxl.load_workbook('../my_task2/heat_map_task.xlsx')
#     sheet = wb.active
#
#     print (sheet.max_row)
#     print (sheet.max_column)
    # for value in sheet.iter_rows(min_row=3, max_row=sheet.max_row, min_col=1, max_col=3, values_only=True):
    #     print(value)
#
#
# test_sample()
read_excel()
