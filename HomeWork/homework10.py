# Method Decorators


def displayResult(fun):
    def innerMethod(self):
        print("Used Decorator")
        print("Subject-wise Marks:")
        for subject, mark in self.subjectMarks.items():
            print(f"  {subject:<20}   {mark:>10} ")
        fun(self)

    return innerMethod


class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.subjectMarks = marks

    @displayResult
    def details(self):
        print(f"\nName of Student{self.name:>25}")
        print(f"Roll Number {self.roll:>25}")
        obatinedMarks = 0
        for v in self.subjectMarks.values():
            obatinedMarks += v
        totalMarks = len(self.subjectMarks) * 100
        percentage = (obatinedMarks / totalMarks) * 100
        print(f"percentage = {percentage:>20.2f} %")


marks = {"Math": 85, "Science": 78, "English": 92, "History": 74, "Computer": 88}
s1 = Student("yadnyesh", 101, marks)
s1.details()
