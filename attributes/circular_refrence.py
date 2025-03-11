class A:
    def __init__(self):
        self.count = 0

    def add_b(self, b):
        self.b = b

    def mut_b(self):
        self.count += 1
        print(self.count)
        self.b.mut_a()
class B:
    def __init__(self):
        self.count = 0

    def add_a(self, a):
        self.a = a

    def mut_a(self):
        self.count += 1
        self.a.mut_b()


a = A()
b = B()
a.add_b(b)
b.add_a(a)

a.mut_b()
print(a.b.a is a)