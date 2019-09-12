import plotly.graph_objects as go
# z = [[1,20,30,50,1],[20,1,60,80,30],[30,60,1,-10,20]]
# x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# y=['Morning', 'Afternoon', 'Evening']
# fig = go.Figure(data=go.Heatmap(z,x,y))
# fig.show()
fig = go.Figure(data=go.Heatmap(
                   z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening']))
                   # z=[16,1,7,9,5,3,1,1,13,2,14,9,7,5,2,4,3,3,3,6,2,3,7,3],
                   # x=['Python','AI ML Stack','Django','Java','Spring Boot','Angular JS','Node JS','PHP','Mongo DB','Influx DB','MySql / Postgress Sql','Warrior Framework','Robot Framework','AWS / Cloud','Optical','L2 / L3','IOT','Dockers','Kubernetes','Jenkins','QA-Web Automation','QA-API Automation','Messaging Kafka','ELK'],
                   # y=['Dark Green','Light green','One level below dark green','Dark Green','One level below dark green','One level below dark green','Light green','Above Light Green','Dark Green','Light green','Dark Green','Dark Green','One level below dark green','Light green','Light green','Light green','Light green','Above Light Green','Above Light Green','Above Light Green','One level below dark green','Light green','Light green','Light green']))
                   # z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   # x=[0,2,4,6,8,10,12,14,16,18],
                   # y=[4,8,12]))
fig.show()
