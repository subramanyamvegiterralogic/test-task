import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import IFrame

def ex1():
    labels = ['O2','H2','Co2','N2']
    values = [4500, 2500, 1053, 500]

    fig = go.Figure(data=[go.Pie(labels= labels, values= values)])
    fig.show()
# ex1()

def ex2():
    colors = ['darkgreen', 'green', 'lightgreen', 'skyblue']
    fig = go.Figure(data=[go.Pie(labels=['Oxyzen', 'Hydrogen','Carbon_dioxide','Nitrogen'],values=[4500, 2500, 1053, 500])])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size = 20,
                      marker = dict(colors= colors,
                                    line = dict(color = '#FF6781', width=2)))
    fig.show()
# ex2()

def ex3():
  labels = ['Cricket' , 'Hockey' , 'Tennis / Shettle', 'Football']
  values = [4500, 2500, 1053, 500]
  fig = go.Figure(data=[go.Pie(labels= labels, values= values, hole=0.3)])
  fig.show()
# ex3()

def ex4():
    labels = ['US', 'China', 'European Union', 'Russian Federation', 'Brazil', 'India', 'Rest Of World']

    fig = make_subplots(rows=1, cols=2, specs=[[{'type' : 'domain'}, {'type' : 'domain'}]])
    fig.add_trace(go.Pie(labels= labels, values=[16, 15, 12, 6, 5, 4, 42], name='GHG Emissions'), 1, 1)
    fig.add_trace(go.Pie(labels= labels, values=[27, 12, 25, 8, 1, 3, 25], name='Co2 Emissions'),1,2)
    fig.update_traces(hole=0.4, hoverinfo='label+percent+name')

    fig.update_layout(title_text='Global Emissions 1990-2011',
                      annotations=[dict(text='GHG', x=0.18, y=0.5, font_size=20, showarrow=False),
                                   dict(text='Co2', x=0.82, y=0.5, font_size=20, showarrow=False)])
    fig.show()
# ex4()

def ex5():
    labels = ['1st', '2nd', '3rd', '4th', '5th']
    night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)',
                    'rgb(36, 55, 57)', 'rgb(6, 4, 4)']
    sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)',
                         'rgb(129, 180, 179)', 'rgb(124, 103, 37)']
    irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                     'rgb(175, 49, 35)', 'rgb(36, 73, 147)']
    cafe_colors = ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)',
                   'rgb(175, 51, 21)', 'rgb(35, 36, 21)']

    # Create subplots, using 'domain' type for pie charts
    specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]]
    fig = make_subplots(rows=2, cols=2, specs=specs)

    # Define pie charts
    fig.add_trace(go.Pie(labels = labels, values = [38, 27, 18, 10, 7], name='Starry Night', marker_colors = night_colors),1,1)
    fig.add_trace(go.Pie(labels = labels, values = [28, 26, 21, 15, 10], name='Sun Flowers', marker_colors = sunflowers_colors),1,2)
    fig.add_trace(go.Pie(labels = labels, values = [30, 19, 16, 14, 13], name='Irises', marker_colors = irises_colors),2,1)
    fig.add_trace(go.Pie(labels = labels, values = [31, 24, 19, 18, 8], name='The Night Kafe', marker_colors = cafe_colors),2,2)

    # Tune layout and hover info
    fig.update_traces(hoverinfo = 'label+percent+name', textinfo = 'none')
    fig.update(layout_title_text = 'Van Gogh: 5 Most Prominent Colors Shown Proportionally', layout_showlegend=False)
    fig = go.Figure(fig)
    fig.show()
# ex5()

def ex6():
    labels = ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']
    fig = make_subplots(1,2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                        subplot_titles=['1980','2018'])
    fig.add_trace(go.Pie(labels = labels, values = [4, 7, 1, 7, 0.5], scalegroup = 'one', name='World GDP 1980'),1,1)
    fig.add_trace(go.Pie(labels = labels, values = [21, 15, 3, 19, 1], scalegroup = 'one', name='World GDP 2018'),1,2)
    fig.update_layout(title_text='World GDP')
    fig.show()
# ex6()

def ex7():
    IFrame(src="https://dash-simple-apps.plotly.host/dash-pieplot", width="100%", height="650px", frameBorder="0")
ex7()