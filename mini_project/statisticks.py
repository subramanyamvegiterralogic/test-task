import plotly.graph_objects as go
from mini_project import database_connection, error_logger
import datetime
# import squarify
db = database_connection.Database()
class GraphicalRepresentation:
    def __init__(self):
        self.error_log = error_logger.ReportError()
        self.current_date = datetime.date.today()
        self.start_date = self.current_date-datetime.timedelta(days=15)

    def bar_chart_representation(self):
        try:
            db.connect_db()
            query = "SELECT transaction_date,COUNT(transaction_id) FROM user_transaction WHERE transaction_date BETWEEN '{}' AND '{}' GROUP BY transaction_date".format(self.start_date,self.current_date)
            data_list = db.get_data_for_query(query)
            data_dict = {}
            for objs in data_list:
                data_dict[objs[0]] = objs[1]

            x = [x for x in data_dict.keys()]
            y = [y for y in data_dict.values()]
            fig = go.Figure([go.Bar(x=x, y=y)])
            fig.show()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())

    def statistic_line_representation(self):
        try:
            db.connect_db()
            query = "SELECT transaction_date,COUNT(transaction_id) FROM user_transaction WHERE transaction_date BETWEEN '{}' AND '{}' GROUP BY transaction_date".format(self.start_date,self.current_date)
            data_list = db.get_data_for_query(query)
            data_dict = {}
            for objs in data_list:
                data_dict[objs[0]] = objs[1]

            x = [x for x in data_dict.keys()]
            y = [y for y in data_dict.values()]
            fig = go.Figure(data=[go.Scatter(x=x,y=y)])
            fig.show()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())


    def statistic_pie_chart_representation(self):
        try:
            db.connect_db()
            query = "SELECT transaction_date,COUNT(transaction_id) FROM user_transaction WHERE transaction_date BETWEEN '{}' AND '{}' GROUP BY transaction_date".format(self.start_date,self.current_date)
            data_list = db.get_data_for_query(query)
            data_dict = {}
            for objs in data_list:
                data_dict[objs[0]] = objs[1]
            labels = [x for x in data_dict.keys()]
            values = [y for y in data_dict.values()]
            fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
            fig.show()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())

    # def statistic_tree_map(self):
    #     data_names = []
    #     data_values = []
    #     data_color = []
    #     try:
    #         db.connect_db()
    #         query = "SELECT transaction_date,COUNT(transaction_id) FROM user_transaction WHERE transaction_date BETWEEN '{}' AND '{}' GROUP BY transaction_date".format(
    #             self.start_date, self.current_date)
    #         data_list = db.get_data_for_query(query)
    #         data_dict = {}
    #         for objs in data_list:
    #             data_dict[objs[0]] = objs[1]
    #         data_names = [x for x in data_dict.keys()]
    #         data_values = [y for y in data_dict.values()]
    #         for value in data_values:
    #             print(value)
    #             try:
    #                 if value is not None:
    #                     if int(value) >= 100:
    #                         data_color.append('rgb(0,100,0)')
    #                     elif int(value) > 75:
    #                         data_color.append('rgb(0,200,0)')
    #                     elif int(value) > 50:
    #                         data_color.append('rgb(0,255,0)')
    #                     elif int(value) > 25:
    #                         data_color.append('rgb(173,255,47)')
    #                     elif int(value)>0:
    #                         data_color.append('rgb(144,238,144)')
    #                     else:
    #                         pass
    #             except Exception as e:
    #                 continue
    #         # print(data_names, data_values, data_color)
    #         fig = go.Figure()
    #         x = 0.
    #         y = 0.
    #         width = 15.
    #         height = 15.
    #         normed = squarify.normalize_sizes(data_values, width, height)
    #         rects = squarify.squarify(normed, x, y, width, height)
    #         color_brewer = data_color
    #         shapes = []
    #         annotations = []
    #         counter = 0
    #
    #         pos = 0
    #         for r, val, color in zip(rects, data_values, color_brewer):
    #             shapes.append(
    #                 dict(
    #                     type='rect',
    #                     x0=r['x'],
    #                     y0=r['y'],
    #                     x1=r['x'] + r['dx'],
    #                     y1=r['y'] + r['dy'],
    #                     line=dict(width=2),
    #                     fillcolor=color
    #                 )
    #             )
    #
    #             annotations.append(
    #                 dict(
    #                     x=r['x'] + (r['dx'] / 2),
    #                     y=r['y'] + (r['dy'] / 2),
    #                     # text = val,
    #                     text=str(data_names[pos]) + ' (' + str(val) + ')',
    #                     showarrow=False
    #                 )
    #             )
    #             pos += 1
    #
    #         # For hover text
    #         fig.add_trace(go.Scatter(x=[r['x'] + (r['dx'] / 2) for r in rects],
    #                                  y=[r['y'] + (r['dy'] / 2) for r in rects],
    #                                  text=[str(v) for v in data_values],
    #                                  mode='text', ))
    #
    #         fig.update_layout(height=650,
    #                           width=1300,
    #                           xaxis=dict(showgrid=False, zeroline=False),
    #                           yaxis=dict(showgrid=False, zeroline=False),
    #                           shapes=shapes,
    #                           annotations=annotations,
    #                           hovermode='closest')
    #         fig.show()
    #     except FileNotFoundError:
    #         print('Seraching File Not Found')
    #     except Exception as e:
    #         print('Exception Raised')
# gr = GraphicalRepresentation()
# t1=threading.Thread(target=gr.statistic_line_representation()).start()
# t2=threading.Thread(target=gr.bar_chart_representation()).start()