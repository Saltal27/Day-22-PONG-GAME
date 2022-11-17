from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)

    def bounce_of_wall(self):
        self.y_move *= -1

    def bounce_of_paddle(self):
        self.x_move *= -1

    def reset(self):
        self.home()
        self.x_move *= -1
