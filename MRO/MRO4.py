# Python program to show the order
# in which methods are resolved

class A:
    def __new__(cls):
        instance = super().__new__(cls)
        print("In class A new")
        return instance
    def __init__(self):
        print("In class A init")
    def rk(self):
        print("In class A")

class B:
    def rk(self):
        print("In class B")

# classes ordering
class C(A, B):
    print("Top level")
    # def __init__(self):
    #     print("hello")
    #     # super().__init__()
    #     print("Constructor C")

r = C()
r.rk()
# it prints the lookup order 
print(C.__mro__)
print(C.mro())