class Teacher:
    name = "atul sir"
    
    @classmethod
    def dipalayName(cls):  # class method to print the name of the teacher dclaredd as class var.
        print(f"Name of Teacher {cls.name:>20}")
        
    @staticmethod
    def calPercentage(student):
        
        student.details() # instance method from student object
        
        obatinedMarks = 0
        for v in student.subjectMarks.values():
            obatinedMarks += v
        totalMarks = len(student.subjectMarks)*100
        percentage = (obatinedMarks/totalMarks)*100
        
        print(f"percentage = {percentage:>20.2f} %")

class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.subjectMarks = marks
    
    def details(self):
        print(f"\nName of Student{self.name:>25}")
        print(f"Roll Number {self.roll:>25}")
        print("Subject-wise Marks:")

        for subject, mark in self.subjectMarks.items():
            print(f"  {subject:<20}   {mark:>10} ")
        
    
marks = {"Math": 85, "Science": 78, "English": 92, "History": 74, "Computer": 88}
s1 = Student("yadnyesh",101,marks) 
t1 = Teacher()
# s1.details()
Teacher.dipalayName()
t1.calPercentage(s1)