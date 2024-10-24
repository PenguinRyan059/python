import random
import turtle #IAmIrrelevant

wn = turtle.Screen(). bgcolor("white")
turt = turtle.Turtle()
turtsec = turtle.Turtle()

x = input("What Shape do you want?(Square, Triangle, Circle, or Hexagon)")
if x == "Square":
    for _ in range(2):
        turtsec.forward(50)
        turtsec.left(90)

wn.exitonclick()
