class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self,pizza , message)
        self.cheese = cheese

def make_pizza(pizza, cheese) :
    if pizza not in ['margherita', 'capriccoisa', 'calzone']:
        raise PizzaError(pizza, "no such Pizza in the Menu")
    if cheese > 100 :
        raise TooMuchCheeseError(pizza, cheese, "too much Cheese")
    print("Pizza Ready")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce :
        print(tmce, ":", tmce.cheese)
    except PizzaError as pe:
        print(pe, ":", pe.pizza)