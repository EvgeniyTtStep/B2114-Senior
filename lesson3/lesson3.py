class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"No passengers found in {self.brand}")




misha = Human("Misha")
maxim = Human("Maxim")
jack = Human("Jack")


car = Auto("Dodge challenger")
car.add_passenger(misha, maxim, jack)
# car.add_passenger(misha)
# car.add_passenger(maxim)
# car.add_passenger(jack)
car.print_passengers_names()










