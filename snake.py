from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_segments.append(snake)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto((new_x, new_y))

        self.head.fd(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
