import pygame
# Initializing
pygame.init()

# Game Window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Test Python Game')

# Set Framerate (So it doesn't go too crazy with higher framerate)
clock = pygame.time.Clock()
FPS = 120

# Player Actions
moving_left = False
moving_right = False
moving_up = False
moving_down = False


# Defining the Player Class
class Soldier(pygame.sprite.Sprite):
    def __init__(self, x= 400, y=400, scale=0.1, speed=3):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load('img/player/idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right, moving_up, moving_down):
        # reset movement variables
        dx = 0
        dy = 0


        # Assign movement variable if moving
        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed
        if moving_up:
            dy = -self.speed
        if moving_down:
            dy = self.speed

        # Update Rectange position
        self.rect.x += dx
        self.rect.y += dy

    # Drawing the Soldier to the screen
    def draw(self):
        screen.blit(self.image, self.rect)
        

class Map(pygame.sprite.Sprite):
    def __init__(self, img="img/map.png", x=1280/2, scale=2.8, y=720/2, speed=3):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load(img)
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self):
        screen.blit(self.image, self.rect)
        

# Creating the Player
player = Soldier()

mapeu = Map()

# Game Loop
run = True
while run:

    # Lock Framerate
    clock.tick(FPS)

    # Making the backgroung Dark
    screen.fill((0, 0, 0))
    
    mapeu.draw()

    # Drawing the player on the screen
    player.draw()
    
    # Moving the player
    player.move(moving_left, moving_right, moving_up, moving_down)


    # Event Handler
    for event in pygame.event.get():
        
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
            
            # Escape escape the game
            if event.key == pygame.K_ESCAPE:
                run = False
        # The cross quit the Game
        if event.type == pygame.QUIT:
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
    
    pygame.display.update()

pygame.quit()