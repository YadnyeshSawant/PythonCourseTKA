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