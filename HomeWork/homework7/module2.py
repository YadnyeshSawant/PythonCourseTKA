class Employee:
    def __init__(self,n,s,ph):
        self.name = n
        self.salary = s
        self.phone = ph
    
    def display(self):
        print(f"Name   ->  {self.name}")
        print(f"Salary ->  {self.salary}")
        print(f"Phone  ->  {self.phone.mobile_no}  {self.phone.email}")
