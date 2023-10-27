#class and object (object oriented programming) -->

'''
creating a class : class is a saperate body which consists variables and methods in it

    syntax: 
        class class_name:
            body of class
eg:
    class chaitanya:
    a="chaitanya sharma"

'''

'''
The __init__() Function : this function is inbuilt function of python which helps the class to creating the object of class | it's defined in the class body | all classes consists this function | this function is called when class is initialized
use: Use the __init__(self,args) function to assign values to object properties, or other operations that are necessary to do when the object is being created:
this is the constructor of class in python

syntax:
class class_name:
    def__init__(arguments)


self keyword is used in __init__() function to represent the instance of class to the function  
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

eg:
    class Person:
  def __init__(self, name, age):
    self.name = name(or any value)
    self.age = age(or any value)

p1 [object] = Person("John", 36) .at this point __init__() function is called

print(p1.name)
print(p1.age)

Note: The __init__() function is called automatically every time the class is being used to create a new object.

eg2:
    class college:
    def __init__(self,name,place):
        self.name=name
        self.place=place

c1 = college("jecrc","sitapura")
print(c1.name)
print(c1.place)

'''
'''
__str__() function : it returns the string value which is given in class object variables without calling the variable name 
if not using this function we have to call the variables using object of class

If the __str__() function is not set, the string representation of the object is returned:
eg:
    calling string values without defining string function in class

        class college:
   def __init__(self,name,age):
        self.name=name
        self.age=age

c1 = college("chaitanya",22)

print(c1)


eg:
    calling string values with defining string function in class

    class school:
    def __init__(self,name,add):
        self.name=name
        self.add=add
        
    def __str__(self):
        return f"{self.name}'is my shcool and my college is '{self.add}"
y=school("kv6","sitapura") 
print(y)       

eg2:

class school:
    def __init__(self,name,add):
        self.name=name
        self.add=add

    def __str__(self):
        return f"{self.name}{self.add}"
y=school(2,3) 
print(y)       

'''

'''
Object methods: Objects can also contain methods. Methods in objects are functions that belong to the object.

eg1:

class operator:
    def __init__(self,fname,sname):
        self.fname=fname
        self.sname=sname
    def prt_fun(self):
        print("my fname is :" ,self.fname,"and my sname is :" , self.sname) 
        
io=operator("chaitanya","sharma")
io.prt_fun()

eg2:

class ui:
    def __init__(self,k,r):
        self.k=k
        self.r=r
    
    def myfun(self):
        print('k:',self.k,'r:',self.r)

h=ui(5,"aoinaognag")
h.myfun()         

'''

'''
modifying object properties

eg:
    class kl:
        l=34
        c="chaitanya"

        def prt(l,c):
            print(l,c)    
    oo=kl
    ff=oo.c="devesh"
    oo.prt(33,ff) 

'''

'''
delete object properties and object:
    
    del is a inbuilt keyword in python which allows to delete a object or property in python
    syntax:
    del object or object_property
     
eg: deleting object property

class kl:
    age=34
    
lc=kl
del lc.age #deleting object_property
print(lc.age)

eg: deleting object 


class kl:
    age=34
    print(f"my age is :{age}")
lc=kl
del lc #deleting object !
print(lc.age)
print(lc)

'''

'''
pass statement

class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
'''

class Person:
