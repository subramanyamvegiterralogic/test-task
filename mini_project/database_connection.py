import mysql.connector

class Database():

    # Connecting Database Connection
    def connect_db(self):
        try:
            global my_connect
            global my_cursor
            my_connect = mysql.connector.connect(host='localhost', database='mini_project', user='root', password='')
            my_cursor = my_connect.cursor()
            return my_cursor
        except Exception as e:
            print(e)
            return None


    # Database Connection and Cursor Closing
    def disconnect_db(self):
        try:
            my_cursor.close()
            my_connect.close()
        except Exception as e:
            print(e)

    # Common Select Query for All Methods
    def get_data_for_query(self, query):
        try:
            my_cursor.execute(query)
            return my_cursor.fetchall()
        except Exception as e:
            print(e)
            return None

    # Common Insert/Update Query for all methods
    def insert_or_update_query(self, query):
        try:
            my_cursor.execute(query)
            my_connect.commit()
        except Exception as e:
            print(e)
