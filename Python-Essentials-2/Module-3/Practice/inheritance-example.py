class Super:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "My Name is : " + self.name + "."

class Sub(Super):
    # def __init__(self, name):
    #     Super.__init__(self, name)

    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return "I am " + self.name + "."

object = Sub("Yatee")
print(object)