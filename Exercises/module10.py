# 1 Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.
class Elevator:
    current_floor = 0
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        Elevator.current_floor=self.bottom_floor
    def floor_up(self):
        if self.current_floor<self.top_floor:
            Elevator.current_floor+=1
            print("Elevator is on floor:", self.current_floor)
        else:
            print("no such floor")
    def floor_down(self):
        if Elevator.current_floor>self.bottom_floor:
            Elevator.current_floor-=1
            print("Elevator is on floor:", self.current_floor)
        else:
            print("no such floor")
    def go_to_floor(self, floor):
        while self.current_floor<floor:
            self.floor_up()
        while self.current_floor>floor:
            self.floor_down()

h=Elevator(1,5)
h.go_to_floor(5)
h.go_to_floor(1)

# 2 Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building. When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building. Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program, write the statements for creating a new building and running the elevators of the building.
class Elevator:
    current_floor = 0
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        Elevator.current_floor=self.bottom_floor
    def floor_up(self):
        if self.current_floor<self.top_floor:
            Elevator.current_floor+=1
            print("Elevator is on floor:", self.current_floor)
        else:
            print("no such floor")
    def floor_down(self):
        if Elevator.current_floor>self.bottom_floor:
            Elevator.current_floor-=1
            print("Elevator is on floor:", self.current_floor)
        else:
            print("no such floor")
    def go_to_floor(self, floor):
        while self.current_floor<floor:
            self.floor_up()
        while self.current_floor>floor:
            self.floor_down()

class Buildings():
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Moving elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Elevator number out of range.")

building = Buildings(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 7)

# 3 Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.
class Elevator:
    current_floor = 0
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        Elevator.current_floor=self.bottom_floor
    def floor_up(self):
        if self.current_floor<self.top_floor:
            Elevator.current_floor+=1
            print("Elevator is on floor:", self.current_floor)
        else:
            print("no such floor")
    def floor_down(self):
        if Elevator.current_floor>self.bottom_floor:
            Elevator.current_floor-=1
            print("Elevator is on floor:", self.current_floor)
        else:
            print("no such floor")
    def go_to_floor(self, floor):
        while self.current_floor<floor:
            self.floor_up()
        while self.current_floor>floor:
            self.floor_down()

class Buildings():
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Moving elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Elevator number out of range.")

    def fire_alarm(self):
        print("Fire alarm! Moving all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i} going to bottom floor.")
            elevator.go_to_floor(self.bottom_floor)

building = Buildings(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 7)
building.fire_alarm()
# 4 This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race. The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class. The class has the following methods:

#hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
#print_status, which prints out the current information of each car as a clear, formatted table.
#race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
#Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.
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
        return self.current_speed
    def drive(self, hours):
        self.distance_travelled=(hours*self.current_speed)+self.distance_travelled
        return self.distance_travelled

class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate()
            car.drive()

    def print_status(self):
        print(f"Registration Number | Maximum Speed | Current Speed | Distance Travelled")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.reg_number:19} | {car.max_speed:13} | {car.current_speed:13} | {car.distance_travelled:17}")

    def race_finished(self):
        return any(car.distance_driven >= self.distance_km for car in self.cars)


# Main program to simulate the race
cars = [Car(f"Car {i+1}", random.randint(100, 200)) for i in range(10)]
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\nAfter {hours} hours:")
        race.print_status()

# Print final status after the race is complete
print("\nFinal Race Status:")
race.print_status()