from homework_23.base_data_base import BooksDB


class FantasyCollection(BooksDB):
    __fantasy_col = BooksDB.get_books_db()["fantasy"]

    @staticmethod
    def get_collection():
        return FantasyCollection.__fantasy_col

    def insert_one(self, data):
        return self.__fantasy_col.insert_one(data)

    def insert_many(self, data_dict):
        return self.__fantasy_col.insert_many(data_dict)

    def find_one(self, query):
        return self.__fantasy_col.find_one(query)

    def find_all(self):
        for doc in self.__fantasy_col.find():
            print(doc)

    def delete_one(self, my_query: dict):
        result = self.__fantasy_col.delete_one(my_query)
        print(result.deleted_count, "documents deleted")

    def delete_many(self):
        result = self.__fantasy_col.delete_many({})
        print(result.deleted_count, "documents deleted")
