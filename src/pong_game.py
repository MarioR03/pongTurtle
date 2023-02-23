from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

#code for the screen/display
display = Screen()._root
display.title("Pong by Mario Rodriguez")
display.bgcolor("cyan")
display.setup(width=800, height=600)
display.tracer(0)

#creating the turtle objects
leftP_obj = Paddle(-350,0)
rightP_obj = Paddle(350,0)
ball_obj = Ball()

#getting key inputs
display.listen()
display.onkeypress(leftP_obj.move_up, "w")
display.onkeypress(leftP_obj.move_down, "s")
display.onkeypress(rightP_obj.move_up, "Up")
display.onkeypress(rightP_obj.move_down, "Down")

#creating the scoreboard
playerOneScore = 0
playerTwoScore = 0

score_obj = Turtle()
score_obj.speed(0)
score_obj.color("black")
score_obj.penup()
score_obj.hideturtle()
score_obj.goto(0, 260)
score_obj.write("{}      {}".format(playerOneScore, playerTwoScore), align="center", font=("Arial", 16, "normal"))

while True:
    display.update()

    ball_obj.movement()

    if (ball_obj.get_x() > 340) and (ball_obj.get_x() < 350) and (ball_obj.get_y() < rightP_obj.get_y() + 40) and (ball_obj.get_y() > rightP_obj.get_y() - 40):
        ball_obj.setx(340)
        ball_obj.longi_bounce()
    
    if (ball_obj.get_x() < -340) and (ball_obj.get_x() > -350) and (ball_obj.get_y() < leftP_obj.get_y() + 40) and (ball_obj.get_y() > leftP_obj.get_y() - 40):
        ball_obj.setx(-340)
        ball_obj.longi_bounce()

    if (ball_obj.rightGoal == True):
        playerOneScore += 1
        ball_obj.rightGoal = False
        score_obj.clear()
        score_obj.write("{}     {}".format(playerOneScore, playerTwoScore), align="center", font=("Arial", 16, "normal"))

    elif (ball_obj.leftGoal == True):
        playerTwoScore += 1
        ball_obj.leftGoal = False
        score_obj.clear()
        score_obj.write("{}     {}".format(playerOneScore, playerTwoScore), align="center", font=("Arial", 16, "normal"))

    #moving the ball
#    ball_obj.ball.sety(ball_obj.ball.ycor() + ball_obj.ball.dx)