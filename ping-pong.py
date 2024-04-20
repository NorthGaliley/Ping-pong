from pygame import *
from random import randint
mixer.init()
font.init()
window = display.set_mode((700, 500))
display.set_caption('CS 5')
background = transform.scale(image.load('background'), (700, 500))
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
    def updete(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_W] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_S] and self.rect.y < 495:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def update(self):
        global miachik
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.x = randint(0, 620)
            self.rect.y = 0

clock = time.Clock()
FPS = 60    
game = True
while game:       
    clock.tick(FPS)
    display.update()