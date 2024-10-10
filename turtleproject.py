import turtle

wn = turtle.Screen()
jim = turtle.Turtle()

distance = 10
for _ in range(50):
    jim.forward(distance)
    jim.right(90)
    distance += 10

wn.exitonclick()