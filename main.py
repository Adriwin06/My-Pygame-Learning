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
        self.pos = 0

    def move(self, moving_left, moving_right, moving_up, moving_down):
        # reset movement variables
        dx = 0
        dy = 0

        self.hitbox = Hitbox(self.rect.x, self.rect.y, self.image)
        for entity in entity_list:
                if (not entity==self) and (self.hitbox.collide(entity)):
                    if self.pos == "left":
                        self.rect.x += self.speed
                    if self.pos == "right":
                        self.rect.x -= self.speed
                    if self.pos == "up":
                        self.rect.y += self.speed
                    if self.pos == "down":
                        self.rect.y -= self.speed
                    break
        self.hitbox = Hitbox(self.rect.x, self.rect.y, self.image)

        # Assign movement variable if moving
        if moving_left:
            for entity in entity_list:
                if (not entity==self) and (self.hitbox.collide(entity)):
                    self.pos = "left"
                    break
            dx += -self.speed
        if moving_right:
            for entity in entity_list:
                if (not entity==self) and (self.hitbox.collide(entity)):
                    self.pos = "right"
                    break
            dx += self.speed
        if moving_up:
            for entity in entity_list:
                if (not entity==self) and (self.hitbox.collide(entity)):
                    self.pos = "up"
                    break
            dy += -self.speed
        if moving_down:
            for entity in entity_list:
                if (not entity==self) and (self.hitbox.collide(entity)):
                    self.pos = "down"
                    break
            dy += self.speed

        # Update Rectangle position
        self.rect.x += dx
        self.rect.y += dy

        self.hitbox = Hitbox(self.rect.x, self.rect.y, self.image)

    # Drawing the Soldier to the screen
    def draw(self):
        screen.blit(self.image, self.rect)


# Same as Soldier class for now, for testing purpose
class Entity(pygame.sprite.Sprite):
    def __init__(self, x= 400, y=100, scale=0.1, speed=3):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load('img/player/idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hitbox = Hitbox(x, y, self.image)

    def move(self, moving_left, moving_right, moving_up, moving_down):
        # reset movement variables
        dx = 0
        dy = 0


        # Assign movement variable if moving
        if moving_left:
            for entity in entity_list:
                if (not entity==self) and (self.hitbox.collide(entity)):
                    dx = self.speed*2.5
                    break
            dx += -self.speed
        if moving_right:
            for entity in entity_list:
                if (not entity==self) and (self.hitbox.collide(entity)):
                    dx = -self.speed*2.5
                    break
            dx += self.speed
        if moving_up:
            for entity in entity_list:
                if (not entity==self) and (self.hitbox.collide(entity)):
                    dy = self.speed*2.5
                    break
            dy += -self.speed
        if moving_down:
            for entity in entity_list:
                if (not entity==self) and (self.hitbox.collide(entity)):
                    dy = -self.speed*2.5
                    break
            dy += self.speed

        # Update Rectange position
        self.rect.x += dx
        self.rect.y += dy

        self.hitbox = Hitbox(self.rect.x, self.rect.y, self.image)

    # Drawing the Entity to the screen
    def draw(self):
        screen.blit(self.image, self.rect)


# Defining the Map class
class Map(pygame.sprite.Sprite):
    def __init__(self, img="img/map.png", x=1280/2, scale=2.8, y=720/2, speed=3):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load(img)
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # Drawing map
    def draw(self):
        screen.blit(self.image, self.rect)


# Defining the Hitbox class ; x is x position of the centre of the hitbox, same for y, and W is the width and H the height
class Hitbox:
    def __init__(self, x, y, img):
        self.rect = img.get_rect()
        self.rect.center = (x+self.rect.width/2, y+self.rect.height/2)

    def collide(self, other):
        # assert isinstance(other, Hitbox) or isinstance(other, Soldier), f"Can't collide Hitbox with another type than Hitbox or Soldier : attempted to collide {other}"
        return self.rect.colliderect(other.rect)


# Creating the Player
player = Soldier()

monster = Entity()

entity_list = [player, monster]

map1 = Map()

# Game Loop
run = True
while run:

    # Lock Framerate
    clock.tick(FPS)

    # Making the backgroung Dark
    screen.fill((0, 0, 0))
    
    # Drawing the map on the screen
    map1.draw()

    # Drawing the player on the screen
    player.draw()
    
    monster.draw()
    
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