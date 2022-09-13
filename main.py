from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()

snake = Snake()
screen.update()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")


screen.exitonclick()
