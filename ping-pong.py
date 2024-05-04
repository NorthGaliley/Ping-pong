from pygame import *
from random import randint
mixer.init()
font.init()
window = display.set_mode((700, 500))
display.set_caption('CS 5')
background = transform.scale(image.load('background.png'), (700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 245:
            self.rect.y += self.speed

    def updateL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 245:
            self.rect.y += self.speed
# class Enemy(GameSprite):
#     def update(self):
#         global miachik
#         self.rect.y += self.speed
#         if self.rect.y >= 500:
#             self.rect.x = randint(0, 620)
#             self.rect.y = 0
class Ball (GameSprite):
    def update(self):
        global speed_y 
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 500-50 or ball.rect.y < 0:
                speed_y *= -1

font2 = font.SysFont("Arial", 70)

lost = font2.render('Дима ЛОХ', True, (255, 0, 0))
win = font2.render('вау! Айфон', True, (255, 0, 0))

heroR = Player('raketka(right).png', 5, 628, 120, 70, 250)
heroL = Player('raketka(left).png', 5, 2, 120, 70, 250)
ball = Ball('miachik.png', 15, 225, 325, 50, 50)
clock = time.Clock()
FPS = 60    
game = True

speed_x = 3
speed_y = 3

while game: 
    window.blit(background,(0,0)) 
    heroR.updateR()
    heroR.reset()
    heroL.updateL()
    heroL.reset()

    if ball.rect.x >= 700:
        window.blit(lost, (200, 250))
    if ball.rect.x <= 0:
        window.blit(win, (200, 250))
        

    if sprite.collide_rect(heroR, ball) or sprite.collide_rect(heroL, ball):
        speed_x *= -1

    ball.update()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()
