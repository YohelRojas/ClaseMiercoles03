from pymongo import MongoClient
from decouple import config
import logging
from bson.objectid import ObjectId


class Connection:

    def __init__(self, collection_name):
        self.collection = None
        self.db = None
        self.connect(collection_name)

    def connect(self, collection_name):
        uri = config("MONGO_URL")
        db = config("MONGO_DB")
        self.collection = MongoClient(uri)[db][collection_name]

    def get_all_data(self):
        try:
            result = self.collection.find({})
        except Exception as e:
            raise Exception(e)
        return result

    def find_one(self, name):
        try:
            result = self.collection.find_one(name)
            return result
        except Exception as e:
            logging.exception(e)
            raise Exception(e)

    def get_by_id(self, id):
        try:
            result = self.collection.find_one({"_id": ObjectId(id)})
        except Exception as e:
            raise Exception(e)
        return result
    
    def get_by_query(self, query):
        try:
            result = self.collection.find(query)
            return result
        except Exception as e:
            logging.error(f"Database error in get_by_query: {e}")
            raise Exception(e)

    def create_data(self, data):
        try:
            return self.collection.insert_one(data)
        except Exception as e:
            raise Exception(e)

    def update_data(self, id, new_data):
        try:
            result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": new_data})
            return result.modified_count > 0
        except Exception as e:
            logging.exception(e)
            raise Exception(e)

    def update_by_condition(self, condition, new_data):
        try:
            self.collection.update_one(condition, {"$set": new_data})
        except Exception as e:
            raise Exception(e)

    def delete_data(self, id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count > 0:
                return True
            else:
                return False
        except Exception as e:
            raise Exception(e)
        

    def get_by_query(self, query):
        try:
            result = self.collection.find(query)
            return list(result)
        except Exception as e:
            logging.exception(e)
            raise Exception(e)
