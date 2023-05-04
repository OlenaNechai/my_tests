from homework_23.base_collection import FantasyCollection
from homework_23.base_data_base import BooksDB

if __name__ == '__main__':
    some_db = BooksDB()
    some_col = FantasyCollection()
    data = {"name": "Lord of the Rings", "author": "John Ronald Reuel Tolkien", "first_published": "29 July 1954"}
    some_col.insert_one(data)
    data_dict = [
        {"name": "The Fellowship of the Ring", "author": "John Ronald Reuel Tolkien",
         "first_published": "29 July 1954"},
        {"name": "The The Two Towers", "author": "John Ronald Reuel Tolkien", "first_published": "11 November 1954"},
        {"name": "The Return of the King", "author": "John Ronald Reuel Tolkien", "first_published": "20 October 1955"}
    ]
    some_col.insert_many(data_dict)
    some_col.find_all()
    print(some_col.find_one({"name": "Lord of the Rings"}))
    some_col.delete_one({"name": "The The Two Towers"})
    some_col.delete_many()
    some_col.find_all()
    some_col.close_connection()
