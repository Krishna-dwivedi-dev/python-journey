# =============================================
# Day 8: Polymorphism - Method Overriding
# =============================================

# -----------------------------------------
# Q1 & Q2: Employee Salary System
# -----------------------------------------
class Employee:
    def calculate_salary(self):
        print("Salary not implemented")

class FullTime(Employee):
    def calculate_salary(self):
        self.salary = 55000
        print(f"Full Time Salary: [{self.salary}]")

class PartTime(Employee):
    def __init__(self, working_time):
        self.working_time = working_time
    def calculate_salary(self):
        if self.working_time > 6:
            self.salary = 40000
            print(f"Part Time Salary; [{self.salary}]")
        else:
            self.salary = 15000
            print(f"salary will be; [{self.salary}]")

class freelancer(Employee):
    def __init__(self, project_cost, numberof_project):
        self.project_cost = project_cost
        self.numberof_project = numberof_project
    def calculate_salary(self):
        print(f"my salary is: [{self.project_cost * self.numberof_project}]")

Salary = [FullTime(), PartTime(10), freelancer(5000, 10)]
for Employee in Salary:
    Employee.calculate_salary()


# -------------------------------------------
# Q3: Notification System
# -------------------------------------------
class Notification:
    def send(self, message):
        self.message = message

class Email(Notification):
    def send(self, message):
        print(f"Email is Sent: [{message}]")

class SMS(Notification):
    def send(self, message):
        print(f"SMS is sent: [{message}]")

class PushNotification(Notification):
    def send(self, message):
        print(f"Notification is sent: [{message}]")

send = [Email(), SMS(), PushNotification()]
message = ["Hello! I'm Krishna Dwivedi", "Hey there! I'm Rahul Sukla", "hi I am Manisha Dwivedi"]
for i, Notification in enumerate(send):
    Notification.send(message[i])
































    