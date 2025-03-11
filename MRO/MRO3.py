class A: 
    pass


class B: 
    pass


class C(A, B): 
    pass


class D(B, A): 
    pass


class E(C,D): 
    pass






# Answer Below













# DLR Algorithm

# In the above Example algorithm first looks into the instance class for the invoked method. If not present, then it looks into the first parent, if that too is not present then-parent of the parent is looked into. This continues till the end of the depth of class and finally, till the end of inherited classes. So, the resolution order in our last example will be D, B, A, C, A. But, A cannot be twice present thus, the order will be D, B, A, C. But this algorithm varying in different ways and showing different behaviours at different times .So Samuele Pedroni first discovered an inconsistency and introduce C3 Linearization algorithm. 

# C3 Linearization Algorithm : 
# C3 Linearization algorithm is an algorithm that uses new-style classes. It is used to remove an inconsistency created by DLR Algorithm. It has certain limitation they are: 

# Children precede their parents
# If a class inherits from multiple classes, they are kept in the order specified in the tuple of the base class.
# C3 Linearization Algorithm works on three rules: 

# Inheritance graph determines the structure of method resolution order.
# User have to visit the super class only after the method of the local classes are visited.
# Monotonicity