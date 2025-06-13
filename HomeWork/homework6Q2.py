# use * operator  for all other data types.
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

print("int * int",a*b)
# int * int 200

print("int * string",a*c)
# int * string SaiSaiSaiSaiSaiSaiSaiSaiSaiSai

print("int * list",a*l1)
# int * list [10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30]

print("int * tuple", a*t1)
# int * tuple (10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30)



print("int * set",a*s1)
# TypeError: unsupported operand type(s) for *: 'int' and 'set'

print("int * dict",a*d1)
# TypeError: unsupported operand type(s) for *: 'int' and 'dict'

print("string * string",c*d)
# TypeError: can't multiply sequence by non-int of type 'str'

print("string * list",c*l1)
# TypeError: can't multiply sequence by non-int of type 'list'

print("string * tuple",c*t1)
# TypeError: can't multiply sequence by non-int of type 'tuple'

print("string * set",c*s1)
# TypeError: can't multiply sequence by non-int of type 'set'

print("string * dict",c*d1)
# TypeError: can't multiply sequence by non-int of type 'dict'

print("list * list",l1*l2)
# TypeError: can't multiply sequence by non-int of type 'list'

print("list * tuple",l1*t1)
# TypeError: can't multiply sequence by non-int of type 'tuple'

print("list * set",l1*s1)
# TypeError: can't multiply sequence by non-int of type 'set'

print("list * dict",l1*d1)
# TypeError: can't multiply sequence by non-int of type 'dict'

print("tuple * tuple", t1*t2)
# TypeError: can't multiply sequence by non-int of type 'tuple'

print("tuple * dict", t1*d1)
# TypeError: can't multiply sequence by non-int of type 'dict'

print("tuple * set", t1*s1)
# TypeError: can't multiply sequence by non-int of type 'set'

print("set * set",s1*s2)
# TypeError: unsupported operand type(s) for *: 'set' and 'set'

print("set * dict",s1*d1)
# TypeError: unsupported operand type(s) for *: 'set' and 'dict'

print("dict * dict", d1*d2)
# TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
