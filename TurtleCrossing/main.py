import time
from turtle import Screen

import car_manager
import road
from car_manager import CarManager
from road import Road
from player import Animal
from scoreboard import ScoreBoard

score_board = ScoreBoard()
pressed_space = False

def press_space():
    global pressed_space
    pressed_space = True

def start_level():
    from road import height, WIDTH
    road = Road()
    road.make_screen()
    road.paint_sidewalks()
    road.paint_roads(disc_dist=5)

    car_man = CarManager(WIDTH, road.number_of_roads)
    player = Animal(height)
    score_board.write_score()
    road.screen.update()
    road.screen.listen()

    # while score_board.alive:
    road.screen.onkey(player.move_forwards, 'Up')
    road.screen.onkey(player.move_backwards, 'Down')
    road.screen.onkey(player.move_right, 'Right')
    road.screen.onkey(player.move_left, 'Left')
    road.screen.onkey(press_space, 'space')


    counter = 0
    while counter < int(WIDTH / 10 + 10):
        car_man.car_generator()
        car_man.move_cars()
        counter += 1

    while not score_board.level_passed and score_board.alive:
        time.sleep(car_manager.SPEED*car_manager.speed_increase)
        car_man.car_generator()
        car_man.move_cars()
        score_board.collision_detector(car_man.cars, player)
        score_board.reached_sidewalk(player)
        road.screen.update()

    if not score_board.alive:
        score_board.write_game_over()
    elif score_board.level_passed:
        road.screen.clear()
        del road
        return

    while not score_board.alive and not pressed_space:
        time.sleep(car_manager.SPEED * car_manager.speed_increase)
        car_man.car_generator()
        car_man.move_cars()
        road.screen.update()

    road.screen.clear()
    del road
    return

while True:
    while score_board.alive:
        score_board.level_passed = False
        start_level()

    score_board.score = 0
    road.total_number_of_roads = 6
    road.height = road.total_number_of_roads * 50 + 120
    car_manager.speed_increase = 1
    pressed_space = False
    score_board.alive = True
