import pygame,random,sys
from pygame.locals import *
from getPoints import get_points
pygame.init()
dice_size = 80
display_width=600
white=(255,255,255)
black=(0,0,0)
grey=(32,32,32)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,128)
yellow=(255,255,0)
radius=20
ss=pygame.image.load("Dice\dice.png")
dienum=[(0,4),(4,4),(0,8),(0,0),(12,4),(8,4)]
dienumdict={(0,4):1,(4,4):2,(0,8):3,(0,0):4,(12,4):5,(8,4):6}
background=pygame.image.load("Board\Board2.jpg")

class Gatti(object):
    radius = 10

    def __init__(self, color, pos, no):
        self.color = color
        self.pos = pos
        self.no = no


    def update(self, gameDisplay,position, path):
        pygame.draw.circle(gameDisplay, black, path[position], self.radius + 5)
        pygame.draw.circle(gameDisplay, self.color, path[position], self.radius)
        #pygame.draw.circle(gameDisplay, white, path[position - 1], self.radius + 5)
        pygame.display.update()
        print position, path[position]

    def draw(self, gameDisplay, position):
        pygame.draw.circle(gameDisplay, black, position, self.radius + 5)
        pygame.draw.circle(gameDisplay, self.color, position, self.radius)


def dice_roll(gameDisplay):
    for i in range(0,15):
        gameDisplay.fill(white)
        gameDisplay.blit(background, [0, 0])
        red_gatti.draw(gameDisplay,path[position[0]])
        yellow_gatti.draw(gameDisplay,path[position[1]])
        blue_gatti.draw(gameDisplay,path[position[2]])
        green_gatti.draw(gameDisplay,path[position[3]])

        image=ss.subsurface(spritesheet(random.randrange(0,15),random.randrange(1,8)))
        #pygame.time.delay(140)
        gameDisplay.blit(image,[random.randrange(380,420),random.randrange(380,420)])
        pygame.display.update()
ladders={1:38,4:14,9:31,21:42,28:84,51:67,80:99,72:91}
snakes={17:7,54:34,62:19,64:60,87:36,98:79,93:73,95:75}
red_gatti=Gatti(red,[1000,1000],1)
blue_gatti=Gatti(blue,[1000,1000],1)
yellow_gatti=Gatti(yellow,[1000,1000],1)
green_gatti=Gatti(green,[1000,1000],1)
def checkladder(position_index):
    num=1
    try:
        num=ladders[position_index]
        return num
    except:
        return 0
def checksnakes(position_index):
        try:
            num=snakes[position_index]
            return num
        except:
            return 0

def spritesheet(x, y):
    size = (16, 9)
    dimx = 736.0 / 16.0
    dimy = 414.0 / 9.0
    return (x * dimx, y * dimy, dimx, dimy)
def draw(gameDisplay,image):
    gameDisplay.blit(background, [0, 0])
    gameDisplay.blit(image, [400, 400])
    red_gatti.draw(gameDisplay, path[position[0]])
    yellow_gatti.draw(gameDisplay, path[position[1]])
    blue_gatti.draw(gameDisplay, path[position[2]])
    green_gatti.draw(gameDisplay, path[position[3]])



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
path = [(1000,1000)]+[(x1, y1) for x1, y1 in zip(path_sx, path_sy)]
path=path[:100]
gattiDict={0:red_gatti,1:yellow_gatti,2:blue_gatti,3:green_gatti}
position = [0, 0, 0, 0]



def main():
    gameDisplay=pygame.display.set_mode((600,600))
    gameDisplay.fill((0,0,0))
    gameDisplay.blit(background,[0,0])
    image = ss.subsurface(spritesheet(0, 4))
    gameDisplay.blit(image,[400,400])
    pygame.display.update()
    turn=0
    while True:
      for event in pygame.event.get():

          if event.type==pygame.QUIT:
              pygame.display.quit()
              sys.exit()


          if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:




              #dice roll
              dice_roll(gameDisplay)
              index_get = random.choice(dienum)
              num = dienumdict[index_get]
              image = ss.subsurface(spritesheet(index_get[0], index_get[1]))


              #Gatti movement
              for _ in range (1,num+1):
                  draw(gameDisplay, image)
                  position[turn % 4] += 1
                  pygame.time.delay(100)
                  draw(gameDisplay, image)
                  gattiDict[turn % 4].update(gameDisplay, position[turn % 4], path)
                  draw(gameDisplay, image)




              #Ladder check and movement
              num=checkladder(position[turn%4])
              if num!=0:
                  initial = position[turn % 4]
                  origin={'x':path[position[turn%4]][0] ,'y':path[position[turn%4]][1]}
                  target = {'x': path[ladders[position[turn % 4]]][0],
                            'y': path[ladders[position[turn % 4]]][1]}
                  movementCoords=get_points(origin,target)
                  i=0
                  position[turn % 4] = 0
                  for _ in movementCoords:
                      draw(gameDisplay,image)
                      gattiDict[turn%4].update(gameDisplay,i,movementCoords)
                      i+=1
                      pygame.time.delay(20)
                  position[turn%4]=ladders[initial]


              #Snake check and movement
              num2 = checksnakes(position[turn % 4])
              if num2 != 0:
                  initial=position[turn%4]
                  origin = {'x': path[position[turn % 4]][0], 'y': path[position[turn % 4]][1]}
                  target = {'x': path[snakes[position[turn % 4]]][0],
                            'y': path[snakes[position[turn % 4]]][1]}
                  movementCoords = get_points(origin, target)
                  i = 0
                  position[turn % 4] = 0
                  for _ in movementCoords:
                      draw(gameDisplay, image)
                      gattiDict[turn % 4].update(gameDisplay, i, movementCoords)
                      i += 1
                      pygame.time.delay(10)
                  position[turn % 4] = snakes[initial]



            draw(gameDisplay, image)
            pygame.time.delay(5)
            turn+=1
            pygame.display.update()


