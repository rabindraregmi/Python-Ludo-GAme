import pygame,random,time
from pygame.locals import *


pygame.init()
dice_size = 80
display_width=600
white=(255,255,255)
black=(0,0,0)
grey=(32,32,32)
radius=20
ss=pygame.image.load("dice.png")
dienum=[(0,4),(4,4),(0,8),(0,0),(12,4),(8,4)]
dienumdict={(0,4):1,(4,4):2,(0,8):3,(0,0):4,(12,4):5,(8,4):6}
background=pygame.image.load('Snake.jpg')
gameDisplay=pygame.display.set_mode((600,600))

def dice_roll():
    for i in range(0,15):
        gameDisplay.fill(white)
        gameDisplay.blit(background, [0, 0])
        pygame.draw.circle(gameDisplay, black, path[position], radius)
        image=ss.subsurface(spritesheet(random.randrange(0,15),random.randrange(1,8)))
        pygame.time.delay(140)
        gameDisplay.blit(image,[random.randrange(380,420),random.randrange(380,420)])
        pygame.display.update()
def gupdate(position, path):
        print position, path[position]
        pygame.draw.circle(gameDisplay, black, path[position],radius)
        #pygame.draw.circle(gameDisplay, black, path[position],radius)
        #pygame.draw.circle(gameDisplay, white, path[position - 1],radius + 5)
        pygame.display.update()
        print position, path[position]
def spritesheet(x, y):
    size = (16, 9)
    dimx = 736.0 / 16.0
    dimy = 414.0 / 9.0

    return (x * dimx, y * dimy, dimx, dimy)
def draw_image():
    gameDisplay.fill((255,255,255))
    gameDisplay.blit(background,(0,0))
    gameDisplay.blit(image, [400, 400])
    pygame.display.update()
def draw(position):
        print position
        #pygame.draw.circle(gameDisplay, black, position,radius)
        #pygame.draw.circle(gameDisplay,(255,255,255), position,radius)



path_sx=[]
path_sy=[]
starting_sx=30
starting_sy=570
x=1
for i in range(1,101):
    if(i>1 and i<=10) or (i>21 and i<=30) or (i>41 and i<=50) or (i>61 and i<=70) or (i>81 and i<=90):
        starting_sx+=60

    if (i > 11 and i <= 20) or (i > 31 and i <= 40) or (i > 51 and i <= 60) or (i > 71 and i <= 80) or (i > 91 and i <= 100):
        starting_sx-=60

    if i==11 or i==21 or i==31 or i==41 or i==51 or i==61 or i==71 or i==81 or i==91:
        starting_sy-=60
    path_sx.append(starting_sx)
    path_sy.append(starting_sy)
path = [(x1, y1) for x1, y1 in zip(path_sx, path_sy)]



gameDisplay.fill((0,0,0))
gameDisplay.blit(background,[0,0])
image=ss.subsurface(spritesheet(0,4))
gameDisplay.blit(image,[400,400])
pygame.display.update()
position=0
for i in range (0,100):
    print i,path[i]
print path
while True:
  for event in pygame.event.get():
      if event.type==pygame.QUIT:
          pygame.quit()
      if event.type==pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          dice_roll()
          index_get = random.choice(dienum)
          num = dienumdict[index_get]
          image = ss.subsurface(spritesheet(index_get[0], index_get[1]))
          print "Num=",num
          for _ in range (1,num+1):
              gameDisplay.blit(background, [0, 0])
              gameDisplay.blit(image, [400, 400])
              draw(path[position])
              position+=1
              gupdate(position,path)
              pygame.time.delay(120)
          pygame.display.update()
quit()