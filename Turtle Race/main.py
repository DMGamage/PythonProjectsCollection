import random
import turtle
import time

WIDTH,HEIGHT = 500,500
COLORS = ['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def create_turtles(colors):
    turtles =[]
    spacingX =WIDTH//(len(colors)+1)

    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i+1)*spacingX , -HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            x,y = racer.pos()
            if y>=HEIGHT//2 -10:
                return colors[turtles.index(racer)]


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Please enter number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter valid number between (2-10)")
            continue
        if 2<=racers<=10:
            return racers
        else:
            print("Please enter value between (2-10)")

def init_turtle():
    screen = turtle.Screen().setup(WIDTH, HEIGHT)

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors=COLORS[:racers]
winner = race(colors)
print(f"The winner is  {winner.upper()} Turtle")





