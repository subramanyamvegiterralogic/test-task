import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd

df2 = pd.read_csv('coffee-flavors.csv')

fig = make_subplots(
    rows = 1, cols = 2,
    column_widths = [0.4, 0.4],
    specs = [[{'type': 'treemap', 'rowspan': 1}, {'type': 'treemap'}]]
)

fig.add_trace(
    go.Treemap(
        ids = df2.ids,
        labels = df2.labels,
        parents = df2.parents,
        maxdepth = 3),
    col = 1, row = 1)

fig.update_layout(
    margin = {'t':0, 'l':0, 'r':0, 'b':0}
)

fig.show()