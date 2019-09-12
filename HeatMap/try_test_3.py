# import numpy as np
# M = np.random.randint(0, high=500, size=(50,4))
# R = np.zeros((500,500))
# for row in M:
#     x1, y1, x2, y2 = row
#     for x in range(x1,x2+1):
#         for y in range(y1,y2+1):
#             R[x,y] += 1
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.heatmap(R)
# plt.show()
import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
                    z=[[1, 20, 30],
                      [20, 1, 60],
                      [30, 60, 1]]))
fig.show()
