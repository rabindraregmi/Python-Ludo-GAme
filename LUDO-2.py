import pygame,time,random
pygame.init()


def uddrawcircle(centre1,centre2,radius1):
    pygame.draw.circle(gameDisplay,white,[centre1,centre2],radius1)
with open("Board.txt","r+") as file:
    board = file.readlines()
n=int(raw_input())
green = (0,255,0)
blue = (0,0,128)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)
grey=(32,32,32)
display_height=600
display_width=600
big_rectangle=240
hole_radius=30
gameDisplay=pygame.display.set_mode((display_width,display_height))
clock=pygame.time.Clock()
pygame.display.update()
pygame.display.set_caption("LUDO FOR EVERYONE")
gameExit=False


#Code for dice
dice_size=80
x=display_width/2-dice_size/2
y=display_width/2-dice_size/2
dot_size=dice_size//10
mid=dice_size//2
left=top=dice_size//4
right=bottom=dice_size-left

def dice_roll(num):
    pygame.draw.rect(gameDisplay,grey,(x-3,y-3,dice_size+6,dice_size+6))
    pygame.draw.rect(gameDisplay,black,(x-3,y-3,dice_size+6,dice_size+6))
    if num==1:
        pygame.draw.circle(gameDisplay,white,(x+mid,y+mid),dot_size)
    else:
        if num==2 or num==3:
            pygame.draw.circle(gameDisplay, white, (x + right, y + mid), dot_size)
            pygame.draw.circle(gameDisplay, white, (x + left, y + mid), dot_size)
            if num==3:
                pygame.draw.circle(gameDisplay, white, (x + mid, y + mid), dot_size)
        else:
            pygame.draw.circle(gameDisplay, white, (x + right, y + top), dot_size)
            pygame.draw.circle(gameDisplay, white, (x + left, y + top), dot_size)
            pygame.draw.circle(gameDisplay, white, (x + left, y + bottom), dot_size)
            pygame.draw.circle(gameDisplay, white, (x + right, y + bottom), dot_size)
            if num==5:
                pygame.draw.circle(gameDisplay, white, (x + mid, y + mid), dot_size)
            elif num==6:
                pygame.draw.circle(gameDisplay, white, (x + mid, y + top), dot_size)
                pygame.draw.circle(gameDisplay, white, (x + mid, y + bottom), dot_size)

#Code for layout
gameDisplay.fill(white)

#RED
pygame.draw.rect(gameDisplay,red,[0,0,big_rectangle,big_rectangle])
pygame.draw.polygon(gameDisplay, red,[[big_rectangle, big_rectangle], [big_rectangle,display_height-big_rectangle],[display_width / 2, display_height / 2]])
pygame.draw.circle(gameDisplay, white, [big_rectangle / 4, big_rectangle / 4], hole_radius)
pygame.draw.circle(gameDisplay, white, [big_rectangle - big_rectangle / 4, big_rectangle / 4], hole_radius)
pygame.draw.circle(gameDisplay, white, [big_rectangle / 4, big_rectangle - big_rectangle / 4], hole_radius)
pygame.draw.circle(gameDisplay, white, [big_rectangle - big_rectangle / 4, big_rectangle - big_rectangle / 4],hole_radius)

#GREEN
pygame.draw.rect(gameDisplay, green, [0,display_height-big_rectangle,big_rectangle,big_rectangle])
pygame.draw.polygon(gameDisplay,green,[[big_rectangle,display_height-big_rectangle],[display_width-big_rectangle,display_height-big_rectangle],[display_width/2,display_height/2]])
uddrawcircle(big_rectangle / 4, display_height - big_rectangle / 4, hole_radius)
uddrawcircle(big_rectangle / 4, display_height - 3 * big_rectangle / 4, hole_radius)
uddrawcircle(3 * big_rectangle / 4, display_height - big_rectangle / 4, hole_radius)
uddrawcircle(3 * big_rectangle / 4, display_height - 3 * big_rectangle / 4, hole_radius)

#YELLOW
pygame.draw.rect(gameDisplay, yellow, [display_width-big_rectangle, 0,big_rectangle,big_rectangle])
pygame.draw.polygon(gameDisplay,yellow,[[big_rectangle,big_rectangle],[display_width-big_rectangle,big_rectangle],[display_width/2,display_height/2]])
pygame.draw.circle(gameDisplay, white, [display_width - 3 * big_rectangle / 4, big_rectangle / 4], hole_radius)
pygame.draw.circle(gameDisplay, white, [display_width - big_rectangle / 4, big_rectangle / 4], hole_radius)
pygame.draw.circle(gameDisplay, white, [display_width - big_rectangle / 4, 3 * big_rectangle / 4], hole_radius)
uddrawcircle(display_width - 3 * big_rectangle / 4, 3 * big_rectangle / 4, hole_radius)

#BLUE
pygame.draw.rect(gameDisplay, blue, [display_width-big_rectangle,display_height-big_rectangle,big_rectangle,big_rectangle])
pygame.draw.polygon(gameDisplay,blue,[[display_width-big_rectangle,display_height-big_rectangle],[display_width-big_rectangle,big_rectangle],[display_width/2,display_height/2]])
uddrawcircle(display_width - big_rectangle / 4, display_height - big_rectangle / 4, hole_radius)
uddrawcircle(display_width - 3 * big_rectangle / 4, display_height - big_rectangle / 4, hole_radius)
uddrawcircle(display_width - 3 * big_rectangle / 4, display_height - 3 * big_rectangle / 4, hole_radius)
uddrawcircle(display_width - big_rectangle / 4, display_height - 3 * big_rectangle / 4, hole_radius)

#pygame.draw.rect(gameDisplay,white,[big_rectangle,big_rectangle,display_width-2*big_rectangle,display_height-2*big_rectangle])
pygame.draw.line(gameDisplay,black,[0,0],[display_width,0])


#INDIVIDUAL BOX COLOR
pygame.draw.rect(gameDisplay, yellow, [big_rectangle + ((display_width - 2 * big_rectangle) / 3), big_rectangle/6,(display_width - 2 * big_rectangle) / 3, big_rectangle])
pygame.draw.rect(gameDisplay, green, [big_rectangle + ((display_width - 2 * big_rectangle) / 3), display_height - big_rectangle,(display_width - 2 * big_rectangle) / 3, big_rectangle-big_rectangle/6])
pygame.draw.rect(gameDisplay,red,[big_rectangle/6,big_rectangle+(display_height-2*big_rectangle)/3,big_rectangle,(display_height-2*big_rectangle)/3])
pygame.draw.rect(gameDisplay,blue,[display_width-big_rectangle,big_rectangle+(display_height-2*big_rectangle)/3,big_rectangle-big_rectangle/6,(display_height-2*big_rectangle)/3])
pygame.draw.rect(gameDisplay,red,[big_rectangle/6,big_rectangle,big_rectangle/6,big_rectangle/6])
pygame.draw.rect(gameDisplay,blue,[display_width-2*big_rectangle/6,big_rectangle+big_rectangle/3,big_rectangle/6,big_rectangle/6])
pygame.draw.rect(gameDisplay,green,[big_rectangle,display_height-big_rectangle/3,big_rectangle/6,big_rectangle/6])
pygame.draw.rect(gameDisplay,yellow,[4*big_rectangle/3,big_rectangle/6,big_rectangle/6,big_rectangle/6])
start_line=big_rectangle
while start_line<=display_width- big_rectangle:
    pygame.draw.line(gameDisplay,black,[start_line,0],[start_line,big_rectangle],3)
    pygame.draw.line(gameDisplay,black,[start_line,display_height-big_rectangle],[start_line,display_height],3)
    pygame.draw.line(gameDisplay,black,[0,start_line],[big_rectangle,start_line],2)
    pygame.draw.line(gameDisplay,black,[display_width-big_rectangle,start_line],[display_width,start_line],2)
    start_line+=40
start_line2 =0
while start_line2 <= big_rectangle:
    pygame.draw.line(gameDisplay, black, [big_rectangle, start_line2], [display_width - big_rectangle, start_line2],2)
    pygame.draw.line(gameDisplay,black,[big_rectangle,display_height-start_line2],[display_width-big_rectangle,display_height-start_line2],2)
    pygame.draw.line(gameDisplay,black,[start_line2,big_rectangle],[start_line2,display_height-big_rectangle],2)
    pygame.draw.line(gameDisplay,black,[display_width-start_line2,big_rectangle],[display_width-start_line2,display_height-big_rectangle],2)
    start_line2 += big_rectangle/6

#Gatti
class Gatti(object):
    radius=10
    gatti_pos=list()
    def __init__(self,color,pos,no):
        for i in xrange(no):
            pygame.draw.circle(gameDisplay,black,pos,self.radius+5)
            pygame.draw.circle(gameDisplay,color,pos,self.radius)
            self.gatti_pos.append(pos)
            if i==0:
                pos[0]+=big_rectangle/2
            elif i==1:
                pos[1]+=big_rectangle/2
            elif i==2:
                pos[0]-=big_rectangle/2

    def update(self, position,color,path):
        pygame.draw.circle(gameDisplay, white, path[position-1], self.radius + 5)
        pygame.draw.circle(gameDisplay, black, path[position], self.radius + 5)
        pygame.draw.circle(gameDisplay, color, path[position], self.radius)
        pygame.display.update()
        
#path
path_x=[60]
start_path_x=60
path_y=[260]
start_path_y=260
for i in xrange(60):
    if (i>1 and i<=5) or (i > 18 and i <= 23) or(i>11 and i<=13):
        start_path_x+=big_rectangle/6
        path_x.append(start_path_x) 
        path_y.append(start_path_y)
    if(i>5 and i<=11) or (i>38 and i<=43):
        if i==6:
            start_path_x+=big_rectangle/6
        start_path_y-=big_rectangle/6
        path_x.append(start_path_x)
        path_y.append(start_path_y)
    if(i>13 and i<=18) or (i>31 and i<=36) or (i>23 and i<=25):
        start_path_y+=big_rectangle/6
        path_y.append(start_path_y)
        path_x.append(start_path_x)
    if i==18:
        start_path_x+=big_rectangle/6
        start_path_y+=big_rectangle/6
        path_x.append(start_path_x)
        path_y.append(start_path_y)
    if(i>25 and i<=30)or (i>36 and i<=38)or (i>45 and i<=50):
        start_path_x-=big_rectangle/6
        path_x.append(start_path_x)
        path_y.append(start_path_y)
    if i==31:
        start_path_x-=big_rectangle/6
        start_path_y+=big_rectangle/6
        path_x.append(start_path_x)
        path_y.append(start_path_y)
    if i==45:
        start_path_x-=big_rectangle/6
        start_path_y-=big_rectangle/6
        path_x.append(start_path_x)
        path_y.append(start_path_y)
        

path_red=[(x1,y1) for x1,y1 in zip(path_x,path_y)]
path_yellow=path_red[12:]+path_red[:12]
path_blue=path_red[25:]+path_red[:25]
path_green=path_red[38:]+path_red[:38]
#print path_red
#print path_yellow
#print path_blue
#print path_green
WIDTH=40

red_gatti = Gatti(red, [big_rectangle / 4, big_rectangle / 4], n)
green_gatti = Gatti(green,[big_rectangle / 4, display_height - 3 * big_rectangle / 4],n)
yellow_gatti = Gatti(yellow,[display_width - 3 * big_rectangle / 4, big_rectangle / 4],n)
blue_gatti = Gatti(blue,[display_width - 3 * big_rectangle / 4, display_height - 3 * big_rectangle / 4],n)



position=[0,0,0,0]
turn=0
#Main game loop
while not gameExit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            user=random.randrange(1, 7)
            dice_roll(user)
            for _ in xrange(1,user+1):
                position[turn%4]+=1
                if turn%4==0:
                    red_gatti.update(position[turn%4],red,path_red)
                elif turn%4==1:
                    yellow_gatti.update(position[turn%4],yellow,path_yellow)
                elif turn%4==2:
                    blue_gatti.update(position[turn%4],blue,path_blue)
                else:
                    green_gatti.update(position[turn%4],green,path_green)
                    
                pygame.time.delay(120)
            turn += 1
            print turn

    
    pygame.display.update()

    clock.tick(5)


pygame.display.quit()
quit()
