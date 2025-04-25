from pygame import *
from random import *
window = display.set_mode((700, 500))
display.set_caption('ШУТЕР')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

clock = time.Clock()
FPS = 60
x1 = 120
y1=120
x2 = 300     
y2=300
speed = 10
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
finish = False
lost = 0
score = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        global score
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80, 700-80)
            lost = lost +1
            score = score - 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()




font.init()
font1 = font.SysFont('Arial', 36)

class Player(GameSprite):
    def update(self):
          keys_pressed = key.get_pressed()
          if keys_pressed[K_LEFT]and self.rect.x > 5:
            self.rect.x -= speed
          if keys_pressed[K_RIGHT] and self.rect.x < 625:
            self.rect.x += speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -20)
        bullets.add(bullet)
          

player = Player('rocket.png', 350, 430, 65, 65, 30)
monsters = sprite.Group()
monsters.add(Enemy('ufo.png', randint(80, 700-80), -15, 65, 65, 2 ))
monsters.add(Enemy('ufo.png', randint(80, 700-80), 10, 65, 65, 2 ))
monsters.add(Enemy('ufo.png', randint(80, 700-80), -30, 65, 65, 2 ))
monsters.add(Enemy('ufo.png', randint(80, 700-80), -20, 65, 65, 2 ))
monsters.add(Enemy('ufo.png', randint(80, 700-80), 0, 65, 65, 2 ))
bullets = sprite.Group()
fire = mixer.Sound('fire.ogg')
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type  == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                fire.play()
      
    
    if not finish:    
        window.blit(background,(0, 0))
        text_lose = font1.render(
                    'Пропущено:' + str(lost), 1, (255, 255, 255)
                )

        if score > 130:
            win = font1.render("ПОООБЕДА" , 1, (255, 255, 123))
            finish = True
            window.blit(win, (240, 200))
        window.blit(text_lose, (10, 20))
        text_win = font1.render(
                    'Сбито:' + str(score), 1, (255, 255, 255)
                )
        window.blit(text_win, (10, 44))
        if lost >= 16:
            fail = font1.render("ПОРОЖЕНИЯЯЯЯ", 1, (145, 109, 167))
            finish = True
            window.blit(fail, (240, 200))


        sprites_list = sprite.groupcollide(
            monsters, bullets, True, True
        )
        for sm in sprites_list:
            score+=1
            monsters.add(Enemy('ufo.png', randint(80, 700-80), -15, 65, 65, 2 ))

            
        player.update()
        monsters.draw(window)
        monsters.update()
        bullets.draw(window)
        bullets.update()
        player.reset()



        clock.tick(FPS)
        display.update()
    else:
        finish = False 
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(5000)
        monsters.add(Enemy('ufo.png', randint(80, 700-80), -15, 65, 65, 2 ))
        monsters.add(Enemy('ufo.png', randint(80, 700-80), 10, 65, 65, 2 ))
        monsters.add(Enemy('ufo.png', randint(80, 700-80), -30, 65, 65, 2 ))
        monsters.add(Enemy('ufo.png', randint(80, 700-80), -20, 65, 65, 2 ))
        monsters.add(Enemy('ufo.png', randint(80, 700-80), 0, 65, 65, 2 ))