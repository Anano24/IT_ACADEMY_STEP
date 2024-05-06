from sqlalchemy import Column, Integer, String, ForeignKey, Double, Date
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()



class Categories(Base):
    __tablename__ = 'categories'

    category_id = Column('category_id', Integer, primary_key=True, autoincrement=True)
    category_name = Column('category_name', String(30))


    
    def insert_category(self, session, category_name):
        new_category = Categories(category_name=category_name)

        session.add(new_category)
        session.commit()



class Products(Base):
    __tablename__ = 'products'

    product_id = Column('product_id', Integer, primary_key=True, autoincrement=True)
    product_name = Column('product_name', String(40))
    product_price = Column('product_price', Double)
    stock_quantity = Column('stock_quantity', Integer)
    category_id = Column('category_id', Integer, ForeignKey(Categories.category_id))

  

    def insert_product(self, session, product_name, price, stock_quantity, category):
        new_product = Products(product_name=product_name,
                               product_price=price,
                               stock_quantity=stock_quantity,
                               category_id=category)
        
        session.add(new_product)
        session.commit()

    
    
    def delete_product(self, session, product_name):
        product = session.query(Products).filter_by(product_name=product_name).first()

        if product:
            session.delete(product)
            session.commit()
        else:
            print('Product not found')


   
    def update_product(self, session, product_name, new_name):
        products = session.query(Products).filter_by(product_name=product_name).all()
        if products:
            for product in products:
                product.product_name = new_name
            session.commit()
        else:
            print('Product not found')


    

class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column('order_id', Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id', Integer, ForeignKey(Products.product_id))
    quantity = Column('quantity', Integer)
    order_date = Column('order_date', Date)
    status = Column('status', String(30))


   
    def make_order(self, session, product_id, quantity, order_date, status):

        product = session.query(Products).filter_by(product_id=product_id).first()

        if product and product.stock_quantity >= quantity:
            new_quantity = product.stock_quantity - quantity
            product.stock_quantity = new_quantity
            new_order = Orders(product_id=product_id,
                           quantity=quantity,
                           order_date=order_date,
                           status=status)
            session.add(new_order)
            session.commit()
            print("Order placed successfully.")
        else:
            print("Unable to place order due to insufficient quantity.")
            
            







