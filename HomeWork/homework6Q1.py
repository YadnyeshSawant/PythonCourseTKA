# use + operator  for all other data types expect int + int  and string + string
a = 10
b = 20
c = "Sai"
d = "Kumar"

l1 = [10,20,30]
l2 = [40,50,60]

t1 = (10,20,30)
t2 = (40, 50, 60)

s1 = {10, 20, 30}
s2 = {40, 50, 60}

d1 = {1:"ONE", 2:"TWO", 3:"THREE"}
d2 = {4:"FOUR", 5:"FIVE", 6:"SIX"}

print("int + int",a+b)
# int + int 30

print("string + string",c+d)
# string + string SaiKumar

print("list + list",l1+l2)
# list + list [10, 20, 30, 40, 50, 60]

print("tuple + tuple", t1+t2)
# tuple + tuple (10, 20, 30, 40, 50, 60)

print("int + string",a+c)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("int + list",a+l1)
# TypeError: unsupported operand type(s) for +: 'int' and 'list'

print("int + tuple", a+t1)
# TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

print("int + set",a+s1)
# TypeError: unsupported operand type(s) for +: 'int' and 'set'

print("int + dict",a+d1)
# TypeError: unsupported operand type(s) for +: 'int' and 'dict'

print("string + list",c+l1)
# TypeError: can only concatenate str (not "list") to str

print("string + tuple",c+t1)
# TypeError: can only concatenate str (not "tuple") to str

print("string + set",c+s1)
# TypeError: can only concatenate str (not "set") to str

print("string + dict",c+d1)
# TypeError: can only concatenate str (not "dict") to str

print("list + tuple",l1+t1)
# TypeError: can only concatenate list (not "tuple") to list

print("list + set",l1+s1)
# TypeError: can only concatenate list (not "set") to list

print("list + dict",l1+d1)
# TypeError: can only concatenate list (not "dict") to list

print("tuple + set", t1+s1)
# TypeError: can only concatenate tuple (not "set") to tuple

print("tuple + dict", t1+d1)
# TypeError: can only concatenate tuple (not "dict") to tuple

print("set + set",s1+s2)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'

print("set + dict",s1+d1)
# TypeError: unsupported operand type(s) for +: 'set' and 'dict'

print("dict + dict", d1+d2)
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'