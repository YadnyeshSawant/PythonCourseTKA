# trial for pop and remove methods for the index and value attributes.

l = [1,2,3,4,5,6,7,8,9,10,"yadnyesh","sawant","tka"]

print("original List ->",l)
print("Input as index for pop function ")
l.pop(9)
print(l)

#################################
# OUTPUT
# original List -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'yadnyesh', 'sawant', 'tka']
# Input as index for pop function 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 'yadnyesh', 'sawant', 'tka']
################################

print("Input as value for remove function") 
l.remove("yadnyesh")
print(l)

#################################
# OUTPUT
# Input as value for remove function
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 'sawant', 'tka']
################################

print("Input as value for pop method")
l.pop("yadnyesh")
print(l)

#################################
# OUTPUT
# Input as value for pop method
# Traceback (most recent call last):
#   File "d:\python csr\PythonCourseTKA\HomeWork\homework4.py", line 28, in <module>
#     l.pop("yadnyesh")
# TypeError: 'str' object cannot be interpreted as an integer
################################

print("Input as index for remove method")
l.remove(0)
print(l)

#################################
# OUTPUT
# Input as index for remove method
# Traceback (most recent call last):
#   File "d:\python csr\PythonCourseTKA\HomeWork\homework4.py", line 41, in <module>
#     l.remove(0)
# ValueError: list.remove(x): x not in list
################################