from turtle import Turtle

import road
from road import height, WIDTH
import car_manager

FONT1 = ('Courier', 10, 'normal')
FONT2 = ('Courier', 30, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.alive = True
        self.level_passed = False
        self.penup()
        self.hideturtle()
        self.pencolor('White')

    def write_score(self):
        from road import height
        self.clear()
        self.setpos(-WIDTH / 2 + 10, height / 2 - 20)
        self.write(f'HighScore: {self.high_score}', align='left', font=FONT1)
        self.setpos(-WIDTH / 2 + 10, height / 2 - 40)
        self.write(f'Score: {self.score}', align='left', font=FONT1)

    def write_game_over(self):
        from road import height
        self.clear()
        if self.high_score > self.score:
            self.setpos(0, -20)
            self.write(f'Final Score: {self.score}', align='center', font=FONT1)

        else:
            self.high_score = self.score
            self.setpos(0, -20)
            self.write(f'NEW HighScore: {self.high_score}', align='center', font=FONT1)
        self.setpos(-WIDTH / 2 + 10, height / 2 - 20)
        self.write(f'HighScore: {self.high_score}', align='left', font=FONT1)
        self.setpos(-WIDTH / 2 + 10, height / 2 - 40)
        self.write(f'Score: {self.score}', align='left', font=FONT1)
        self.setpos(0, 0)
        self.write('GAME OVER', align='center', font=FONT2)
        self.setpos(0, -40)
        self.write('Press \'space\' to start a new game.', align='center', font=FONT1)


    def reached_sidewalk(self, player):
        if player.ycor() >= road.height/2 -60:
            player.sety(-road.height/2 +35)
            self.level_passed = True
            if road.total_number_of_roads < 12:
                road.total_number_of_roads += 1
                road.height = road.total_number_of_roads*50 + 120
            elif car_manager.speed_increase > 0.05:
                car_manager.speed_increase = car_manager.speed_increase *0.925

            self.score += 1
            self.write_score()

    def collision_detector(self, car_list, player):
        for car in car_list:
            if self.alive and car.xcor() + 20 >= player.xcor() >=car.xcor() - 20 and car.ycor() + 10 >= player.ycor() >= car.ycor() - 10:
                print('Turty got run over...')
                player.color('red')
                self.alive = False
                player.alive = False

