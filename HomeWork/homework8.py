# Student has features like name, roll and subjects with marks. There are 5 subjects for every students with some marks.
# Student has one operation which will display percentage of student.
# use dictionary


class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.subjectMarks = marks
        self.marksObatined = sum(self.subjectMarks.values())
        self.numberOfSubject = len(self.subjectMarks) * 100
        self.percentage = (self.marksObatined / self.numberOfSubject) * 100

    def display(self):
        print(f"Name of Student              {self.name}")
        print("Subject-wise Marks:")

        for subject, mark in self.subjectMarks.items():
            print(f"  {subject:<25}  {mark}")
        print(f"Total Marks Obtained by      {self.marksObatined}")
        print(f"Percentage Obatained         {self.percentage:.2f}%")
        print("---" * 20)

students = []

stud1 = {"Math": 85, "Science": 78, "English": 92, "History": 74, "Computer": 88}
students.append(Student("Yadnyesh", 101, stud1))

stud2 = {"Math": 67, "Science": 56, "English": 34, "History": 68, "Computer": 90}
students.append(Student("Ujwal", 101, stud2))

stud3 = {"Math": 76, "Science": 39, "English": 34, "History": 67, "Computer": 89}
students.append(Student("Shruti", 101, stud3))

stud4 = {"Math": 68, "Science": 23, "English": 43, "History": 45, "Computer": 97}
students.append(Student("Shree", 101, stud4))

for s in students:
    s.display()
