class CoffeeCup:
    
    def __init__(self, temperature):
        self.temperature = temperature

    def drink_coffee(self):
        if self.temperature > 90:
            #print("Coffee is too hot.")
            raise Exception("Coffee is too hot.")
        elif self.temperature < 60:
            #print("Coffee is too cold.")
            raise ValueError("Coffee is too cold.")
        else:
            print("Drink the Coffee, it's ok.")

cup=CoffeeCup(75)
cup.drink_coffee()
