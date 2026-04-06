import turtle

# setup screen
wn = turtle.Screen()
wn.bgcolor("lightblue")  # background color

t = turtle.Turtle()
t.color("brown")  # turtle color
t.pensize(3)

# DRAW SQUARE (HOUSE BASE) using FOR LOOP
side = 150
for i in range(4):
    t.forward(side)
    t.left(90)

# move to top of square
t.left(90)
t.forward(side)
t.right(90)

# DRAW TRIANGLE (ROOF) using WHILE LOOP
count = 0
while count < 3:
    t.forward(side)
    t.left(120)
    count += 1

# optional: add a door
t.penup()
t.goto(50, 0)
t.pendown()
t.color("black")

for i in range(2):
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)

# finish
wn.mainloop()
