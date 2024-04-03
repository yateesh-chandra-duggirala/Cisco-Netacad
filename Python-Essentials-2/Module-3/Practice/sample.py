# __day = 'Mon'
# n = 15
# __week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# print(__week[(__week.index(__day) + n)  % 7])
# print(__week[(__week.index(__day) - n)  % 7])

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

# sun = Star("Sun", "Milky Way")
# for i in sun.__dict__.keys():
#     print(i, '->', sun.__dict__[i])

# exception = ArithmeticError
# print(exception.__name__)
# for subclass in exception.__subclasses__():
#     print(subclass.__name__)

# q = 7
# d = 0
# try :
#     res = 1 / d
#     print(res)
# except ZeroDivisionError as e :
#     raise ZeroDivisionError("DIVI ERROR")

# class A:
#     def __init__(self,v = 1):
#         self.v = v

#     def set(self,v):
#         self.v = v
#         return v


# a = A()
# print(a.set(a.v + 1))

# class A:
#     X = 0
#     def __init__(self,v = 0):
#         self.Y = v
#         A.X += v


# a = A()
# b = A(1)
# c = A(2)
# print(c.X)


class A:
    def __init__(self):
        pass


a = A(1)
print(hasattr(a,'A'))

