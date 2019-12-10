import plotly.graph_objects as go

labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]
marker_colors = ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgreen", "lightblue"]

fig = go.Figure(go.Treemap(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    marker_colors = marker_colors))

fig.show()