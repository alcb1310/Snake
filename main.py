from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snakes = []
x_position = 0
width = 5
for _ in range(3):
    snake = Turtle("square")
    snake.resizemode("user")
    snake.shapesize(stretch_wid=0.5, stretch_len=1)
    snake.color("white")
    snake.penup()
    snake.goto(x=x_position, y=0)
    x_position -= 20
    snakes.append(snake)




screen.exitonclick()
