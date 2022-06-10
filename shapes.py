# Classes and Mathematical operators 

       #Question1

from math import pi

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        x= pi*self.radius**2
        return x

    def circumference(self):
        y = 2 * pi*self.radius
        return y

c1 = Circle(radius=21)
print(c1.radius)
print(c1.area())
print(c1.circumference())        


     #Question2
class Square:

    def __init__(self,s):
        self.s = s

    def area(self):
        a = self.s^2
        return a


    def perimeter(self):
       return(self.s *4)

s1 = Square(s = 6)
print(s1.s)
print(s1.area())
print(s1.perimeter())


#   #Question3
class Rectangle:

    def __init__(self,length,width):
          self.length = length
          self.width = width

    def area(self):
        a = self.length * self.width
        return a

        
    def perimeter(self):
        b = 2*(self.length,self.width)
        return b

s = Rectangle(length=12,width=10)
print(s.area())
print(s.perimeter())


#   #Question 4
class Sphere:
     def __init__(self,radius):
        self.radius = radius

     def area(self):
        x= 4*pi*self.radius**2
        return x

     def volume(self):
        y = 3/4 * pi*self.radius**3
        return y

a1 = Sphere(radius = 30)
print(a1.radius)
print(a1.area())
print(a1.volume())   





   



    



           







