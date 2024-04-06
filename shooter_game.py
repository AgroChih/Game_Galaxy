#ХЕЛОУ ВОРЛД!!
from pygame import *
from random import randint
from time import time as timer
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height)) 
display.set_caption('Шутер')
galaxy = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))
clock = time.Clock()
#ТОШЕ КЛАСФССФСФ 33333333333333333333333333333 
class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image1), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 65:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',  self.rect.centerx, self.rect.top, 20, 25, -15)
        bullets.add(bullet)
lost = 0 #проигрыш выигрыш
score = 0

#КЛАССЫЫЫ!!!!!!!!!!!!!!!!!!!!!
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed 
        global lost
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(0 ,win_width - 65)
            lost += 1
class Asteroud(GameSprite):
    def update(self):
        self.rect.y += self.speed 
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(0, win_width - 65)
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()

#создание фиговин!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(1, 6):
    monster =  Enemy('ufo.png',  randint(80 ,win_width - 80), -40, 80, 50, randint(1, 3))
    monsters.add(monster)
for i in range(1, 4):
    asteroid =  Asteroud('asteroid.png',  randint(80 ,win_width - 80), -40, 50, 40, randint(1, 3))
    asteroids.add(asteroid)

font.init()
font1 = font.Font(None, 36) #надписи156327163871837918372684268748375928943452
font2  = font.Font(None, 36) #0310904932783785932593532895329
font3 = font.Font(None, 36) #49763749769380694-06-8436468

#корабль и музыка
ship = Player('rocket.png', win_width // 2 - 32, win_height - 100, 80, 100, 10) 
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
FPS = 60

num_fire = 0 #пулииииииииииииииииииииииииииииииииии
rel_time = 0 #время
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN', True, (255,215, 0))
lose = font.render('YOU LOSE', True, (180,0, 0))
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE: # перезарядка11111111111111
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    ship.fire()
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True
    display.update()
    clock.tick(FPS)
    if not finish:
        window.blit(galaxy, (0, 0))
        ship.reset()
        ship.update()
        monsters.draw(window)
        monsters.update()
        asteroids.draw(window)
        asteroids.update()
        bullets.update()
        bullets.draw(window)
        text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        text_score = font1.render('Счёт:' + str(score), 1, (255, 255, 255))
        window.blit(text_lose, (10,50))
        window.blit(text_score, (10,20))
        if rel_time == True: #       перезарядка22222222222222222222222
            now_time = timer()
            if now_time - last_time < 3:
                wait = font3.render('Wait, please..', True, (180, 0, 0))
                window.blit(wait, (260, 460))
            else:
                num_fire = 0
                rel_time = False
                #проиграшфшшф 777777777777777777777777
        if  sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False) or lost == 5:
            finish = True
            window.blit(lose, (200, 200))
        sprite_list = sprite.groupcollide(monsters, bullets, True, False)
        sprite_list1 = sprite.groupcollide(asteroids, bullets, False, True)
        for c in sprite_list: #подсчетттмтмтмтмтмтмттм
            score += 1
            monster =  Enemy('ufo.png',  randint(80 ,win_width - 80), -40, 80, 50, randint(1, 3))
            monsters.add(monster)
        if score == 16: #выыигрышышышшышшышышышшышшшышы
            finish = True
            window.blit(win, (200,200))
        