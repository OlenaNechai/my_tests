from homework_22.session import session
from homework_22.models.product_order import Order


class OrderRepository:
    def __init__(self):
        self.__session = session

    def get_order_by_id(self, id_value):
        return self.__session.get(Order, {'id': id_value})

    def get_all_orders(self):
        all_orders = self.__session.query(Order).all()
        return all_orders

    def insert_one(self, order: Order):
        self.__session.add(order)
        self.__session.commit()

    def get_order_by_product_id(self, product_id: int):
        order = self.__session.query(Order).filter_by(product_id=product_id).first()
        return order
