# Create a Car class with attributes for make, model, and year. Include a method called start_engine() that prints a formatted string describing the car starting up.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.year = year
        self.model = model

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running!")

# crate object of the class
# my_car = Car("Toyota", "Camry", 2022)



make = input("Enter car make: ")
model = input("Enter car model: ")
year = int(input("Enter car year: "))

# create object
my_car = Car(make, model, year)

# call the method
my_car.start_engine()