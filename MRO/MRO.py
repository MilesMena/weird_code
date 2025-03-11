class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")

        

r = B()
r.rk()




# Answer Below
























# In the above example the methods that are invoked is from class B but not from class A, and this is due to Method Resolution Order(MRO). 
# The order that follows in the above code is- class B – > class A .

# In multiple inheritances, the methods are executed based on the order specified while inheriting the classes. For the languages that support single inheritance, method resolution order is not interesting, but the languages that support multiple inheritance method resolution order plays a very crucial role. Let’s look over another example to deeply understand the method resolution order