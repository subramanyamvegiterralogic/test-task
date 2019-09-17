import plotly.graph_objects as go
# import openpyxl
# wb = openpyxl.load_workbook('heat_map_task.xlsx')
# sheet = wb.active
# data = []
# for value in sheet.iter_rows(min_row=3, max_row=30, min_col=1, max_col=3, values_only= True):
#     print(type(value))
#     if value[0] is not None:
#         data.append(value)
# print(data)
# import plotly.figure_factory as ff
z = [[70, 70, 70, 20, 20, 20, 40, 40, 0, 0, 0, 0],
     [70, 70, 70, 20, 20, 20, 40, 40, 0, 0, 0, 0],
     [70, 70, 70, 45, 45, 45, 25, 25, 0, 0, 0, 0],
     [70, 70, 70, 45, 45, 45, 25, 25, 0, 0, 0, 0],
     [50, 50, 50, 45, 45, 45, 25, 25, 0, 0, 0, 0],
     [50, 50, 50, 45, 45, 45, 25, 25, 0, 0, 0, 0],
     [50, 50, 50, 45, 45, 45, 10, 10, 0, 0, 0, 0],
     [50, 50, 50, 45, 45, 45, 10, 10, 0, 0, 0, 0],
     [87, 87, 87, 87, 20, 20, 10, 10, 0, 0, 0, 0],
     [87, 87, 87, 87, 20, 20, 30, 30, 0, 0, 0, 0],
     [87, 87, 87, 87, 20, 20, 30, 30, 0, 0, 0, 0],
     [87, 87, 87, 87, 20, 20, 30, 30, 0, 0, 0, 0]]
x = [x for x in range(1, 13, 1)]
y = [y for y in range(1, 13, 1)]
z_text = [['', '', '', '', '', '', '', '', 'Node JS (1)', 'Influx DB (1)','',''],
          ['', '', '', '', 'Robot Framework (6)', '', 'ELK (2)', 'Optical (20', 'ML (1)', ' PHP (1)', '', ''],
          ['', 'MySql (12)', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '','Web QA (2)', 'API QA (2)', 'Kubernetes (2)', 'IOT (2)', '', ''],
          ['', '', '', '', 'Warrior Framework (9)', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', 'L2/L3 (4)', '', 'Dockers (4)', '',  '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', ''],
          ['', 'Mongo DB(12)', '', '', 'Java (9)', '', 'Jenkins (6)', '', 'AWS (4)',  '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', 'Angular JS (4)', '', '', ''],
          ['','Python(16)','','','Kafka(8)','','DJango (6)','','','','','',],
          ['', '', '', '', '', '', '', '', 'Spring Boot (4)', '', '', '']]
fig = go.Figure(data=go.Heatmap(z=z, x=x, y=y,colorscale='Greens',text=z_text))
# fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale='Greens' )
fig.show()
