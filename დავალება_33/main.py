import psycopg2


HOST = 'localhost'
PORT = 5432
DATABASE = 'employee'
USER = 'postgres'
PASSWORD = '...anano24'

conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)
cursor = conn.cursor()


insert_departments = "INSERT INTO department (departmentname) VALUES ('Marketing'), ('IT')"
insert_employees = "INSERT INTO employee (fullname, hiredate, departmentid) VALUES ('John Mekesh', '2023-03-28', 4), ('Mary Mekesh', '2015-03-28', 3)"

cursor.execute(insert_departments)
cursor.execute(insert_employees)

select_query = "SELECT fullname, hiredate, departmentname FROM employee inner join department on employee.departmentid = department.departmentid"
cursor.execute(select_query)

result = cursor.fetchall()
for data in result:
    print(data)

conn.commit()

cursor.close()
conn.close()