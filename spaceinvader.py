import pygame
import random
import math
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((700,700))
#Title and logo
pygame.display.set_caption('KILL AS MANY')

icon=pygame.image.load('logo.png')
pygame.display.set_icon(icon)
background=pygame.image.load('bimg.png')
#player
hero=pygame.image.load('hero.png')
playerX=320
playerY=550
# #sound

# mixer.music.load('bsound.M4A')
# mixer.music.play(-1)

#enemy
enemy=[]
enemyY=[]
enemyX=[]
enemy_Xchange=[]
num_enemy=6
for i in range(num_enemy):
    enemy.append(pygame.image.load('alien.png'))
    enemyY.append(random.randint(30,120))
    enemyX.append(random.randint(0,700))
    enemy_Xchange.append(0.3)
#bullet
bullet=pygame.image.load('bullet.png')
bulletX=0
bulletY=550
bulletX_change=0
bulletY_change=0.5
bullet1_state='ready'
#text on screen
score=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
#hero function 
def hero_function(x,y):
    screen.blit(hero,(x,y))
#enemy function
def enemy_function(X,Y,i):
    screen.blit(enemy[i],(X,Y))
#bullet function
def bullet_function(x,y):
    global bullet1_state
    bullet1_state='fire'
    screen.blit(bullet,(x+33,y+45))
#collision

def collision(enemyX,enemyY,bulletX,bulletY):

    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<25:
        return True
    else:
        return False
#showing text function
def score_function(x,y):
    score_screen=font.render("SCORE :"+str(score),True,(255,255,255))
    screen.blit(score_screen,(x,y))
#game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
        
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bulletX=playerX
        bulletY=550
        bullet_function(bulletX,bulletY)

    screen.fill((0,0,0))
#bullet movement
    if bullet1_state == 'fire':
        bulletY-=bulletY_change
        bullet_function(bulletX,bulletY)
    if bulletY<=0:
        bullet_state='ready'
    
#player movement
    if keys[pygame.K_LEFT]:
        playerX-=0.5
    if keys[pygame.K_RIGHT]:
        playerX+=0.5
    if playerX<=0:
        playerX=0
    if playerX>=620:
        playerX=620

    
    hero_function(playerX,playerY)

#enemy movement
    for i in range(num_enemy):
        
        enemyX[i]+=enemy_Xchange[i]
        if enemyX[i]<=0:
            enemy_Xchange[i]=0.3
            enemyY[i]+=40
        if enemyX[i]>=668:
            enemy_Xchange[i]=-0.3
            enemyY[i]+=40
        enemy_function(enemyX[i],enemyY[i],i)
#collision    
        iscollision=collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if iscollision:
            bullet1_state='ready'
            score+=1
            enemyX[i]=random.randint(0,700)
            enemyY[i]=random.randint(30,120)
    #score
    score_function(textX,textY)
    # screen.blit(background,(0,0))
    pygame.display.update()
