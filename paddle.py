from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle = []
        self.create_paddle(position)

    def create_paddle(self, position):
        segment_x = 350
        if position == "left":
            segment_x *= -1
        segment_y = 50
        for _ in range(5):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setposition(segment_x, segment_y)
            segment.setheading(90)
            segment_y -= 20
            self.paddle.append(segment)

    def move_up(self):
        if not self.paddle[0].ycor() > 260:
            for segment in self.paddle:
                segment.forward(20)

    def move_down(self):
        if not self.paddle[4].ycor() < -260:
            for segment in self.paddle:
                segment.backward(20)
