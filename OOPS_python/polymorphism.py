#polymorphism: The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
'''
eg: same function len can get len of list,tuple,string etc

k=[1,2,3,4]
print(len(k))

k={1,45,"rt","chaitanya"}
print(len(k))

k="chaitanya sharma"
print(len(k))

#class polymorphism:

class a:
    def moving():
        print("a object is moving")
class b:
    def moving():
        print("a turtle is moving")
class c:
    def moving():
        print("something is moving")
        
g=a
g.moving()

g=b
g.moving()

g=c
g.moving()

'''
