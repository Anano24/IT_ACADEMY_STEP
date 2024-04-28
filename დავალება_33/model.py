from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = 'localhost'
PORT = 5432
DATABASE = 'employee'
USER = 'postgres'
PASSWORD = '...anano24'

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
Base = declarative_base()



class Department(Base):
    __tablename__ = 'department'

    departmentid = Column('departmentid', Integer, primary_key=True, autoincrement=True)
    departmentname = Column('departmentname', String(30))



class Employee(Base):
    __tablename__ = 'employee'

    employeeid = Column('employeeid', Integer, primary_key=True, autoincrement=True)
    fullname = Column('fullname', String(50))
    hiredate = Column('hiredate', Date)
    departmentid = Column('departmentid', Integer, ForeignKey(Department.departmentid))



Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


