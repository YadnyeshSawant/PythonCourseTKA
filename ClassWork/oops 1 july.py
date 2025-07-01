# class Book:
#     def __init__(self, name, p):
#         self.bname = name
#         self.price = p
#     def __add__(self,**kwargs):
#         return self.price * other.price


# b1 = Book("core py", 200)
# b2 = Book("adv py", 400)
# b3 = Book("core java", 400)


class P:

        def property(self):
            l = ["gold","land","house","car"]
            print(l)
        def marry(self):
            print("GIRL A")


class C1(P):
    
        def property1(self):
            l = ["car","gold"]
            print(l)
            
        def marry(self):
            super().marry()
            # print("GIRL B")

ch1 = C1()
ch1.property()
ch1.property1()
ch1.marry()