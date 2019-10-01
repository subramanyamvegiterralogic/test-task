import mysql.connector
from mini_project import error_logger
class Database():

    def __init__(self):
        self.error_log = error_logger.ReportError()
    # Connecting Database Connection
    def connect_db(self):
        try:
            global my_connect
            global my_cursor
            my_connect = mysql.connector.connect(host='localhost', database='mini_project', user='root', password='')
            my_cursor = my_connect.cursor()
            return my_cursor
        except Exception as e:
            # print(e)
            self.error_log.report_error_log(__file__, e.__str__())
            return None


    # Database Connection and Cursor Closing
    def disconnect_db(self):
        try:
            my_cursor.close()
            my_connect.close()
        except Exception as e:
            # print(e)
            self.error_log.report_error_log(__file__, e.__str__())

    # Common Select Query for All Methods
    def get_data_for_query(self, query):
        try:
            my_cursor.execute(query)
            return my_cursor.fetchall()
        except Exception as e:
            # print(e)
            self.error_log.report_error_log(__file__, e.__str__())
            return None

    # Common Insert/Update Query for all methods
    def insert_or_update_query(self, query):
        try:
            my_cursor.execute(query)
            my_connect.commit()
        except Exception as e:
            # print(e)
            self.error_log.report_error_log(__file__, e.__str__())
