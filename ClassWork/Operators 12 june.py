# # use + for all other data types expect num and string
# # use * for all other data types with string.
# ps = True
# sp = True
# sb = False
# if(ps and sp and sb):
#     print("AIRBAG DEPLOYED")
# else:
#     print("AIRBAG NOT DEPLOYED")
# # print(a>b)
# # print(a<b)
# # print(a==b)
# # print(a!=b)
# # print(a>=b)
# # print(a<=b)
# # print(a>c)
# # print(a>=c)
# # print(a<=c)
# # print(a==c)
# # print(a!=c)
# # print(a>b>c)
# # print(a<b<c)

# l = [1,2,3,4,5,6,7,8,9,10]
# print(90 in l)
# print(ps is sb)

a = 10

l = ["Sai",10,20.5]

# print(type(a),type(l))
print(a is l[1])
print(id(a) == id(l[1]))