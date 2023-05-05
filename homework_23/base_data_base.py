from homework_23.base_mongo_client import BaseMongoClient


class BooksDB(BaseMongoClient):
    __books_db = BaseMongoClient.get_base_client()["books"]

    @staticmethod
    def get_books_db():
        return BooksDB.__books_db
