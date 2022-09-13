from turtle import Turtle, Screen

snake = Turtle("square")
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake.resizemode("user")
snake.shapesize(stretch_wid=0.50)
snake.color("white")



screen.exitonclick()
