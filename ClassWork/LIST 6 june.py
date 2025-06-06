# a =10
# print(id(a),a)

# a =20
# print(id(a), a)

# a=30
# print(id(a), a)

# l =[]
# print(id(l))
# l.append(10)
# print(id(l))
# l.append("Hello")
# print(id(l))
# l.append(-20.5)
# print(id(l))
# l.append(True)
# print(id(l))
# l.append("Hello")
# print(id(l))

# print(l[1:4])
# print(l[4])
# print(l[-1])
# print(l[-4])

# for i in l:
#     print(i)
    
# for i in range(len(l)):
#     if i %2 ==0:
#         print(i, "--->", l[i])
        
        
name =["viru","ujwal","gabbar","niraj"]
# print(name[len(name)-1])
# for i in name:
#     if(i=="gabbar"):
#         for j in i:
#             if(j =="r"):
#                 print(j)
# a =name[0]
# print(a[::-1])

count =0
for i in range(len(name)):
    if(len(name[i]) > 4):
        count +=1
        print(i,name[i])
