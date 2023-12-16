# lab10 task2
# wih scores

import pygame 
from pygame.locals import *
import random, time, sys    
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
SPEED = 5

car_score = 0
coin_score = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("details/AnimatedStreet.png")
bgmusic = pygame.mixer.Sound("details/background.wav")
bgmusic.play()

DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Car game")
DISPLAYSURF.fill(WHITE)

FrPS = pygame.time.Clock()

ci= 0
cs = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("details/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)

    def move(self):
        global car_score
        self.rect.move_ip(0, SPEED) # 5 = speed
        if (self.rect.bottom > 600):
            car_score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    
    


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
    

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("details/Coin.jpg"), (25,25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(32, 468), -31)
        self.a = random.randint(600, 1000)

    def move(self):
        global coin_score
        self.rect.move_ip(0,10)
        if self.rect.top > 600:
            self.rect.top = -62
            self.rect.center = (random.randint(32, 468), -31)
        elif self.rect.colliderect(p):
            coin_score += 1
            pygame.mixer.Sound("details/coin2.mp3").play()
            self.rect.top = -62
            self.rect.center = (random.randint(32, 468), -31)


p = Player()
e = Enemy()
c = Coins()

enemies = pygame.sprite.Group()
enemies.add(e)
all_sprites = pygame.sprite.Group()
all_sprites.add(p)
all_sprites.add(e)
coins = pygame.sprite.Group()
coins.add(c)

INC_SPEED = pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED, 500)


bgy = 0
c_y = 0
c_x = 0
y = 0


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED +=0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,bgy))
    DISPLAYSURF.blit(background, (0,bgy-600))

    if ci == 23:
        ci = 0
    else:
        ci += 1

    if bgy < 600:
        bgy += 7
    else: 
        bgy = 0
    

    car_scores = font_small.render(f"Score: {str(car_score)}", True, BLACK)
    coin_scores = font_small.render(f"Coins: {str(coin_score)}", True, BLACK)
    DISPLAYSURF.blit(car_scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (300, 10))


    for ent in all_sprites:  
        DISPLAYSURF.blit(ent.image, ent.rect)
        ent.move()

    for ent in coins:
        DISPLAYSURF.blit(ent.image, ent.rect)
        ent.move()
        


    if pygame.sprite.spritecollideany(p, enemies):
        bgmusic.stop()
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


    pygame.display.update()
    FrPS.tick(60)