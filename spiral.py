import turtle
spiral = turtle.Turtle()
spiral.speed(0) 
spiral.pensize(2)
spiral.color("orange")
radius = 10
for i in range(60):
    spiral.circle(radius + i) 
    spiral.left(90) 
turtle.done()
