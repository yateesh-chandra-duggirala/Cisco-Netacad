class InvalidDimension(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class Rectangle :
    def __init__(self, length = 0, breadth = 0):
        self.__length = length
        self.__breadth = breadth

    def area(self) :
        if self.__length <= 0 or self.__breadth <= 0:
            raise InvalidDimension("Invalid Dimension of the rectangle")
        return f"The Area of the Rectangle : {self.__length * self.__breadth}"
        
    
    def perimeter(self) :
        if self.__length <= 0 or self.__breadth <= 0:
            raise InvalidDimension("Invalid Dimensions of the rectangle")
        return f"The Perimeter of the Rectangle : {2 * (self.__length + self.__breadth)}"

rectangle_2 = Rectangle(5, 4)
print(rectangle_2.perimeter())

rectangle_1 = Rectangle(5)
print(rectangle_1.area())