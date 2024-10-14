import random
import turtle #IAmIrrelevant

wn = turtle.Screen(). bgcolor("white")
turt = turtle.Turtle()
turtsec = turtle.Turtle()

ColorRandom = random.randint(1, 2)
distance = 10
RandCalc = random.randint(1, 2)
if RandCalc == 1:
    for _ in range(50):
       turtsec.forward()
    for _ in range(50):
        if ColorRandom == 1:
            wn = turtle.Screen(). bgcolor("red")
            ColorRandom = 2
        else:
           if ColorRandom == 2:
              wn = turtle.Screen(). bgcolor("blue")
              ColorRandom = 1
        turt.forward(distance)
        turt.right(90)
        distance += 10
else:
    if RandCalc == 2:
     for _ in range(25):
        if ColorRandom == 1:
            wn = turtle.Screen(). bgcolor("yellow")
            ColorRandom = 2
        else:
           if ColorRandom == 2:
              wn = turtle.Screen(). bgcolor("green")
              ColorRandom = 1
        turt.forward(distance)
        turt.right(45)
        distance += 5

wn.exitonclick()
