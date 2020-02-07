class Employee:
    empCount = 0
    sum = 0
    avg = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.empCount += 1
        Employee.avgSal(salary)

    def avgSal(salary):
        Employee.sum += salary
        Employee.avg = Employee.sum / Employee.empCount


class fulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


emp = Employee("Jai", "Koya", 5000, "Development")
emp = Employee("Sekhar","Koya", 6000, "IT")
full = fulltimeEmployee("Khan","Joe",8000,"Code")
print(full.name)
print("Average Salary:",Employee.avg)
print("Employee COunt:",Employee.empCount)
