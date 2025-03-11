
class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")

class C(A):
    def rk(self):
        print("In class C")

# classes ordering
class D(B, C):
    pass

r = D()
r.rk()



# Answer Below
















#Diamond inheritance
# Python follows a depth-first lookup order and hence ends up calling the method from class A. By following the method resolution order, the lookup order as follows. 
# Class D -> Class B -> Class C -> Class A 
# Python follows depth-first order to resolve the methods and attributes. So in the above example, it executes the method in class B. 