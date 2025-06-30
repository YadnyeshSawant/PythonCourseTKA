# INHERITANCE IN PYTHON

# Single level
# class Parent:

#     def property(self):
#         l = ["gold","land","house","car"]
#         print(l)

# class Child(Parent):

#     def m1(self):
#         print("Im Child Class")

# ch1 = Child()
# ch1.m1()
# ch1.property()


# Multilevel
# class GrandParent:

#     def grandMethod(self):
#         print("Im am class grand parent")

#     def property(self):
#         l = ["gold","land","house","car"]
#         print(l)

# class Parent(GrandParent):

#     def parentMethod(self):
#         print("Im parent Class")

# class Child(Parent):

#     def childMethod(self):
#         print("Im Child Class")

# ch1 = Child()
# ch1.grandMethod()
# ch1.parentMethod()
# ch1.childMethod()
# ch1.property()

# p1 = Parent()
# p1.property()

# Multiple Inheritance

# class GrandParent:

#     def grandMethod(self):
#         print("Im am class grand parent")

#     def property(self):
#         print("gp")

# class Mother(GrandParent):

#     def mother(self):
#         print("Im am class grand parent")

# class Father:

#     def father(self):
#         print("Im parent Class")

#     def property(self):
#         print("father")

# class Child(Mother,Father):

#     def childMethod(self):
#         print("Im Child Class")

# ch1 = Child()
# ch1.mother()
# ch1.father()
# ch1.property()


# Hierarchical Inheritance
class P:

    def m1(self):
        print("Im Parent")


class C1(P):

    def m2(self):
        print("Im Child C1")


class C2(P):

    def m3(self):
        print("Im Child C2")


class C3(P):

    def m3(self):
        print("Im Child C3")


c1 = C1()
c2 = C2()
c3 = C3()

c1.m1()
c2.m1()
c3.m1()
 