import plotly.graph_objects as go
import squarify
import openpyxl

data_names = []
data_values = []
data_color = []
try:
    wb = openpyxl.load_workbook('heat_map_task.xlsx')
    sheet = wb.active
    for value in sheet.iter_rows(min_row=3, max_row=200, min_col=1, max_col=3, values_only= True):
        try:
            if value[0] is not None and value[1] is not None and value[2] is not None:
                data_names.append(value[0])
                data_values.append(value[1])
                if value[2] == 'Dark Green':
                    data_color.append('rgb(0,150,0)')
                elif value[2] == 'One level below dark green':
                    data_color.append('rgb(0,225,0)')
                elif value[2] == 'Above Light Green':
                    data_color.append('rgb(150,255,150)')
                elif value[2] == 'Light green':
                    data_color.append('rgb(229,255,229)')
                else:
                    pass
        except Exception:
            continue
    # print(data_names, data_values, data_color)
    fig = go.Figure()
    x = 0.
    y = 0.
    width = 15.
    height = 15.
    normed = squarify.normalize_sizes(data_values , width , height)
    rects = squarify.squarify(normed,x,y,width,height)
    color_brewer = data_color
    shapes=[]
    annotations = []
    counter=0

    pos=0
    for r, val, color in zip(rects, data_values, color_brewer):
        shapes.append(
            dict(
                type = 'rect',
                x0 = r['x'],
                y0 = r['y'],
                x1 = r['x']+r['dx'],
                y1 = r['y']+r['dy'],
                line = dict( width = 2 ),
                fillcolor = color
            )
        )

        annotations.append(
            dict(
                x = r['x']+(r['dx']/2),
                y = r['y']+(r['dy']/2),
                # text = val,
                text = str(data_names[pos])+' ('+str(val)+')',
                showarrow = False
            )
        )
        pos += 1

    # For hover text
    fig.add_trace(go.Scatter(x = [ r['x']+(r['dx']/2) for r in rects ],
                             y = [ r['y']+(r['dy']/2) for r in rects ],
                             text = [ str(v) for v in data_values ],
                             mode = 'text',))

    fig.update_layout(height=650,
                      width=1300,
                      xaxis=dict(showgrid=False,zeroline=False),
                      yaxis=dict(showgrid=False,zeroline=False),
                      shapes=shapes,
                      annotations=annotations,
                      hovermode='closest')
    fig.show()
except Exception as e:
    print('Exception Raised')