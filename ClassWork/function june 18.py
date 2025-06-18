# def maxNum(a,b):
#     if a>b:
#         return [a,b,70,"if"]
#     else:
#         return b,a,70,"else"
# max = maxNum(20,10)
# print(type(max))

# a,b,c,d = max
# print(a,b,c,d)

# print(type(a),type(b),type(c),type(d))

# a =10
# b=20
# c=30
# d=40
# bag = a,b,c,d
# print(type(bag))

#positional arb arg

# def Addition(*args):
#     print(type(args))
#     print(args)
#     res = sum(args)
#     print(res)
    
# Addition(20,30,40,50,60)

#Keyword Arb Args
def submit(**kwargs):
    print(type(kwargs))
    print(kwargs)
submit(name="yadnyesh",no =909090909,email="yadnyesh@gmailcom")