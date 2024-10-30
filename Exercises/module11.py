# 1 Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor. Also write the required initializers to both classes. Create a print_information method to both subclasses for printing out all information of the publication in question. In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both publications using the methods you implemented.
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        return f"{self.name} (Author {self.author}, {self.page_count} pages)"

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        return f"{self.name} (Chief Editor {self.chief_editor})"

publication_list=[
    Book("Compartment No. 6", "Rosa Liksom", "192"),
    Magazine("Donald Duck", "Aki Hyyppä")
]
for publications in publication_list:
    print(publications.print_information())
# 2 Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses. For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter. It calls the initializer of the base class to set the first two properties and then sets its capacity. Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.

class Car:
    def __init__(self, reg_number, max_speed, current_speed=0, distance_travelled=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled
    def __str__(self):
        return f'{self.reg_number} {self.max_speed} km/h {self.current_speed} km/h {self.distance_travelled} km'
    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.distance_travelled += hours * self.current_speed

class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        super().__init__(reg_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, tank_volume):
        super().__init__(reg_number, max_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(100)
gasoline_car.accelerate(120)

electric_car.drive(3)
gasoline_car.drive(3)

print("Car details after 3 hours of driving:")
print(electric_car)
print(gasoline_car)
