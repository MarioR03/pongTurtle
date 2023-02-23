import turtle

class Ball:
    rightGoal = False
    leftGoal = False

    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("black")
        self.ball.penup()
        self.ball.goto(0,0)
        
        #movement variables
        self.ball.dx = .03
        self.ball.dy = .03

    #getters
    def get_x(self):
        return self.ball.xcor()
    
    def get_y(self):
        return self.ball.ycor()
    
    def get_dx(self):
        return self.ball.dx
    
    def get_dy(self):
        return self.ball.dy
    
    #setters
    def set_dx(self, dx):
        self.ball.dx = dx

    def set_dy(self, dy):
        self.ball.dy = dy

    def setx(self, x = None):
        if x == None:
            self.ball.setx(self.get_x() + self.get_dx())
        else:
            self.ball.setx(x)

    def sety(self, y = None):
        if y == None:
            self.ball.sety(self.get_y() + self.get_dy())
        else:
            self.ball.sety(y)

    #helper bounce methods
    def longi_bounce(self):
        dx = self.get_dx()
        dx *= -1
        self.set_dx(dx)

    def lati_bounce(self):
        dy = self.get_dy()
        dy *= -1
        self.set_dy(dy)

    def movement(self):
        self.setx()
        self.sety()

        if self.get_y() > 290:
            self.sety(290)
            self.lati_bounce()

        if self.get_x() > 390:
            self.ball.goto(0,0)
            self.longi_bounce()
            self.leftGoal = True

        if self.get_y() < -290:
            self.sety(-290)
            self.lati_bounce()

        if self.get_x() < -390:
            self.ball.goto(0,0)
            self.longi_bounce()
            self.rightGoal = True
