# Hw Task 2: An Employee has name, salary and phone. Phone means mobile number, email address. employee has one operation which displays salary and email and name of employee.


class Employee:
    name = "Yadnyesh Sawant"
    salary = 120000
    phone = {"mobileNumber": 8576940375, "email": "yadnyesh2022@gmil.com"}

    def displayInfo(*args):
        print("Employee Details")

        if "name" in args:
            print(f"Employee Name: {Employee.name}")

        if "salary" in args:
            print(f"Employee Salary: {Employee.salary}")

        if "phone" in args:
            # print(f"Employee Phone: {Employee.phone}")
            for k, v in Employee.phone.items():
                print(f"{k} : {v}")
                
        else:
            print(f"Employee Name: {Employee.name}")
            print(f"Employee Salary: {Employee.salary}")
            # print(f"Employee Phone:{Employee.phone}")
            for k, v in Employee.phone.items():
                print(f"{k} : {v}")


emp = Employee()
print("If argumaents passed")
emp.displayInfo("name")
emp.displayInfo("salary")
emp.displayInfo("phone")

print("\nIf argument not passed")
emp.displayInfo()

##################################################################

# OUTPUT

# If argumaents passed
# Employee Details
# Employee Name: Yadnyesh Sawant

# Employee Details
# Employee Salary: 120000

# Employee Details
# mobileNumber : 8576940375
# email : yadnyesh2022@gmil.com

# If argument not passed

# Employee Details
# Employee Name: Yadnyesh Sawant
# Employee Salary: 120000
# mobileNumber : 8576940375
# email : yadnyesh2022@gmil.com

#################################################################
