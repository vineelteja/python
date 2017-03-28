# **********----  Class Definition Syntax
# A class is like a function but at completely very high level  functionality
# Classes are used to code for properties and functionalities for an object.
# Class itself will not do any work, we will create objects with all the defined properties and functionalities
# so the object will do the work for us.
# Objects are like containers which holds namespaces which are defined in the class. Objects are defined outside the
# scope of class.
# Imagine Objects as container which holds properties and functionalities from the class with which they do the job.
# You can define the class as the Blueprint from which individual objects are created.


# **********---- Class
# class definition will start with the keyword class and followed by the classname with colon ':'

# example
class className:
    """documentation for the class"""
    b = "variable"

    def method(self):
        pass

    pass




# Classes have to initiated after the definition, and they have own namespace


# **********----  Class Objects
# Class objects support two kinds of operations: attribute references and instantiation.
# To make use of properties and methods in the class we have to instantiate the class, that is done in the following way
variable = className()              # className() creates new empty object and assigns this object to variable
#  variable is called object, it has everything which is defined in class
# The process of creating object is called instantiation
# to access the variables defined in class this is the procedure (object.variable)
variable.b = "new value"
# to access the methods in class (object.method)
variable.method()
#  __doc__ is also a valid attribute, returning the docstring belonging to the class.
x = variable.__doc__            # store the docstring in x and print it
print(x)

# To create an instance with values init at time of create we have to include __init__() method in class, example
class className:
    """documentation for the class"""
    b = "variable"

    def __init__(self):
        pass

    pass

# __init__(args) method in class can have arguments, when the arguments are given at time of instantiation they
# are passed on to __init__ example,
class className:
    """documentation for the class"""
    b = "variable"

    def __init__(self, name, age):
        self.myname = name
        self.myage = age

    pass

variable2 = className("test", 25)          # given at time of instantiation they are passed on to __init__()


# **********---- Instance Objects
# you can create and use the instance variable even if the variable is not declared prior to it.


# **********---- Method Objects
# when an instance attribute is referenced that isn’t a data attribute, its class is searched.
# If a valid class attribute which is a function object when found a method object
# A new method object is created containing the  reference of  instance object to the function object just
# found together in an abstract object
# When the method object is called with an argument list, a new argument list is constructed from the instance object
# and the argument list, and the function object is called with this new argument list


# **********---- Class and Instance Variables
# Instance variables are those unique to them self
# Class variables are those shared among all instance, class variables is to have a common value to all the instances
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print("d.kind is: ", d.kind)
print("e.kind is: ", e.kind)
print("d.name is: ", d.name)
print("e.name is: ", e.name)


# Shared data can have possibly surprising effects with involving mutable objects such as lists and dictionaries
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print("d.tricks is: ", d.tricks)
print("e.tricks is: ", e.tricks)
# We might want to have unique tricks to each dog, in that case you should create the list inside __init__()
# not as as an class variable

# **********---- Random Remarks to remember
# Data attributes override method attributes with the same name, to avoid this Possible conventions include
# capitalizing method names, prefixing data attribute names with a small unique string (perhaps just an underscore)

# Nothing in Python makes it possible to enforce data hiding — it is all based upon convention.
# (On the other hand, the Python implementation, written in C, can completely hide implementation details and
# control access to an object if necessary; this can be used by extensions to Python written in C.)


# Any function object that is a class attribute defines a method for instances of that class. It is not necessary that
# the function definition is textually enclosed in the class definition: assigning a function object
# to a local variable in the class is also ok. For example:
# Function defined outside the class

def functionOne(self, x, y):
    return min(x, x+y)

class ClassNew:
    function = functionOne

    def functionTwo(self):
        return 'hello world'

    ref = functionTwo
# Now functionOne, functionTwo and ref are all attributes of class ClassNew that refer to function objects,
# and consequently they are all methods of instances of ClassNew ref being exactly equivalent to funtionTwo,
# This will only create confusion, try to avoid this style of practice

# Methods may call other methods by using method attributes of the self argument:
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)             # calling data attribute data

    def addtwice(self, x):
        self.add(x)                     # calling method add from within
        self.add(x)
    pass

# **********----  Inheritance
# Inheritance is a way to use properties and functions of other classes as your own, you can either extend
# the functionality or you can override the existing one
# the class you are inheriting is called the base class, and the calling which is inheriting is derived/sub/child class
# Syntax for inheritance is include the base class name in parenthesis'()' after the class name example
# class ClassName(Dog):             # Dog is the base class, ClassName is child class.
# Both the Base class and derived class are expected to be defined in same scope. if they are in different module
# then you have to do this
# class DerivedClassName(moduleName.BaseClassName):

# when the class object is constructed, the base class is remembered.
# This is used for resolving attribute references: if a requested attribute is not found in the class,
# the search proceeds to look in the base class.
# This rule is applied recursively if the base class itself is derived from some other class,
# the same follows for methods too

# Python has two built-in functions that work with inheritance:
    # Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or
    # some class derived from int.
    # Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int.
    # However, issubclass(float, int) is False since float is not a subclass of int.


# **********---- Multiple Inheritance
# In python you can inherit from multiple classes that mean you can have multiple base classes seperated with comma ','
# class DerivedClassName(Base1, Base2, Base3):
# when an attribute is searched and failed to find in DerivedClassName, as we know python searches for it in the
# base class, it starts the search from the left most inherited class & search in every class to the right till the end


# method resolution order >>>>

# **********---- Private Variables >>>>
# “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python, However
# a name prefixed with an underscore should be treated as a non-public part of the API example: _variable


# **********---- Odds and Ends >>>>



# **********---- Iterators
# we have used for loops many times, have you ever wondered how it is working
# Behind the scenes, the for statement calls iter() on the container object.
# It is like type casting the container object,
# for example you are changing the list object to iterator object, and then use next() to call the first element
# every time you call the next function it will produce the next value, Once there is nothing to print, then
# when you call the next function, it raises an exception 'stop iteration' to stop.
s = 'abc'
print("type of s: ",type(s))                # s is str at this point
it = iter(s)                                # s is converted to str_iterator
print("type of it: ",type(it))              # now check it
print(it)
print(next(it))                             # printing each values
print(next(it))
print(next(it))
print(next(it))                             # raises an exception when it reaches the end


# Having seen the mechanics behind the iterator protocol, it is easy to add iterator behavior to your classes.
# Define an __iter__() method which returns an object with a __next__() method. If the class defines __next__(),
# then __iter__() can just return self:

class something:
    def __init__(self):
        self.count = ["car", "bike", 3, "love"]         # creating a list
        self.index = -1                                 # setting index to -1

    def __iter__(self):
        return self                                     # Returning the same object

    def __next__(self):                                 # always iter is followed by next, next alone cannot iterate
        self.index += 1                                 # increase the index by 1 everytime it is executed
        if(self.index == len(self.count) ):             # check if index is equal to length
            raise StopIteration                         # if equal to len, stop iteration
        return self.count[self.index]                   # return the value from list

s = something()
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())


# **********---- Generators
# Generators are a simple and powerful tool for creating iterators.
# Generators are written like regular functions but use the yield statement whenever they want to return data.
#  Each time next() is called on it, the generator resumes where it left off
# (it remembers all the data values and which statement was last executed).



# **********----  Scopes and Namespaces

# Scope is the area in which a variable is available to use.
# Two types of scope: Global and Local
# Local Variable when initiated, is available to use only in the particular block of code.
# if a variable is initiated in a function, that variable is not available outside the function
# if the variable is initiated in the beginning of the file before all functions and classes then it is said to be
# Global variable, and that variable is available from the program beginning till the program end.
# There are at least three nested scopes whose namespaces are directly accessible
    # The innermost scope, which is searched first, contains the local names
    # The scopes of any enclosing functions, which are searched starting with the nearest enclosing scope,
    # contains non-local, but also non-global names
    # The next-to-last scope contains the current module’s global names
    # The outermost scope (searched last) is the namespace containing built-in names


# Namespace is a place where names(variables, function names) are mapped to
# the respective objects(values).
# Namespaces are currently implemented with python dictionaries.
# if you define a = 10, b = "string". python stores it as {'a':10, 'b:"string"}
# Each module has there own namespace, Namespaces have absolutely no relation between names in different namespaces
# Imagine as what ever the object holds inside of it are the attributes of the object, attributes are accessed
# with the '.' dot. example: object.variable, object.functionName etc
# If you are referring to names in other modules, they are always attribute reference.
# use the module name to refer them example: module.functionName, module.variable
# As you everything is stored in namespace in form of dictionaries. we can use del() to delete the name completely.
# Namespaces are created at various points at time of execution.
# Pythons built in names are always created when the python interpreter get in action, and the names are never deleted
# Just like humans python also reads the code starting from line 1 and goes till the end
# when the Module is read by the interpreter the global namespace is created and will last till the interpreter quits
# The first file which interacts with the interpreter are considered part of a module called __main__,
# They have there own namespace
# Namespaces for functions are created when the function is called, and deleted when the execution of function is complete
# Recursives like loops have there own local namespace
# Example for Scopes and Namespaces


