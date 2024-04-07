# Create a class named Fib
class Fib:

    # Prepare a class constructor
    def __init__(self, nn):
        
        # Print this message to observe the class behaviour
        print("__init__")

        # Create a private variable (__n) to store the series limit
        self.__n = nn

        # Create a private variable (__i) to track the current fiboonacci number to provide
        self.__i = 0

        # To save the 2 previous numbers, declare two private variables (__p1, __p2)
        self.__p1 = self.__p2 = 1

    # This method is obliged to return the iterator object itself.
    def __iter__(self):
        print("__iter__")
        return self

    # The __next__() method is responsible for creating the sequence
    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for  i in Fib(10):
    print(i)
    