import pymongo
from faker import Faker
import random
city_list = ['Australia', 'Bangalore', 'Chennai', 'Dallas', 'Hyderabad', 'Mumbai', 'Pune', 'San Jose',  'Vietnam']
fake_data = Faker()


def insert_data_into_mongo_db(employee_list):
    try:
        my_client = pymongo.MongoClient('mongodb://localhost:27017/')
        my_db = my_client['SpringBoot_Employee']
        my_collection = my_db['employee']
        my_collection.insert_many(employee_list)
    except Exception as e:
        print(e)


def generate_employee_fake_data(employee_count):
    try:
        employee_list = []
        for i in range (employee_count):
            emp = dict()
            emp['emp_name'] = fake_data.name()
            emp['emp_id'] = random.randrange(1000,99999,3)
            emp['emp_city'] = random.choice(city_list)
            emp['emp_age'] = random.randint(22,40)
            employee_list.append(emp)
            print(i)
        return employee_list
    except Exception as e:
        print(e)
        return e.__str__()


insert_data_into_mongo_db(generate_employee_fake_data(10000))
