import turtle


class Paddle:
    def __init__(self, x, y):

        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("black")
        self.paddle.shapesize(4,1)
        self.paddle.penup()
        self.paddle.goto(x,y)

    def move_up(self):
        y_coor = self.paddle.ycor()
        if y_coor < 260:
            y_coor += 20
            self.paddle.sety(y_coor)

    def move_down(self):
        y_coor = self.paddle.ycor()
        if y_coor > -260:
            y_coor -= 20
            self.paddle.sety(y_coor)

    #getters
    def get_y(self):
        return self.paddle.ycor()
    #note, these are the coordinates of the center point of the paddle in each direction