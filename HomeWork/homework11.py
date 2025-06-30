# Hybrid Inheritance
class A:
    def m1(self):
        print("Method of CLASS A M1")


class B(A):
    def m2(self):
        print("Method of CLASS B M2")


class C(A):
    def m3(self):
        print("Method of CLASS C M3")


class D:
    def m4(self):
        print("Method of CLASS D M4")


class E(B):
    def m5(self):
        print("Method of CLASS E M5")


class F(C, D):
    def m6(self):
        print("Method of CLASS F M6")


jay = E()
viru = F()

print("methods and class accesible from object jay")
jay.m1()
jay.m2()
jay.m5()

print("methods and class accesible from object viru")
viru.m1()
viru.m3()
viru.m4()
viru.m6()


###############################################################
# OUTPUT:-
# methods and class accesible from object jay
# Method of CLASS A M1
# Method of CLASS B M2
# Method of CLASS E M5

# methods and class accesible from object viru
# Method of CLASS A M1
# Method of CLASS C M3
# Method of CLASS D M4
# Method of CLASS F M6
