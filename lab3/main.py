from person import Person
from Employee import Employee
from office import Office

employees = []
employees.append(Employee("abdo",10000,10,200))
employees.append(Employee("sayed",20000,20,100))


office=Office("software",employees)
print(office.get_All_employees())



