from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
   
 
    def __init__(self, image_file, x, y, speed, size_x, size_y):
        super().__init__()  
        self.image = transform.scale(
            image.load(image_file), (size_x, size_y) )  
        self.speed = speed  
        self.rect = (self.image.get_rect())  
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    
    def update_r(self):
        
        keys = key.get_pressed()

        
        if keys[K_UP] and self.rect.y > 5:
            
            self.rect.y -= self.speed

        
        if keys[K_DOWN] and self.rect.y < height - 80:
           
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed









width = 600
height = 500
back  = (150, 30, 240)

window = display.set_mode((width, height))
window.fill(back)




racket1 =Player('raketka1.png', 30, 200, 4, 50, 150)
racket2 = Player('raketka2.png', 520, 200, 4, 50, 150)
ball = GameSprite('myachik.png', 200, 200 , 4, 50, 50)



speedx = 3
speedy = 3



finish = False 

game = True  





font.init()
font1 = font.SysFont("Arial", 36)
font2 = font.SysFont("Arial", 80)
lose1 = font2.render("Player 1 lose", True, (180 , 0, 0))
lose2 = font2.render("player 2 loseeeeeeee", True, (180, 0, 0))


clock = time.Clock()
FPS = 60








while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False  
     

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speedx
        ball.rect.y += speedy

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect( racket2, ball):
            speedx *= -1
            speedy *= -1

        if ball.rect.y > height - 50 or ball.rect.y < 0:
            speedy *= -1
        
        if ball.rect.x > width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

    racket1.reset()
    racket2.reset()
    ball.reset()



       


    
    display.update()
    clock.tick(FPS)