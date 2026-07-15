# Creating an Employee class 
class Employee():
    # Using a constructor to give attributes to instances
    def __init__(self,name,emp_id,salary):      #Here Magic Variable is used
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    # Initiating a 'Static Variable' for Demonstration
    company = "Spacex"
    # Creating a Method which prints out all attributes of an object
    def display(self):
        print(f"Name : {self.name}\nEmp_ID : {self.emp_id} \nSalary : {self.salary}")

Objects = [] # Using Global list
def add_object_to_Employee(n):
    for i in range(1,n+1):
        emp = Employee(input("Enter name:"),int(input("Enter Employee id: ")),input("Enter Salary:"))
        Objects.append(emp)
    

add_object_to_Employee(int(input("Enter the number of employee you want to store:")))
for el in Objects:
    el.display()