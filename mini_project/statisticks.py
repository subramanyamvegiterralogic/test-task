import plotly.graph_objects as go
from mini_project import database_connection, error_logger
import datetime
import threading
db = database_connection.Database()
class GraphicalRepresentation:
    def __init__(self):
        self.error_log = error_logger.ReportError()
    def bar_chart_representation(self):
        try:
            db.connect_db()
            current_date = datetime.date.today()
            start_date = current_date-datetime.timedelta(days=15)
            query = "SELECT transaction_date,COUNT(transaction_id) FROM user_transaction WHERE transaction_date BETWEEN '{}' AND '{}' GROUP BY transaction_date".format(start_date,current_date)
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
        finally:
            db.disconnect_db()

    def statistic_line_representation(self):
        try:
            db.connect_db()
            query = 'SELECT transaction_date,COUNT(transaction_id) FROM user_transaction GROUP BY transaction_date'
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
        finally:
            db.disconnect_db()
# gr = GraphicalRepresentation()
# t1=threading.Thread(target=gr.statistic_line_representation()).start()
# t2=threading.Thread(target=gr.bar_chart_representation()).start()