from pygame import *
'''שיעורי חובה'''

# מחלקת האב עבור הספרייטים
class GameSprite(sprite.Sprite):
    #בנאי מחלקה
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height): # הוסף שני פרמטרים נוספים בעת יצירת וקבע את גודל המלבן לתמונה בעצמך
        super().__init__()
 
        # כל ספרייט חייב לאחסן מאפיין תמונה - תמונה
        self.image = transform.scale(image.load(player_image), (wight, height)) # ביחד 55.55 - פרמטרים
        self.speed = player_speed
 
        # כל ספרייט חייב לאחסן את המאפיין rect - המלבן שבו הוא רשום
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#כיתת ילדים עבור ספרייט שחקן (נשלט על ידי חיצים)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

# סצנת המשחק
back = (200, 255, 255) # רקע
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
# דגלים למצבי המשחק
game = True
finish = False
clock = time.Clock()
FPS = 60
 
# יצירת כדור ומחבטים  
racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)
 
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
 
speed_x = 3
speed_y = 3
 
while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:
       window.fill(back)
       racket1.update_l()
       racket2.update_r()
       ball.rect.x += speed_x
       ball.rect.y += speed_y
 
       if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
           speed_x *= -1
           speed_y *= 1
      
       # אם הכדור הגיע לקצה המסך, שנה כיוון
       if ball.rect.y > win_height-50 or ball.rect.y < 0:
           speed_y *= -1
 
       # אם הכדור הגיע אל מאחורי המחבט, הצג מצב הפסד עבור שחקן 1
       if ball.rect.x < 0:
           finish = True
           window.blit(lose1, (200, 200))
           game_over = True
 
       # אם הכדור הגיע אל מאחורי המחבט, הצג מצב הפסד עבור שחקן 2
       if ball.rect.x > win_width:
           finish = True
           window.blit(lose2, (200, 200))
           game_over = True
 
       racket1.reset()
       racket2.reset()
       ball.reset()
 
   display.update()
   clock.tick(FPS)
