from turtle import Turtle
Alignment = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard:

    def __init__(self):
        self.create_middle_line()
        self.right_score_value = 0
        self.right_score_text = self.create_score(100, self.right_score_value)
        self.left_score_value = 0
        self.left_score_text = self.create_score(-100, self.left_score_value)

    def create_middle_line(self):
        middle_line = Turtle()
        middle_line.color("white")
        middle_line.hideturtle()
        middle_line.penup()
        middle_line.goto(0, -290)
        middle_line.setheading(90)
        middle_line.pensize(5)
        while middle_line.ycor() < 280:
            middle_line.penup()
            middle_line.forward(20)
            middle_line.pendown()
            middle_line.forward(10)

    def create_score(self, score_x, score):
        each_score = Turtle()
        each_score.hideturtle()
        each_score.color("white")
        each_score.penup()
        each_score.goto(score_x, 260)
        self.refresh_score(each_score, score)
        return each_score

    def refresh_score(self, score_text, score_value):
        score_text.clear()
        score_text.write(arg=f"score: {score_value}", align=Alignment, font=FONT)
