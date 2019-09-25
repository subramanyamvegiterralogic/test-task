import mysql.connector
import random
from datetime import datetime

date_list = ['2019-09-25','2019-09-24','2019-09-23','2019-09-22','2019-09-21','2019-09-20','2019-09-19',
             '2019-09-18','2019-09-17','2019-09-16', '2019-09-15', '2019-09-14','2019-09-13','2019-09-12',
             '2019-09-11','2019-09-10','2019-09-09','2019-09-08','2019-09-07','2019-09-06' ,'2019-09-05',
             '2019-09-04','2019-09-03', '2019-09-02', '2019-09-01','2019-08-31','2019-08-30','2019-08-29']


def generate_transaction_id():
    try:
        transaction_id = ''
        for num in range(0, 10):
            transaction_id += str(random.randint(0, 9))
        return transaction_id
    except Exception as e:
        print(e)
my_connection = mysql.connector.connect(host='localhost', database='mini_project', user='root',password='')
my_cursor = my_connection.cursor()
for i in range (0,100):
    transaction_id = generate_transaction_id()
    transaction_amount = random.randint(1,100000)
    transaction_date = random.choice(date_list)
    query = "INSERT INTO user_transaction VALUES ('{}','{}','{}')".format(transaction_id, transaction_amount, transaction_date)
    my_cursor.execute(query)
    print(i)
my_connection.commit()
my_cursor.close()
my_connection.close()
