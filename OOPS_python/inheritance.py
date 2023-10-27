#---------------------inheritance--------------------------#

#inheritance : inheritance is the part of OOPS in python using we can use the properties of parent class into derived class
#parent class : from where all the properties are derived 
#child class : to where all properties are going to be used !

#types of inheritance:{ single , multiple , multilevel , hirarchical , hybrid } inheritance
#super.__init__(args) : this helps to inherit all the methods and variables of parent class in derived class without using the name of it's parent class
 
 
'''
single : one base class & one derived class

eg:

class l1:
    j=23
    def kl():
        print("iam right")

class l2(l1):
    print("done")
    
o=l2
o.kl()
o
print(o.j+2)

'''

'''
Multiple : multiple base clasess and single derived class


class A:
    e=10

class B:
    r=20    

class C:
    t=30

class derived(A,B,C):
    pass

s = derived
print(s.e+s.r+s.t)

'''

'''
Multilevel - inheritance : derivation occures in a series of class level-wise
eg:

class a:
    j=10

class b(a):
    pass

class c(b):
    pass
kl=c
print(kl.j)

'''

'''
heirarchical : single base class and multiple derived class like a family tree/heirarchy tree

eg:

class a:
    g=10

class b(a):
    pass

class c(a):
    pass

class d(a):
    pass

class h(a):
    pass

ov=b

print(ov.g)

ov=c

print(ov.g)

ov=d

print(ov.g)

ov=h

print(ov.g)

'''

'''
hibrid inheritance: mix of multiple types of inheritance

eg:

class a:
    k=10

class b(a):
     pass #print(k) 

class c(a):
        pass #print(k+10)

class d(a):
    g=19 #print(g+k)

class t(d):
    pass #print(t)

ob=b
print(ob.k)

ob=c
print(ob.k+10)

ob=d
print(ob.k+ob.g)

ob=t
print(ob.g)

'''

#init system (inheriting init function from base class , declaring init in base class , inheriting all properties of base class using .super keyword)

#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.


class a:
    def __init__(self,fname,lname,year_of_b):
        self.fname=fname
        self.lname=lname
        self.year_of_b=year_of_b
    def fun(self):
        print(f"hello my fname is {self.fname} & my lname is : {self.lname} and my year of birth is :{self.year_of_b}")
        
class b(a):
    def __init__(self, fname, lname, year_of_b): #this is not very important !
        super().__init__(fname,lname,year_of_b) # we not need to provide self keyword in super function arguments
        self.year_of_b=year_of_b
        #a.__init__(self,fname,lname)
    def add_fun(self):
        print("current year iam living in :",self.year_of_b+22)
        
h=b("chaitanya","sharma",2001)

h.fun()
h.add_fun()