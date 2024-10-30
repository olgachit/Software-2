# 1 Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.
'''
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
'''
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

# 3 Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.

# 4 This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race. The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class. The class has the following methods:

#hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
#print_status, which prints out the current information of each car as a clear, formatted table.
#race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
#Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.