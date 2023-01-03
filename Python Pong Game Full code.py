import os
import turtle
# import os
import winsound

# setup window
wn = turtle.Screen() # window create
wn.title('Pong Game')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0) #it will stop window from updating.

# score
score_a = 0
score_b = 0



# Set Paddle A and B

# paddle_A
paddle_a = turtle.Turtle()# this is a class not module
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup() #turtle allows to draw line but we don't need it so we use penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)


# paddle_B
paddle_b = turtle.Turtle()# this is a class not module
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup() #turtle allows to draw line but we don't need it so we use penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)


# score pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Paddle A: 0  Paddle B: 0",align='center',font=('Courier',24,'normal'))


# movement of ball is divided into x and y coordinates
ball.dx = 3
ball.dy = -3



# couple of functions for moving paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)



# keyboards binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,"Down")


# game loop
import time
gameloop = True
while gameloop:
    time.sleep(1/60) # solved by stackoverflow
    wn.update()


    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # borer check

    # top and bottom check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverse direction
        # os.system("asplay boing.mp3")
        winsound.PlaySound('boing.pm3',winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverse direction
        winsound.PlaySound('boing.pm3',winsound.SND_ASYNC)



    # left and right check
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 2
        pen.clear()
        pen.write(f"Paddle A: {score_a}  Paddle B: {score_b}", align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('boing.pm3',winsound.SND_ASYNC)

    # left and right check
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 2
        pen.clear()
        pen.write(f"Paddle A: {score_a}  Paddle B: {score_b}", align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('boing.pm3',winsound.SND_ASYNC)


    # paddels and ball collisions
    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1