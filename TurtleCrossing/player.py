from turtle import Turtle

class Animal(Turtle):
    def __init__(self, height):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setx(0)
        self.sety(-height/2 +35)
        self.color('Green')
        self.setheading(90)
        self.alive = True
        self.x_jumps = 0

    def move_forwards(self):
        if self.alive:
            self.setheading(90)
            self.sety(self.ycor()+50)

    def move_backwards(self):
        if self.alive:
            self.setheading(270)
            self.sety(self.ycor()-50)

    def move_right(self):
        if self.alive and self.x_jumps < 5:
            self.setheading(0)
            self.setx(self.xcor()+50)
            self.x_jumps += 1

    def move_left(self):
        if self.alive and self.x_jumps > -5:
            self.setheading(180)
            self.setx(self.xcor()-50)
            self.x_jumps -= 1

