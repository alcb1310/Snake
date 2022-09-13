from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()

snake_segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    snake = Turtle("square")
    # snake.resizemode("user")
    # snake.shapesize(stretch_wid=0.5, stretch_len=1)
    snake.color("white")
    snake.penup()
    snake.goto(position)
    snake_segments.append(snake)
screen.update()


def go_up():
    if snake_segments[0].heading() != 270:
        snake_segments[0].setheading(90)


def go_right():
    if snake_segments[0].heading() != 180:
        snake_segments[0].setheading(0)


def go_left():
    if snake_segments[0].heading() != 0:
        snake_segments[0].setheading(180)


def go_down():
    if snake_segments[0].heading() != 90:
        snake_segments[0].setheading(270)


game_is_on = True
while game_is_on:

    for seg_num in range(len(snake_segments) - 1,  0, -1):
        new_x = snake_segments[seg_num-1].xcor()
        new_y = snake_segments[seg_num-1].ycor()
        snake_segments[seg_num].goto((new_x, new_y))
    snake_segments[0].fd(20)
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")

    time.sleep(0.1)
    screen.update()


screen.exitonclick()
