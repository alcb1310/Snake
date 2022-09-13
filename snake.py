from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_segments = []
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            snake = Turtle("square")
            # snake.resizemode("user")
            # snake.shapesize(stretch_wid=0.5, stretch_len=1)
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_segments.append(snake)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto((new_x, new_y))

        self.snake_segments[0].fd(20)

    def go_up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)

    def go_right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)

    def go_left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)

    def go_down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)
