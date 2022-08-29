# This program uses tkinter to build a user interface that implements
# turtle to build the requested koch snowflake
# By Yashna Shetty - 2901410
from tkinter import *
import turtle
from turtle import *

# Function that builds the GUI.
# The button makes a call to the buttonClick function
# That builds the user specified degree koch snowflake


def GUIuser():
    root = Tk()
    root.title("Koch Snowflake")

    instructionLabel = Label(
        root, text="Exit the graphics window to start a new drawing!")
    instructionLabel.pack()

    frame1 = LabelFrame(root, padx=50, pady=50)
    frame1.pack(padx=5, pady=5)

    instructionLabel2 = Label(
        frame1, text="I only accept whole integers :)")
    instructionLabel2.pack()

    inputLevel = Entry(frame1, width=20, borderwidth=5)
    inputLevel.pack()

    frame2 = Frame(root)
    frame2.pack()

    buildButton = Button(frame2, text="Build!",
                         command=lambda: buttonClick(turtle, turtle.getscreen().window_width() * 0.5, inputLevel.get()))
    buildButton.pack()

    return root


# function uses turtle
# specifies what the program should do
# when the user clicks the button
# makes a call to buildSnowflake function
# exits graphics window when the user closes
# the graphics window


def buttonClick(turtle, lengthSide, levels):
    try:
        levels = int(levels) - 1
    except:
        return

    clear()

    turtle.penup()

    turtle.setx(0)
    turtle.sety(0)

    turtle.backward(lengthSide/2)
    turtle.left(90)
    turtle.forward(lengthSide/2)
    turtle.right(90)

    turtle.TurtleScreen._RUNNING = True

    if ((levels + 1) <= 6):
        turtle.tracer(n=2)
    elif ((levels + 1) <= 7):
        turtle.tracer(n=3)
    elif ((levels + 1) <= 8):
        turtle.tracer(n=10)
    else:
        turtle.tracer(n=100)
    turtle.hideturtle()
    turtle.speed("fastest")

    turtle.penup()

    turtle.pendown()

    for i in range(3):
        buildSnowflake(turtle, lengthSide, levels)
        turtle.right(120)

    turtle.exitonclick()


# specifies how to
# build the koch snowflake to the desired degree
# recursive function


def buildSnowflake(turtle, lengthSide, levels):
    if levels == 0:
        turtle.forward(lengthSide)
        return
    lengthSide /= 3.0
    buildSnowflake(turtle, lengthSide, levels-1)
    turtle.left(60)
    buildSnowflake(turtle, lengthSide, levels-1)
    turtle.right(120)
    buildSnowflake(turtle, lengthSide, levels-1)
    turtle.left(60)
    buildSnowflake(turtle, lengthSide, levels-1)

# main function that begins the program


def main():
    GUIuser().mainloop()


main()
