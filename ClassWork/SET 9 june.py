# s = set()
# s.add(10)
# s.add(20)
# s.add(30)
# s.add("Yadnyesh")
# s.add("Sawant")
# s.add("Sawant")
# print(s)

# t = (1,2,3)
# s.add(t)
# print(s)

l1 = [10,20,30,40]
l2 = ["jay", "viru", "Gabbar"]
t = (1,2,3)
s = {1,2,3,4,5,6}
s2 = {4,5,6,7}
s3 = s.intersection(s2)
print(s3)
fs = frozenset(s)
print(fs)
fs.add(78)
print(fs)
# print(len(t))
# print(t[3][1])
# print(t[4][2])
# for data in t[5]:
#     if data == 9:
#         print(data)
        
# l1.insert(2,l2)
# print(l1[2][1][2])
# l1.insert(1, t)
# l1.insert(1, s)
# print(l1)
# print(l1[1][0])

# for data in l1[1]:
#     print(data)

# print(len(l1))
# l1l2 = []
# l1l2.append(l1)
# l1l2.append(l2)
# print(l1l2)
# l1l2.append(t)
# print(l1l2)
# l1l2.append(s)
# print(l1l2)
