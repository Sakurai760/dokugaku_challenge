#1
# class Apple:
#     def __init__ (self,w,c,t,p):
#         self.weight = w
#         self.color = c
#         self.taste = t
#         self.place = p
#         print("Created!")

# apple =Apple(100,"red","甘い","日本")

#2
# import math 
# class Circle:
#     def __init__ (self,r):
#         self.radius = r

    
#     def area(self):
#         return math.pi*(self.radius**2)
    
# circle = Circle (3)
# print (circle.area())

#3
# class Triangle:
#     def __init__ (self,b,h):
#         self.base =b
#         self.height =h

#     def area(self):
#         return (self.base*self.height)/2
    
# triangle = Triangle(3,4)
# print (triangle.area())

#4
class Haxagon:
    def __init__ (self,a,b,c,d,e,f):
        self.sidea= a
        self.sideb =b
        self.sidec =c
        self.sided =d
        self.sidee =e
        self.sidef =f
    def calculate_perimater(self):
        return self.sidea+self.sideb+self.sidec+self.sided+self.sidee+self.sidef

haxagon = Haxagon(1,1,1,1,1,1)
print(haxagon.calculate_perimater())




    
