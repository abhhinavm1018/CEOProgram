import pygame

# Initialize the game engine
pygame.init()

# Define some colors
WHITE = (255, 255, 255)
TEXT_OUTPUT = 'Times clicked: '
BLUE_COLOR = 0
RED_COLOR = 0
GREEN_COLOR = 0

# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Text Color")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
text_rotate_degrees = 0

# Trackers for clicks
count_blue = 0
count_red = 0
count_green = 0
# Loop as long as done == False
while not done:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_b]:
        BLUE_COLOR = ((BLUE_COLOR + 1) % 255)
        count_blue += 1
    if keys[pygame.K_g]:
        GREEN_COLOR = ((GREEN_COLOR+ 1) % 255)
        count_green += 1
    if keys[pygame.K_r]:
        RED_COLOR = ((RED_COLOR + 1) % 255)
        count_red += 1

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Animated rotation
    output = str(count_blue) + " ticks blue\n" + str(count_red) + " ticks red\n" + str(count_green) + " ticks green"
    text = font.render(output, True, (RED_COLOR, GREEN_COLOR, BLUE_COLOR))
    text = pygame.transform.rotate(text, text_rotate_degrees)
    text_rotate_degrees += 1
    screen.blit(text, [100, 50])

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
