import turtle
import time

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.title("STRANGE TIME")
wn.tracer(0)

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(9)

def draw_clk(h,m,s,pen):
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("#aac3c3")
    pen.pendown() 
    pen.circle(219)
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    
    for i in range(60):
        if i % 5 == 0:
            pen.pensize(10)
            pen.penup()
            pen.forward(200*1.2)
            pen.pendown()
            pen.forward(10*1.2)
            pen.penup()
            pen.backward(210*1.2)
        else:
            pen.pensize(5)
            pen.penup()
            pen.forward(200*1.2)
            pen.pendown()
            pen.forward(5*1.2)
            pen.penup()
            pen.backward(205*1.2)      
        pen.right(6)
    
    pen.penup()
    pen.goto(0,0)
    pen.color("#79487d")
    pen.setheading(90)
    angl=(h/12) * 360
    pen.rt(angl)
    pen.pendown()
    pen.fd(100)
    pen.pensize(8)
    
    pen.penup()
    pen.goto(0,0)
    pen.color("#79487d")
    pen.setheading(90)
    angl=(m / 60) * 360
    pen.rt(angl)
    pen.pendown()
    pen.fd(170)

    pen.penup()
    pen.goto(0,0)
    pen.color("#bab574")
    pen.setheading(90)
    angl=(s / 60) * 360
    pen.rt(angl)
    pen.pendown()
    pen.fd(50)

while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))       
    draw_clk(h,m,s,pen)
    wn.update()
    time.sleep(1)
    pen.clear()
wn.mainloop()