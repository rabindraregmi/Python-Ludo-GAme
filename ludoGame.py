import pygame, time, random
from pygame.locals import *

pygame.init()
green = (0, 255, 0)
blue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
grey = (32, 32, 32)
n=4
display_height = 600
display_width = 600
big_rectangle = 240
hole_radius = 30
gameExit = False
gameOver = False
# Pathing of circles/gatti
path_x = [60]
start_path_x = 60
path_y = [260]
start_path_y = 260
for i in xrange(2, 53):
    if (i > 1 and i <= 5) or (i > 19 and i <= 24) or (i > 11 and i <= 13):
        start_path_x += big_rectangle / 6
    if (i > 6 and i <= 11) or (i > 39 and i <= 44) or (i > 50 and i <= 53):
        start_path_y -= big_rectangle / 6
    if i == 6:
        start_path_x += big_rectangle / 6
        start_path_y -= big_rectangle / 6
    if (i > 13 and i <= 18) or (i > 32 and i <= 37) or (i > 24 and i <= 26):
        start_path_y += big_rectangle / 6
    if i == 19:
        start_path_x += big_rectangle / 6
        start_path_y += big_rectangle / 6
    if (i > 26 and i <= 31) or (i > 37 and i <= 39) or (i > 45 and i <= 50):
        start_path_x -= big_rectangle / 6
    if i == 32:
        start_path_x -= big_rectangle / 6
        start_path_y += big_rectangle / 6
    if i == 45:
        start_path_x -= big_rectangle / 6
        start_path_y -= big_rectangle / 6
    path_x.append(start_path_x)
    path_y.append(start_path_y)
path_red = [(x1, y1) for x1, y1 in zip(path_x, path_y)]
path_yellow = path_red[13:] + path_red[:13] + [(300, 60), (300, 100), (300, 140), (300, 180),
                                               (300, 220), (300, 260), (1000, 1000)]
path_blue = path_red[26:] + path_red[:26] + [(540, 300), (500, 300), (460, 300), (420, 300),
                                             (380, 300), (340, 300), (1000, 1000)]
path_green = path_red[39:] + path_red[:39] + [(300, 540), (300, 500), (300, 460), (300, 420),
                                              (300, 380), (300, 340), (1000, 1000)]
path_red = path_red + [(60, 300), (100, 300), (140, 300), (180, 300), (220, 300), (260, 300), (1000, 1000)]
del path_red[51], path_green[51], path_blue[51], path_yellow[51]
exception = [path_red[0]] + path_red[51:] + [path_red[13]] + path_yellow[51:] + [path_red[26]] + path_blue[51:] + [
    path_red[39]] + path_green[51:]
WIDTH = 40
turnColor = {0: 'Red', 1: 'Yellow', 2: 'Blue', 3: 'Green'}
turnPath = {0: path_red, 1: path_yellow, 2: path_blue, 3: path_green}
board = pygame.image.load('Board\Board.jpeg')

# Message on screen 

def message(gameDisplay,msg, color, x_pos, y_pos):
    font = pygame.font.SysFont(None, 35)
    pygame.draw.rect(gameDisplay, white, [display_width + 10, 0, 190, display_height])
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x_pos, y_pos])
# Code for dice roll
def dice_roll(gameDisplay,num):
    for i in xrange(1,7):
        drawBoard(gameDisplay)
        gameDisplay.blit(pygame.image.load("Dice\dice"+str(random.randrange(1,7))+".jpeg"),(display_height/2,display_width/2))
        pygame.display.update()
        pygame.time.delay(20)
        drawBoard(gameDisplay)
        gameDisplay.blit(pygame.image.load("Dice\dicemid.jpeg"), (display_height / 2-i*random.randrange(1,50), display_width / 2-random.randrange(1,50)))
        pygame.display.update()
        pygame.time.delay(40)
    drawBoard(gameDisplay)
    gameDisplay.blit(pygame.image.load("Dice\dice"+str(num)+".jpeg"), (display_height / 2-40, display_width / 2-40))
    pygame.display.update()


# Circles/Gatti
class Gatti(object):
    radius = 10

    def __init__(self, color, pos, no):
        self.color = color
        self.pos = pos
        self.no = no


    def update(self, gameDisplay,position, path):
        pygame.draw.circle(gameDisplay, black, path[position], self.radius + 5)
        pygame.draw.circle(gameDisplay, self.color, path[position], self.radius)
        for circs in xrange(self.no):
            pygame.draw.circle(gameDisplay,black,path[position],self.radius/10+circs*2)
        if path[position-1] in exception:
            for index in xrange(len(exception)):
                if path[position-1]==exception[index]:
                    if index<6:
                        pygame.draw.circle(gameDisplay, red, path[position - 1], self.radius + 5)
                    elif index<12:
                        pygame.draw.circle(gameDisplay, yellow, path[position - 1], self.radius + 5)
                    elif index<18:
                        pygame.draw.circle(gameDisplay, blue, path[position - 1], self.radius + 5)
                    else:
                        pygame.draw.circle(gameDisplay, green, path[position - 1], self.radius + 5)
                    break
        else:
            pygame.draw.circle(gameDisplay, white, path[position-1], self.radius + 5)
        pygame.display.update()

    def draw(self, gameDisplay,position):
        pygame.draw.circle(gameDisplay, black, position, self.radius + 5)
        pygame.draw.circle(gameDisplay, self.color, position, self.radius)
        for circs in xrange(self.no):
            pygame.draw.circle(gameDisplay,black,position,self.radius/10+circs*2)

    def __str__(self):
        return  str(self.color)+str(self.no)


#Initial gatti position
def gattiInit(color, coord):
    gattilist = list()
    for i in xrange(n):
        clone = tuple(coord[:])
        gatti = Gatti(color, clone, i)
        if i == 0:
            coord[0] += big_rectangle / 2
        elif i == 1:
            coord[1] += big_rectangle / 2
        elif i == 2:
            coord[0] -= big_rectangle / 2
        gattilist.append(gatti)
    return gattilist

#Check move for entering home
def check_move(position, index, dice):
    if position[index][user] + dice < 57:
        return 1
    if position[index][user] + dice == 57:
        return 2
    else:
        return 0

#Check for kills
def check_kill(position, pos_index, dice, startingOne):
    for key in turnPath:
        if turnPath[key]!=turnPath[pos_index]:
            for var in xrange(n):
                if (turnPath[pos_index])[position[pos_index][user] + dice] == (turnPath[key])[position[key][var]]:
                    position[key][var] = 0
                    startingOne[key][var] = 0
                

#Game loop fxn
def gameloop(gameDisplay):
    global position
    position=[]
    for _ in xrange(4):
        position.append([0 for j in xrange(n)])
    turn = 0
    startingOne = []
    for i in xrange(4):
        startingOne.append([0 for j in xrange(n)])
    FPS = 5
    clock = pygame.time.Clock()
    gameExit = False
    gamePercent=[0,0,0,0]
    gameOver = False
    drawBoard(gameDisplay)
    # Main game loop
    while not gameExit:
        chance = 1
        drawBoard(gameDisplay)
        while gameOver == True:
            gameDisplay.fill(white)
            message(gameDisplay,"Game Over", black, display_height / 2, display_width / 2)
            message(gameDisplay,"Winner:" + turnColor[winner], black, display_width / 2, display_height / 2 - 30)
            message(gameDisplay,"Press Q to Quit and C to play again", blue, display_width / 2, display_height / 2 + 30)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameloop(gameDisplay)

                    else:

                        break
        for event in pygame.event.get():
            message(gameDisplay,'TURN : ' + turnColor[turn % 4], red, display_width + 15, display_height / 2)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                dice = random.randrange(1, 7)
                dice_roll(gameDisplay,dice)
                global user
                user=-1
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key ==pygame.K_0:
                                user=0
                            elif event.key ==pygame.K_1:
                                user=1
                            elif event.key ==pygame.K_2:
                                user=2
                            elif event.key ==pygame.K_3:
                                user=3
                    if user>=0:
                        break
                if dice == 1 or dice == 6:
                    if dice == 1:
                        startingOne[turn % 4][user] += 1
                    chance += 1
                if startingOne[turn % 4][user] >= 1:
                    checked = check_move(position, turn % 4, dice)
                    if position[turn%4][user]+dice<57:
                        check_kill(position, turn % 4, dice ,startingOne)
                    if checked == 2:
                        gamePercent[turn%4]+=100/n
                        for anypercent in gamePercent:
                            if anypercent>=99:
                                gameOver = True
                                winner = turn % 4
                    if checked == 0:
                        message(gameDisplay,"Invalid Move", black, display_width + 15, display_height / 2 - 40)
                        if dice != 1 and dice != 6:
                            turn += 1
                        break
                    else:
                        for _ in xrange(1, dice + 1):
                            gameDisplay.blit(board, (0, 0))
                            for u in range(n):
                                red_gatti[u].draw(gameDisplay,([red_gatti[u].pos]+path_red)[position[0][u]])
                                yellow_gatti[u].draw(gameDisplay,([yellow_gatti[u].pos]+ path_yellow)[position[1][u]])
                                blue_gatti[u].draw(gameDisplay,([blue_gatti[u].pos]+path_blue)[position[2][u]])
                                green_gatti[u].draw(gameDisplay,([green_gatti[u].pos]+path_green)[position[3][u]])
                            position[turn % 4][user] += 1
                            if turn % 4 == 0:
                                red_gatti[user].update(gameDisplay,position[turn % 4][user], [red_gatti[user].pos]+path_red)
                            elif turn % 4 == 1:
                                yellow_gatti[user].update(gameDisplay,position[turn % 4][user],[yellow_gatti[user].pos]+ path_yellow)
                            elif turn % 4 == 2:
                                blue_gatti[user].update(gameDisplay,position[turn % 4][user], [blue_gatti[user].pos]+path_blue)
                            else:
                                green_gatti[user].update(gameDisplay,position[turn % 4][user], [green_gatti[user].pos]+path_green)
                            pygame.time.delay(150)
                            pygame.display.update()
                if chance == 1:
                    turn += 1

        pygame.display.update()
        clock.tick(FPS)

#Draw current gatti positions+board
def drawBoard(gameDisplay):
    gameDisplay.blit(board, (0, 0))
    for p in xrange(n):
        red_gatti[p].draw(gameDisplay,([red_gatti[p].pos] + path_red)[position[0][p]])
        yellow_gatti[p].draw(gameDisplay,([yellow_gatti[p].pos] + path_yellow)[position[1][p]])
        blue_gatti[p].draw(gameDisplay,([blue_gatti[p].pos] + path_blue)[position[2][p]])
        green_gatti[p].draw(gameDisplay,([green_gatti[p].pos] + path_green)[position[3][p]])

def main():

    gameDisplay = pygame.display.set_mode((display_width + 200, display_height))
    pygame.display.set_caption("LUDO FOR EVERYONE")
    gameIcon = pygame.image.load('icons\icon.png')
    pygame.display.set_icon(gameIcon)

    gameloop(gameDisplay)
    pygame.display.quit()
    quit()


red_gatti = gattiInit(red, [big_rectangle / 4, big_rectangle / 4])
green_gatti = gattiInit(green, [big_rectangle / 4, display_height - 3 * big_rectangle / 4])
yellow_gatti = gattiInit(yellow, [display_width - 3 * big_rectangle / 4, big_rectangle / 4])
blue_gatti = gattiInit(blue, [display_width - 3 * big_rectangle / 4, display_height - 3 * big_rectangle / 4])
