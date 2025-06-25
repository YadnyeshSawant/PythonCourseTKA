# Student has features like name, roll and subjects with marks. There are 5 subjects for every students with some marks.
# Student has one operation which will display percentage of student.
# use dictionary


class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.subjectMarks = marks

    def display(self):

        self.marksObatined = 0
        for v in self.subjectMarks.values():
            self.marksObatined += v

        self.numberOfSubject = len(self.subjectMarks) * 100
        self.percentage = (self.marksObatined / self.numberOfSubject) * 100

        print(f"\nName of Student{self.name:>28}")
        print("Subject-wise Marks:")

        for subject, mark in self.subjectMarks.items():
            print(f"  {subject:<25}   {mark:>10} ")

        print(f"Total Marks Obtained by{self.marksObatined:>18}")
        print(f"Percentage Obatained{self.percentage:>23.2f}")
        print()
        print("=" * 42)


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

#############################################################
# OUTPUT

# Name of Student                    Yadnyesh
# Subject-wise Marks:
#   Math                                85
#   Science                             78
#   English                             92
#   History                             74
#   Computer                            88
# Total Marks Obtained by               417
# Percentage Obatained                  83.40

# ==========================================

# Name of Student                       Ujwal
# Subject-wise Marks:
#   Math                                67
#   Science                             56
#   English                             34
#   History                             68
#   Computer                            90
# Total Marks Obtained by               315
# Percentage Obatained                  63.00

# ==========================================

# Name of Student                      Shruti
# Subject-wise Marks:
#   Math                                76
#   Science                             39
#   English                             34
#   History                             67
#   Computer                            89
# Total Marks Obtained by               305
# Percentage Obatained                  61.00

# ==========================================

# Name of Student                       Shree
# Subject-wise Marks:
#   Math                                68
#   Science                             23
#   English                             43
#   History                             45
#   Computer                            97
# Total Marks Obtained by               276
# Percentage Obatained                  55.20

# ==========================================
