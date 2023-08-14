import pygame
import sys
import serial

# Initialize Pygame
pygame.init()

# Establish serial connection
ser = serial.Serial('COM8', 9600) # Change the port with to your arduino port

# Set up the window
width, height = 770, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vehicle Control Buttons")

# Define colors
WHITE = ("#19D9FF")
BLACK = ("#000000")
RED = ("#000000")
GREEN = ("#000000")
BLUE = ("#000000")
YELLOW = ("#000000")
ORANGE = ("#000000")

# Define button dimensions
button_width, button_height = 100, 100
button_padding = 10

# Define button positions
left_button_positions = [
    (240, 75),
    (345, 75),
    (450, 75),
    (240, 190),
    (345, 190),
    (450, 190)
]

left_button_labels = ['Q', 'W', 'E', 'A', 'S', 'D']

# Define button colors
button_colors = [
    RED,
    GREEN,
    BLUE,
    YELLOW,
    ORANGE,
    BLACK,
    BLACK]

# Create the font for button labels
font = pygame.font.Font(None, 24)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        ser.write(b'w')  # Send 'w' to Arduino for forward movement
    elif keys[pygame.K_s]:
        ser.write(b's')  # Send 's' to Arduino for backward movement
    elif keys[pygame.K_q]:
        ser.write(b'q') # Send 'q' to Arduino for stopping the motor
    elif keys[pygame.K_a]:
        ser.write(b'a') # Send 'a' to Arduino for turning left
    elif keys[pygame.K_d]:
        ser.write(b'd') # Send 'd' to Arduino for turning right

    # Clear the screen
    screen.fill(WHITE)

    # Draw left buttons
    for position, color, label in zip(left_button_positions, button_colors, left_button_labels):
        pygame.draw.rect(screen, color, (position[0], position[1], button_width, button_height))
        label_text = font.render(label, True, WHITE)
        label_rect = label_text.get_rect(center=(position[0] + button_width // 2, position[1] + button_height // 2))
        screen.blit(label_text, label_rect)



    # Update the display
    pygame.display.flip()