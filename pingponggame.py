#pingponggame
import turtle as t
import os

player_a_score = 0
player_b_score = 0
  
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)
  
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)
  
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2
  
pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=('Arial', 24, 'normal'))

def leftpaddleup():
    y = leftpaddle.ycor()
    if y < 250:
        leftpaddle.sety(y + 20)
  
def leftpaddledown():
    y = leftpaddle.ycor()
    if y > -240:
        leftpaddle.sety(y - 20)
  
def rightpaddleup():
    y = rightpaddle.ycor()
    if y < 250:
        rightpaddle.sety(y + 20)
  
def rightpaddledown():
    y = rightpaddle.ycor()
    if y > -240:
        rightpaddle.sety(y - 20)
  
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')
  
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
  
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
          
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=('Arial', 24, 'normal'))
        os.system("afplay wallhit.wav&")
  
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=('Arial', 24, 'normal'))
        os.system("afplay wallhit.wav&")
  
    if (340 < ball.xcor() < 350) and (rightpaddle.ycor() - 50 < ball.ycor() < rightpaddle.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")
  
    if (-350 < ball.xcor() < -340) and (leftpaddle.ycor() - 50 < ball.ycor() < leftpaddle.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")

