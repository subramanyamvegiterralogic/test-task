import plotly.graph_objects as go
# z = [[1,20,30,50,1],[20,1,60,80,30],[30,60,1,-10,20]]
# x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# y=['Morning', 'Afternoon', 'Evening']
# fig = go.Figure(data=go.Heatmap(z,x,y))
# fig.show()
# fig = go.Figure(data=go.Heatmap(
#                    z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
#                    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
#                    y=['Morning', 'Afternoon', 'Evening']))
# fig.show()

import xlrd
# import pandas as pd
# import numpy
# from pandas import ExcelFile,ExcelWriter
file_name = "Heat map Task.xlsx"
# def test_test():
#     import pandas as pd
#     df = pd.read_excel(file_name)
#     df = df[['Area']
# test_test()

def xlrd_exp():
    workbook = xlrd.open_workbook(file_name)
    worksheet = workbook.sheet_by_name('Sheet1')
    no_of_rows = worksheet.nrows
    no_of_cols = worksheet.ncols
    print(no_of_rows , no_of_cols)
    result_data = []
    for curr_row in range(no_of_rows):
        row_data = []
        for curr_col in range(no_of_cols):
            data = worksheet.cell_value(curr_row,curr_col)
            row_data.append(data)
        result_data.extend(row_data)
    print(res)
# xlrd_exp()

def example3():
    workbook = xlrd.open_workbook(file_name, on_demand = True)
    worksheet = workbook.sheet_by_index(0)
    first_row = [] # Header
    for col in range(worksheet.ncols):
        first_row.append( worksheet.cell_value(0,col) )
    # tronsform the workbook to a list of dictionnaries
    data =[]
    for row in range(1, worksheet.nrows):
        elm = {}
        for col in range(worksheet.ncols):
            elm[first_row[col]]=worksheet.cell_value(row,col)
        data.append(elm)
    print(data)
example3()
