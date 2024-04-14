class ExampleClassPri:
    def __init__(self, val = 1):
        self.__first = val
    def set_second(self, val = 2):
        self.__second = val
    
example_obj_1 = ExampleClassPri()

example_obj_2 = ExampleClassPri(2)
example_obj_2.set_second(3)

example_obj_3 = ExampleClassPri(4)
example_obj_3.__third = 5

print(example_obj_1.__dict__)
print(example_obj_2.__dict__)
print(example_obj_3.__dict__)