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
        for seg_num in range(len(self.snake_segments) - 1,  0, -1):
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto((new_x, new_y))

        self.snake_segments[0].fd(20)

