import turtle
a = int(input("enter value of x:"))
#Function for square
window = turtle.Screen()
turtle.speed(5)
turtle.pensize(5)
turtle.penup()


turtle.goto(-100,100)
turtle.color("black")
turtle.pendown()
for i in range(4):
    turtle.forward(a)
    turtle.left(90)
turtle.penup()

#Function for circle

turtle.goto(-90,-250)
turtle.pendown()
turtle.circle(a)
turtle.end_fill()

window.exitonclick()
window.mainloop()


