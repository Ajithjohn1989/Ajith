class Company:
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def display_company_details(self):
   print(f"Company Name: {self.name}")
   print(f"Location: {self.location}")

# Intermediate class inheriting from Company
class Department(Company):
  def __init__(self, name, location, department_name):
   super().__init__(name, location)
   self.department_name = department_name

  def display_department_details(self):
   print(f"Department: {self.department_name}")

# Derived class inheriting from Department
class Employee(Department):
   def __init__(self, name, location, department_name, employee_name, employee_id):
    super().__init__(name, location, department_name)
    self.employee_name = employee_name
    self.employee_id = employee_id

   def display_employee_details(self):
    print(f"Employee Name: {self.employee_name}")
    print(f"Employee ID: {self.employee_id}")

# Creating an instance of the Employee class
employee = Employee("TechCorp", "New York", "Planning", "Ajith John", 12345)

# Accessing methods from all levels of inheritance
employee.display_company_details()
employee.display_department_details()
employee.display_employee_details()
