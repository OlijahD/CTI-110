# Name: Olijah Dowtin
# Assignment: P4LAB1 - Turtle House
# Purpose: Draw a square and triangle using a for loop and a while loop.
#
# Pseudocode:
# 1. Import turtle and set the background color.
# 2. Create a turtle with a different color from the background.
# 3. Move to the bottom-left corner of the house.
# 4. Use a for loop to draw four sides of a square.
# 5. Move to the top-left corner of the square.
# 6. Use a while loop to draw three sides of a triangle roof.
# 7. Keep the drawing window open until the user closes it.

import turtle

# Set up the drawing window.
window = turtle.Screen()
window.title("P4LAB1 - Olijah Dowtin's House")
window.setup(width=700, height=600)
window.bgcolor("lightblue")

# Set up the drawing turtle.
artist = turtle.Turtle()
artist.shape("turtle")
artist.color("navy")
artist.pensize(4)
artist.speed(3)

# Draw the square house with a for loop.
artist.penup()
artist.goto(-100, -150)
artist.pendown()

for side in range(4):
    artist.forward(200)
    artist.left(90)

# Move to the top-left corner and point toward the roof peak.
artist.penup()
artist.goto(-100, 50)
artist.setheading(60)
artist.pendown()

# Draw the triangle roof with a while loop.
side = 0
while side < 3:
    artist.forward(200)
    artist.right(120)
    side += 1

# Keep the output window open.
turtle.done()