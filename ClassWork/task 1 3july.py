class A:
    name ="Yadnyesh"
    
    @classmethod
    def method1(cls):
        print(cls.name)
    
    @staticmethod
    def method2(msg):
        print(msg)
    
class B(A):
    
    @classmethod
    def method1(cls):
        cls.name = "Ujwal"
        print(f"This is from child class {cls.name}")
    
    @staticmethod
    def method2(msg):
        print(f"This is from child class {msg}")

p1 = A()
p1.method1()
p1.method2("Hello from yadnyesh")

c1 = B()
c1.method1()
c1.method2("Hello from ujwal")