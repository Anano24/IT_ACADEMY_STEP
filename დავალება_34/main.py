from model import Base, Products, Categories, Orders
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



HOST = 'localhost'
PORT = 5432
DATABASE = 'product'
USER = 'postgres'
PASSWORD = '...anano24'

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


category = Categories()
# category.insert_category(session, 'Dresses')
# category.insert_category(session, 'Accessories')
# category.insert_category(session, 'Pants')
# category.insert_category(session, 'Shoes')

product = Products()
# product.insert_product(session, 'Red dress', 200.5, 15, 1)
# product.insert_product(session, 'Black hat', 100, 5, 2)
# product.insert_product(session, 'Blue Trousers', 315, 10, 3)
# product.insert_product(session, 'sunglasses', 250, 12, 2)
# product.insert_product(session,'sandals', 350, 6, 4)

# product.delete_product(session, 'Black hat')

# product.update_product(session, 'Blue Trousers', 'Green Trousers')

order = Orders()
# order.make_order(session, 1, 3, '2024-04-29', 'panding')
# order.make_order(session, 4, 2, '2024-04-30', 'panding')
# order.make_order(session, 5, 10, '2024-04-30', 'delivered')
# order.make_order(session, 4, 2, '2024-04-29', 'panding')



joined_query = session.query(Products, Categories, Orders).\
    join(Orders, Orders.product_id == Products.product_id).\
    join(Categories, Products.category_id == Categories.category_id).\
    filter(Orders.status == 'panding').all()


for product, category, order in joined_query:
    print("Product:", product.product_name)
    print("Stock_quantity:", product.stock_quantity)
    print("Category:", category.category_name)
    print("Order Quantity:", order.quantity)
    print("Order Date:", order.order_date)
    print("Status:", order.status)
    print()



