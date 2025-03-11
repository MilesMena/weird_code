class Base:
    atter = "this is BASE"
    def __init__(self, name):
        self.set_name(name)

    def set_name(self, name):
        self.name = name + "_miles"
    
    
class SubClass(Base):
    atter = "OVERIDE BASE"
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

if __name__ == "__main__":
    b = Base("1")
    sc = SubClass("2", "2")
    print(b.atter)
    print(vars(b))
    print(sc.atter)
    print(vars(sc))