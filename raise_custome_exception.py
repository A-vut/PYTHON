class CoffeeTooHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeeTooColdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CoffeeCup:
    
    def __init__(self, temperature):
        self.temperature = temperature

    def drink_coffee(self):
        if self.temperature > 90:
            #print("Coffee is too hot.")
            raise CoffeeTooHotException("Coffee Temperature: " + str(self.temperature))
        elif self.temperature < 60:
            #print("Coffee is too cold.")
            raise CoffeeTooColdException("Coffee Temperature: " + str(self.temperature))
        else:
            print("Drink the Coffee, it's ok.")

cup=CoffeeCup(85)
cup.drink_coffee()
