# TUPLE DATA TYPE:  JUNE 9 
t = (1,2,3,"Yadnyesh","Sawant")

for data in t:
    print(data)
    
for i in range(len(t)):
    print(i," -- >",t[i])
print(id(t))

l = list(t)
print(l)
l.append("TKA")
print(l)

t = tuple(l)
print(t)
for i in range(len(t)):
    print(i," -- >",t[i])
print(id(t))
