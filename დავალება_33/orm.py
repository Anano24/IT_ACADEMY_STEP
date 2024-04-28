from model import session, Employee, Department


joined_query = session.query(Employee.fullname, Employee.hiredate, Department.departmentname).join(Department).all()

for data in joined_query:
    print(data)

