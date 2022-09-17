from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()

snake = Snake()
food = Food()
score = ScoreBoard()
screen.update()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() <= -290 or snake.head.ycor() >= 270:
        score.reset()
        snake.reset()

    # Detect collision with itself:
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

score.end_game()

screen.exitonclick()
