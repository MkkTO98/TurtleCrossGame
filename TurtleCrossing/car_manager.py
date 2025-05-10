import random
from turtle import Turtle
from random import choice, randint

colors = ['purple', 'black', 'red', 'blue', 'white', 'yellow', 'brown']
SPEED = 0.1 #The lower the float the faster the cars go
speed_increase = 1 #multiplies with SPEED
amount_of_cars = 30 #Should never be lower than ~20. That lower that more cars.

class CarManager:
    def __init__(self, width, number_of_roads):
        self.width = width
        self.number_of_roads = number_of_roads
        self.cars = []
        #The first bool of roads indicates if a car has been created on it recently,
        #the first int how many instances left until a new one can be created and the
        #second the direction the cars on the road drive. The float is the lanespeed
        self.roads = []
        for _ in range(number_of_roads):
            lane_speed = random.randint(50, 150)/100
            if randint(0, 1) == 0:
                self.roads.append([False, 0, 0, lane_speed])
            else:
                self.roads.append([False, 0, 180, lane_speed])

    def car_generator(self):
        #Checks if a car has just been generated on that road and if there is space for a new one.
        for road_num in range(len(self.roads)):
            if self.roads[road_num][0] and self.roads[road_num][1] > 1:
                self.roads[road_num][1] -= 1
            elif self.roads[road_num][0] and self.roads[road_num][1] == 1:
                self.roads[road_num][0] = False
                self.roads[road_num][1] = 0


        for road_num in range(len(self.roads)):
            if not self.roads[road_num][0] and randint(0, amount_of_cars) == 0:
                ypos = road_num*50 + 25 - self.number_of_roads*25
                car = Car(self.width, ypos, self.roads[road_num][2], self.roads[road_num][3])
                self.cars.append(car)
                self.roads[road_num][0] = True
                self.roads[road_num][1] = int(5/self.roads[road_num][3]+0.5)


    def move_cars(self):
        i = 1
        for car in range(len(self.cars)):
            if self.cars[car-i].heading() == 180 and self.cars[car-i].xcor() >= -self.width/2 -50:
                self.cars[car-i].move_forwards(self.cars[car-i].line_speed)
            elif self.cars[car-i].heading() == 0 and self.cars[car-i].xcor() <= self.width/2 +50:
                self.cars[car-i].move_forwards(self.cars[car-i].line_speed)
            else:
                self.cars.pop(car-i)
                i += 1
                del car

class Car(Turtle):
    def __init__(self, width, ypos, direction, line_speed):
        super().__init__()
        self.shape('square')
        self.shapesize(1,2)
        self.color(choice(colors))
        self.penup()
        self.sety(ypos)
        self.setheading(direction)
        self.line_speed = line_speed
        if direction == 180:
            self.setx(width / 2 + 50)
        else:
            self.setx(-width / 2 - 50)

    def move_forwards(self, line_speed):
        self.forward(10*line_speed)