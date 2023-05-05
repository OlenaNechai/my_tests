import pymongo


class BaseMongoClient:
    __base_client = pymongo.MongoClient("mongodb://localhost:27017/")

    @staticmethod
    def get_base_client():
        return BaseMongoClient.__base_client

    @staticmethod
    def close_connection():
        return BaseMongoClient.__base_client.close()
