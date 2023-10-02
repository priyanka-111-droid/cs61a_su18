'''
SUPER KEYWORD:
It allows you to call methods of the superclass in your subclass. 
The primary use case of this is to extend the functionality of the inherited method.
'''


# Single inheritance 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length) # super(Square, self).__init__(length, length) used in Python2,avoid now.


#Multilevel inheritance
class Cube(Square):
    def surface_area(self):
        face_area = super().area() #super not used used with init
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

        
         
sq = Square(4)
print(sq.area())


