from turtle import Turtle, Screen
from random import randint
total_number_of_roads = 6
height = total_number_of_roads*50 + 120 #roads will be 50 in height, sidewalks 60
WIDTH = 600

class Road:
    def __init__(self):
        self.screen = Screen()
        self.road_pen = Turtle()
        self.road_pen.speed(0)
        self.road_pen.hideturtle()
        self.road_pen.color('Black')
        self.road_pen.pensize(2)
        self.number_of_roads = total_number_of_roads


    def make_screen(self):
        self.screen.bgcolor('grey')
        self.screen.title('Cross Road Game')
        self.screen.tracer(0)
        self.screen.setup(WIDTH, height)

    def paint_sidewalks(self):
        print('Drawing sidewalks...')
        self.draw_line(height/2 -55)
        self.draw_line(height/2 -60)
        self.draw_line(-height / 2 + 55)
        self.draw_line(-height / 2 + 60)


    def paint_roads(self, disc_dist):
        print('Drawing roads...')
        for r in range(int((height-120)/50)):
            self.draw_discontinuous_line(60+r*50 -height/2, disc_dist)

    def draw_line(self, ypos):
        self.road_pen.penup()
        self.road_pen.setpos(-WIDTH/2, ypos)
        self.road_pen.setheading(0)
        self.road_pen.pendown()
        self.road_pen.forward(WIDTH)

    def draw_discontinuous_line(self, ypos, disc_dist):
        self.road_pen.penup()
        self.road_pen.setpos(-WIDTH / 2, ypos)
        self.road_pen.setheading(0)
        for _ in range(int(WIDTH/disc_dist)):
            self.road_pen.pendown()
            self.road_pen.forward(disc_dist)
            self.road_pen.penup()
            self.road_pen.forward(disc_dist*2)