import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

t.color("yellow")
for i in range(36):
    t.circle(50)
    t.right(10)

t.color("orange")
t.circle(100)

t.hideturtle()
turtle.done()
