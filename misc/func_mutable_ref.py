 
def g(x):
    def f(num=None, lst=[]):
        if num is not None: lst.append(num)
        return lst
    print(f.__defaults__)
    for xx in x:
        c = f(xx)
    return c, f
 
if __name__ == '__main__':
    lst1, f1 = g([1, 2, 3])
    print(f1.__defaults__)
    print(lst1)
    lst2, f2 = g([3, 4, 5])
    print(lst2)
    print(lst1)
    
    lst1 = f2(num=10, lst=lst1)
    print(lst1)
    print(f1())
    print(f1.__name__)       # Function name
    print(f1.__doc__)        # Docstring
    print(f1.__defaults__)   # Default values of arguments
    print(f1.__code__.co_varnames)  # Variable names (local + args)
    print(f1.__code__.co_argcount)  # Number of arguments
    print(f1.__annotations__)       # Type annotations (if any)
    num, lst_inception = f1.__defaults__
    lst_inception.append(20)
    print(lst_inception)
    print(lst1)
    f1.__defaults__[1].clear()
    print(f1.__defaults__)
    print(lst1)
 