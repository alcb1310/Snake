from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snakes = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    snake = Turtle("square")
    # snake.resizemode("user")
    # snake.shapesize(stretch_wid=0.5, stretch_len=1)
    snake.color("white")
    snake.penup()
    snake.goto(position)
    snakes.append(snake)




screen.exitonclick()
