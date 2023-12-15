# lab10 task3

# Importing pygame and others
import pygame 
from pygame.locals import *
import random, time, sys    

# Initilize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SPEED = 5

# Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("details/AnimatedStreet.png")

# Create pygame window
DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Car game")
DISPLAYSURF.fill(WHITE)

# Setting up FPS
FrPS = pygame.time.Clock()


# Create class for enemy car
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("details/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)

    def move(self):
        self.rect.move_ip(0, SPEED) # 5 = speed
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    
    # def draw(self, sc):
    #     sc.blit(self.image, self.rect)


# # Create class for player car
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("details/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pr_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pr_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400:
            if pr_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    
    # def draw(self, sc):
    #     sc.blit(self.image, self.rect)

p = Player()
e = Enemy()


# Create sprite group
enemies = pygame.sprite.Group()
enemies.add(e)
all_sprites = pygame.sprite.Group()
all_sprites.add(p)
all_sprites.add(e)

# add new event
INC_SPEED = pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED, 1000)


# Game loop begins
while True:
    # For exit the pygame window
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED +=2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    DISPLAYSURF.blit(background, (0,0))

    # Moves All sprites
    for ent in all_sprites:  
        DISPLAYSURF.blit(ent.image, ent.rect)
        ent.move()


    if pygame.sprite.spritecollideany(p, enemies):
        pygame.mixer.Sound('details/crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(font.render("Game Over", True, BLACK), (30,250))

        pygame.display.update()
        for ent in all_sprites:
            ent.kill()
        
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # p.update()
    # e.move()

    # screen.fill(WHITE)
    
    
    # p.draw(screen)
    # e.draw(screen)
    
    # Update display after all changings
    pygame.display.update()
    FrPS.tick(60)