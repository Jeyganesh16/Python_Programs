import turtle
screen = turtle.Screen()
screen.title("Left-Justified Tangent Circles")
t = turtle.Turtle()
t.speed(2)
t.pensize(2)
t.color("blue")
radius = 30
num_circles = 10
start_x = -screen.window_width() // 2 + radius
for i in range(num_circles):
    t.penup()
    t.goto(start_x + i * 2 * radius, 0)
    t.pendown()
    t.circle(radius)
turtle.done()
