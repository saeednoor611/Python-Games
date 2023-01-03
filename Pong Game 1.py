# Pong by Noor
import turtle

# setup window
wn = turtle.Screen()
wn.title("Prong by Noor Saeed")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) #it will stop window from updating.


# set paddles A and B

# paddle A
paddle_a = turtle.Turtle() # here Turtle with capital T is a class not modle turtle
paddle_a.speed(0) # this is not the speed of moving paddle A but this is the speed of animation for turtle
paddle_a.shape("square") #adding shape (there are built shape)
paddle_a.color("white")
paddle_a.penup() #turtle allows to draw line but we don't need it so we use penup()
paddle_a.goto(-350,0) # paddle start at -350 (x-axis) 0 (vertically at center)
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #giving shape width with length

# paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
# dividing ball movement into x an y coordinates
ball.dx = 3 # 3 means eveytime ball moves by 3 pixels
ball.dy = -3




# couple of functions for moving paddles
def paddle_a_up():
    y = paddle_a.ycor() #ycor() is turtle funcition that helps you to move towards y coordinate
    y += 20 # that will add 20 pixels to the y coordinate
    paddle_a.sety(y)   # here sety() will calculate the new y
def paddle_a_down():
    y = paddle_a.ycor() #ycor() is turtle funcition that helps you to move towards y coordinate
    y -= 20 # that will decrease 20 pixels to the y coordinate
    paddle_a.sety(y)   # here sety() will calculate the new y
def paddle_b_up():
    y = paddle_b.ycor() #ycor() is turtle funcition that helps you to move towards y coordinate
    y += 20 # that will add 20 pixels to the y coordinate
    paddle_b.sety(y)   # here sety() will calculate the new y
def paddle_b_down():
    y = paddle_b.ycor() #ycor() is turtle funcition that helps you to move towards y coordinate
    y -= 20 # that will decrease 20 pixels to the y coordinate
    paddle_b.sety(y)   # here sety() will calculate the new y


# keyboards binding
wn.listen() # this tells us to listen from keyboard
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# game main loop
import time  # stack overflow (ball speed slow)
gameloop = True
while gameloop:
    time.sleep(1 / 60) #stack overflow
    wn.update() # on each iteration of loop it will update window
    # ball movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # border checking
    # top checking
    if(ball.ycor() >290):          # wn = 600, ball=20, half of wn = 300, so, 290
        ball.sety(290)
        ball.dy *= -1
    # bottom checking
    if (ball.ycor() < -290):       # wn = 600, ball=20, half of wn = 300, so, 290
        ball.sety(-290)
        ball.dy *= -1


    # # left and right checking on x-axis
    if ball.xcor() > 390:          # wn = 800,ball=20,half = 400, 390
        ball.goto(0,0)             #back to center
        ball.dx *= -1
    if ball.xcor() < -390:        # wn = 800,ball=20,half = 400, 390
        ball.goto(0,0)           #back to center
        ball.dx *= -1


    # paddle and ball collision
    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50: