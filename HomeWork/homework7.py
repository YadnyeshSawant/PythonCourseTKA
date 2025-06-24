# Hw Task 2: An Employee has name, salary and phone. Phone means mobile number, email address. employee has one operation which displays salary and email and name of employee. 

class Employee:
    name ="Yadnyesh Sawant"
    salary = 120000
    phone = {"mobileNumber": 8576940375, "email":"yadnyesh2022@gmil.com"}
    
    def displayInfo(*args):
        print("Employee Details")
        if "name" in args:
            print(f"Employee Name: {Employee.name}")
            
        if "salary" in args:
            print(f"Employee Salary: {Employee.salary}")
            
        if "mobileNumber" in args:
            print(f"Employee Mobile Number: {Employee.mobileNumber}")
            
        if "email" in args:
            print(f"Employee Email Address: {Employee.email}")
            
        if not args:
            print(f"Employee Name: {Employee.name}")
            print(f"Employee Salary: {Employee.salary}")
            print(f"Employee Phone: {Employee.phone}")
            # print(f"Employee Email Address: {Employee.email}")


print("If argumaents passed")
Employee.displayInfo("name")
Employee.displayInfo("salary")
Employee.displayInfo("phone")

print("\nIf argument not passed")
Employee.displayInfo()

##################################################################

# OUTPUT

# If argumaents passed
# Employee Details
# Employee Name: Yadnyesh Sawant

# Employee Details
# Employee Salary: 120000

# Employee Details
# Employee Email Address: yadnyesh2022@gmil.com

# If argument not passed
# Employee Details
# Employee Name: Yadnyesh Sawant
# Employee Salary: 120000
# Employee Mobile Number: 8576940375
# Employee Email Address: yadnyesh2022@gmil.com

#################################################################
