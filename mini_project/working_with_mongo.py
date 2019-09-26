import pymongo

class MongoOperations:
    def __init__(self):
        self.my_client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.my_db = self.my_client['mini_project']
        self.db_list = self.my_client.list_database_names()
        self.my_collection = self.my_db['user_transaction']

    def insert_one_record_into_collection(self,transaction_data):
        x=self.my_collection.insert_one(transaction_data)
        # print(x)

    def insert_many_records_into_collection(self, transaction_data):
        x = self.my_collection.insert_many(transaction_data)
        # print(x)

    def find_one(self):
        print(self.my_collection.find_one())

    def find_all(self):
        for item in self.my_collection.find():
            print(item)

    def normal_query(self):
        my_query = {'item_name':'Almonds'}
        my_doc = self.my_collection.find(my_query)
        for x in my_doc:
            print(x)

    def advanced_query(self):
        my_query = {'item_total_amount': {"$gte" : 1340}}
        my_doc = self.my_collection.find(my_query)
        for x in my_doc:
            print(x)

    def regex_query(self):
        my_query = {'transaction_id': {'$regex' : '^\d+44\d+'}}
        my_doc = self.my_collection.find(my_query)
        for x in my_doc:
            print(x)

    def asc_sort(self):
        my_doc=self.my_collection.find().sort('item_total_amount')
        for item in my_doc:
            print(item)

    def desc_sort(self):
        my_doc = self.my_collection.find().sort('item_total_amount',-1)
        for item in my_doc:
            print(item)

    def delete_one_record_from_collection(self):
        my_query = {'transaction_id':'7894412459'}
        self.my_collection.delete_one(my_query)

    def delete_many_records_from_collection(self):
        my_query = {'transaction_id':{'$regex':"\d+44\d+"}}
        x= self.my_collection.delete_many(my_query)
        print(x)

    def drop_collection(self):
        self.my_collection.drop()

# my_mongo = MongoOperations()
# transaction_data = [{'transaction_id':'1014412459', 'item_name':'Banana', 'item_price':34, 'item_quantity':4, 'item_total_amount':136},
#                     {'transaction_id':'1014412459', 'item_name':'Almonds', 'item_price':670, 'item_quantity':2, 'item_total_amount':1340},
#                     {'transaction_id':'1014412459', 'item_name':'Dry Fruits Mix', 'item_price':989, 'item_quantity':1, 'item_total_amount':989},
#                     {'transaction_id':'1014412459', 'item_name':'Papaya', 'item_price':40, 'item_quantity':3, 'item_total_amount':120}]
# my_mongo.insert_one_record_into_collection(transaction_data)
# my_mongo.insert_many_records_into_collection(transaction_data)
# my_mongo.find_one()
# my_mongo.find_all()
# my_mongo.normal_query()
# my_mongo.advanced_query()
# my_mongo.regex_query()
# my_mongo.asc_sort()
# my_mongo.desc_sort()
# my_mongo.delete_one_record_from_collection()
# my_mongo.delete_many_records_from_collection()
# my_mongo.drop_collection()