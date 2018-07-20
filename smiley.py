"""
title: smiley
author: Abhinav Mugunda
date: 7/20/18 9:42 AM
"""

# -*- coding: utf-8 -*-
"""
 Simple graphics demo

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (246, 226, 51)
BROWN = (139, 69, 19)
ORANGE = (255, 128, 0)
PI = 3.141592653

# Set the height and width of the screen
size = (800, 2000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Set Up")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


def draw_stick_figure(x, y):
    # The face
    pygame.draw.circle(screen, BROWN, [400+x, 200+y], 150)

    # The eyes
    pygame.draw.ellipse(screen, BLACK, [300+x, 130+y, 70, 40])
    pygame.draw.ellipse(screen, BLACK, [420+x, 130+y, 70, 40])

    # The mouth
    pygame.draw.arc(screen, BLACK, [325+x, 200+y, 150, 125], PI, 2 * PI, 5)

    # The nose
    pygame.draw.polygon(screen, BLACK, [[375+x, 200+y], [425+x, 200+y], [400+x, 225+y]])

    # The Body
    # Torso
    pygame.draw.line(screen, BLACK, [400+x, 350+y], [400+x, 800+y], 5)
    # Legs
    pygame.draw.line(screen, BLACK, [400+x, 800+y], [600+x, 1200+y], 5)
    pygame.draw.line(screen, BLACK, [400+x, 800+y], [200+x, 1200+y], 5)
    # Arms
    pygame.draw.line(screen, BLACK, [400+x, 600+y], [200+x, 400+y], 5)
    pygame.draw.line(screen, BLACK, [400+x, 600+y], [600+x, 400+y], 5)


def draw_basketballs(x, y, z):
    # The ball
    pygame.draw.circle(screen, ORANGE, [700+x, 400+y-z], 100)

x_coord = 0
y_coord = 0
x_speed = 0
y_speed = 0
bball_bounce = 3
bball_coord = 0

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -30
            elif event.key == pygame.K_RIGHT:
                x_speed = 30
            elif event.key == pygame.K_UP:
                y_speed = -30
            elif event.key == pygame.K_DOWN:
                y_speed = 30
            elif event.key == pygame.K_SPACE:
                bball_bounce = -100
            elif event.key == pygame.K_v:
                bball_bounce = 100
        elif event.type == pygame.KEYUP:
            y_speed = 0
            x_speed = 0

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    if bball_coord > 0:
        bball_bounce = -100
    elif bball_coord < -400:
        bball_bounce = 100



    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    bball_coord += bball_bounce
    print(bball_coord)


    draw_stick_figure(x_coord, y_coord)
    draw_basketballs(x_coord, y_coord, bball_coord)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen

    # Put the image of the text on the screen at 250x250

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while (139,69,19)loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(600)



# Be IDLE friendly
pygame.quit()
