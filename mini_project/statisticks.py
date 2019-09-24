import plotly.graph_objects as go
from mini_project import database_connection

try:
    db = database_connection.Database()
    db.connect_db()
    query = 'SELECT transaction_date,COUNT(transaction_id) FROM user_transaction GROUP BY transaction_date'
    data_list = db.get_data_for_query(query)
    db.disconnect_db()
    data_dict = {}
    for objs in data_list:
        data_dict[objs[0]] = objs[1]

    x = [x for x in data_dict.keys()]
    y = [y for y in data_dict.values()]
    fig = go.Figure([go.Bar(x=x, y=y)])
    fig.show()
except Exception as e:
    print(e)
