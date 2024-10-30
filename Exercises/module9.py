# 1 Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance. Add a class initializer that sets the first two of the properties based on parameter values. The current speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.
class Car:
    def __init__(self, reg_number, max_speed, current_speed=0, distance_travelled=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled
    def __str__(self):
        return f'{self.reg_number} {self.max_speed} {self.current_speed} {self.distance_travelled}'

car = Car("ABC-123", "142 km/h")
print(str(car))
# 2 Extend the program by adding an accelerate method into the new class. The method should receive the change of speed (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero. Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed. The travelled distance does not have to be updated yet.
class Car:
    def __init__(self, reg_number, max_speed, current_speed=0, distance_travelled=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled
    def __str__(self):
        return f'{self.reg_number} {self.max_speed} {self.current_speed} {self.distance_travelled}'
    def accelerate(self, speed_change):
        self.current_speed += speed_change

        return self.current_speed

car = Car("ABC-123", "142 km/h")
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"{car.current_speed} km/h")
car.accelerate(-200)
print(f"{car.current_speed} km/h")
# 3 Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method increases the travelled distance by how much the car has travelled in constant speed in the given time. Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.
class Car:
    def __init__(self, reg_number, max_speed, current_speed=0, distance_travelled=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled
    def __str__(self):
        return f'{self.reg_number} {self.max_speed} {self.current_speed} {self.distance_travelled}'
    def accelerate(self, speed_change):
        self.current_speed += speed_change
        return self.current_speed
    def drive(self, hours):
        self.distance_travelled=(hours*self.current_speed)+car.distance_travelled
        return self.distance_travelled

car = Car("ABC-123", "142 km/h")
car.accelerate(60)
car.distance_travelled=2000
car.drive(1.5)
print(f"{car.distance_travelled} km")
# 4 Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are performed:

# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accerelate method.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are printed out formatted into a clear table.
import random

class Car:
    def __init__(self, reg_number, max_speed, current_speed=0, distance_travelled=0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled
    def __str__(self):
        return f'{self.reg_number} {self.max_speed} {self.current_speed} {self.distance_travelled}'
    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.distance_travelled += hours * self.current_speed

class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars
    def hour_passes(self):
        # For each car, adjust speed randomly and update distance
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
    def print_status(self):
        # Print out the status of each car in a formatted table
        print(f"{'Registration Number':<19} | {'Max Speed':<13} | {'Current Speed':<13} | {'Distance Travelled':<17}")
        print("-" * 70)
        for car in self.cars:
            print(f"{car.reg_number:<19} | {car.max_speed:<13} | {car.current_speed:<13} | {car.distance_travelled:<17}")
    def race_finished(self):
        # Check if any car has reached or exceeded the race distance
        return any(car.distance_travelled >= self.distance_km for car in self.cars)

cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
race = Race("Grand Demolition Derby", 8000, cars)

hours_passed = 0
while not race.race_finished():
    race.hour_passes()
    hours_passed += 1

    if hours_passed % 10 == 0:
        print(f"\nAfter {hours_passed} hours:")
        race.print_status()

print("\nFinal Race Status:")
race.print_status()
print(f"The race finished in {hours_passed} hours.")
