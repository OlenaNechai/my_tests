from homework_22.db_repositories.order_repository import OrderRepository
from homework_22.db_repositories.product_repository import ProductRepository

product_repo = ProductRepository()
order_repo = OrderRepository()

if __name__ == '__main__':
    for product in product_repo.get_all_products():
        print(product)
    for order in order_repo.get_all_orders():
        print(order)
    print(product_repo.get_total_sum())
