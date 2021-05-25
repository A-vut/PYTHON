class Salary:
    def __init__(self, pay, bonus):
        self.pay=pay
        self.bonus=bonus
    def anual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.obj_salary=salary

    def total_salary(self):
        return self.obj_salary.anual_salary()

salary=Salary(33000,550)

emp=Employee("Mehedi",25,salary)
print(emp.total_salary())
 

