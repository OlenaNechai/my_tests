from homework_22.session import session
from homework_22.models.product_order import Product, Order


class ProductRepository:
    def __init__(self):
        self.__session = session

    def get_product_by_id(self, id_value):
        return self.__session.get(Product, {'id': id_value})

    def get_all_products(self):
        all_products = self.__session.query(Product).all()
        return all_products

    def insert_one(self, product: Product):
        self.__session.add(product)
        self.__session.commit()

    def get_product_by_name(self, name: str):
        product = self.__session.query(Product).filter_by(name=name).first()
        return product

    def get_total_sum(self):
        for p, o in self.__session.query(Product, Order).filter(Product.id == Order.product_id).all():
            print(f"name: {p.name} price: {p.price} quantity: {o.quantity} total: {p.price * o.quantity}")
