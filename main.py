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


# def go_up():
#     if snake_segments[0].heading() != 270:
#         snake_segments[0].setheading(90)
#
#
# def go_right():
#     if snake_segments[0].heading() != 180:
#         snake_segments[0].setheading(0)
#
#
# def go_left():
#     if snake_segments[0].heading() != 0:
#         snake_segments[0].setheading(180)
#
#
# def go_down():
#     if snake_segments[0].heading() != 90:
#         snake_segments[0].setheading(270)


game_is_on = True
while game_is_on:

    # screen.onkey(go_up, "Up")
    # screen.onkey(go_down, "Down")
    # screen.onkey(go_left, "Left")
    # screen.onkey(go_right, "Right")
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
