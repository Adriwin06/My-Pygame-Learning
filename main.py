import pygame
# Initializing
pygame.init()

# Game Window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Test Python Game')


# Player Actions
moving_left = False
moving_right = False
moving_up = False
moving_down = False


# Defining the Player Class
class Soldier(pygame.sprite.Sprite):
    def __init__(self, x= 400, y=400, scale=0.1, speed=1):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load('img/player/idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right, moving_up, moving_down):
        

    # Drawing the Soldier to the screen
    def draw(self):
        screen.blit(self.image, self.rect)

# Creating the Player
player = Soldier()

# Game Loop
run = True
while run:

    # Making the backgroung Dark
    screen.fill((0, 0, 0))

    # Drawing the player on the screen
    player.draw()
    
    # Getting pressed keyboard keys
    if event.type == pygame.KEYDOWN:
        # Moving Logic
        if event.key == pygame.K_q:
            moving_left = True
        if event.key == pygame.K_d:
            moving_right = True
        if event.key == pygame.K_z:
            moving_up = True
        if event.key == pygame.K_s:
            moving_down = True
        
        # Escape escpae the game
        if event.key == pygame.K_ESCAPE:
            run = False

    # Getting released keyboard keys
    if event.type == pygame.KEYUP:
        # Moving Logic
        if event.key == pygame.K_q:
            moving_left = False
        if event.key == pygame.K_d:
            moving_right = False
        if event.key == pygame.K_z:
            moving_up = False
        if event.key == pygame.K_s:
            moving_down = False

# Event Handler
    for event in pygame.event.get():
        # Quit the Game
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()