# There are 10 students in a class. with roll numbers 1 to 10
# Atul sir conducted on python session on that class and attendance is as follows
# t = (5,2,9,5,5,1,8,2)
# Few students marked their attendance twice or many times.
# 1. Find total number of students attended that session
# 2. Display roll number of present students

t = (5, 2, 9, 5, 5, 1, 8, 2)
absent = []
s = set(t)
print("Present Students ", s)
print("Total students present ", len(s))

for data in range(1, 11):
    if data not in s:
        absent.append(data)
print("Absent Students", absent)
