import pygame, time, random, Board
from pygame.locals import *

pygame.init()
n = int(raw_input())
green = (0, 255, 0)
blue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
grey = (32, 32, 32)
display_height = 600
display_width = 600
big_rectangle = 240
hole_radius = 30
gameExit = False
gameOver = False


def uddrawcircle(centre1, centre2, radius1):
    pygame.draw.circle(Board.gameDisplay, white, [centre1, centre2], radius1)


font = pygame.font.SysFont(None, 35)


def message(msg, color, x_pos, y_pos):
    pygame.draw.rect(Board.gameDisplay, white, [display_width + 10, 0, 190, display_height])
    screen_text = font.render(msg, True, color)
    Board.gameDisplay.blit(screen_text, [x_pos, y_pos])


# Code for dice
dice_size = 80
x = display_width / 2 - dice_size / 2
y = display_width / 2 - dice_size / 2
dot_size = dice_size // 10
mid = dice_size // 2
left = top = dice_size // 4
right = bottom = dice_size - left


def dice_roll(num):
    pygame.draw.rect(Board.gameDisplay, grey, (x - 3, y - 3, dice_size + 6, dice_size + 6))
    pygame.draw.rect(Board.gameDisplay, black, (x - 3, y - 3, dice_size + 6, dice_size + 6))
    if num == 1:
        pygame.draw.circle(Board.gameDisplay, white, (x + mid, y + mid), dot_size)
    else:
        if num == 2 or num == 3:
            pygame.draw.circle(Board.gameDisplay, white, (x + right, y + mid), dot_size)
            pygame.draw.circle(Board.gameDisplay, white, (x + left, y + mid), dot_size)
            if num == 3:
                pygame.draw.circle(Board.gameDisplay, white, (x + mid, y + mid), dot_size)
        else:
            pygame.draw.circle(Board.gameDisplay, white, (x + right, y + top), dot_size)
            pygame.draw.circle(Board.gameDisplay, white, (x + left, y + top), dot_size)
            pygame.draw.circle(Board.gameDisplay, white, (x + left, y + bottom), dot_size)
            pygame.draw.circle(Board.gameDisplay, white, (x + right, y + bottom), dot_size)
            if num == 5:
                pygame.draw.circle(Board.gameDisplay, white, (x + mid, y + mid), dot_size)
            elif num == 6:
                pygame.draw.circle(Board.gameDisplay, white, (x + mid, y + top), dot_size)
                pygame.draw.circle(Board.gameDisplay, white, (x + mid, y + bottom), dot_size)


# Gatti
class Gatti(object):
    radius = 10
    gatti_pos = list()

    def __init__(self, color, pos, no):
        self.color = color
        self.pos = pos
        self.no = no

    def draw_initialpos(self):
        for i in xrange(self.no):
            pygame.draw.circle(Board.gameDisplay, black, self.pos, self.radius + 5)
            pygame.draw.circle(Board.gameDisplay, self.color, self.pos, self.radius)
            self.gatti_pos.append(self.pos)
            if i == 0:
                self.pos[0] += big_rectangle / 2
            elif i == 1:
                self.pos[1] += big_rectangle / 2
            elif i == 2:
                self.pos[0] -= big_rectangle / 2

    def update(self, position, path):
        pygame.draw.circle(Board.gameDisplay, black, path[position], self.radius + 5)
        pygame.draw.circle(Board.gameDisplay, self.color, path[position], self.radius)
        pygame.draw.circle(Board.gameDisplay, white, path[position - 1], self.radius + 5)
        pygame.display.update()
        print position, path[position]

    def draw(self, position):
        pygame.draw.circle(Board.gameDisplay, black, position, self.radius + 5)
        pygame.draw.circle(Board.gameDisplay, self.color, position, self.radius)


def check_move(position, index, dice, red_path, green_path, blue_path, yellow_path):
    if position[index] + dice < 57:
        return 1
    if position[index] + dice == 57:
        return 2
    else:
        return 0


def check_kill(position, pos_index, dice, path1, path2, path3, path4,startingOne):
    if position[pos_index] + dice < 57:
        if pos_index == 0:
            print "R", path1[position[pos_index] + dice]
            print "Y", path2[position[1]]
            print "B",path3[position[2]]
            print "G",path4[position[3]]
            if path1[position[pos_index] + dice]==path2[position[1]]:
                position[1]=0
                startingOne[1]=0
            if path1[position[pos_index] + dice] == path3[position[2]]:
                position[2]=0
                startingOne[2]=0
            if path1[position[pos_index] + dice] == path4[position[3]]:
                position[3]=0
                startingOne[3]=0
        if pos_index == 1:
            print "Y", path2[position[pos_index] + dice]
            print "R", path1[position[0]]
            print "B", path3[position[2]]
            print "G", path4[position[3]]
            if path2[position[pos_index] + dice]==path1[position[0]]:
                position[0]=0
                startingOne[0]=0
            if path2[position[pos_index] + dice] == path3[position[2]]:
                position[2]=0
                startingOne[2]=0
            if path2[position[pos_index] + dice] == path4[position[3]]:
                position[3]=0
                startingOne[3]=0
        if pos_index == 2:
            print "B", path3[position[pos_index] + dice]
            print "R", path1[position[0]]
            print "Y", path2[position[1]]
            print "G", path4[position[3]]
            if path3[position[pos_index] + dice]==path1[position[0]]:
                position[0]=0
                startingOne[0]=0
            if path3[position[pos_index] + dice] == path2[position[1]]:
                position[1]=0
                startingOne[1]=0
            if path3[position[pos_index] + dice] == path4[position[3]]:
                position[3]=0
                startingOne[3]=0
        if pos_index == 3:
            print "G", path4[position[pos_index] + dice]
            print "R", path1[position[0]]
            print "B", path3[position[2]]
            print "Y", path2[position[1]]
            if path4[position[pos_index] + dice]==path1[position[0]]:
                position[0]=0
                startingOne[0]=0
            if path4[position[pos_index] + dice] == path3[position[2]]:
                position[2]=0
                startingOne[2]=0
            if path1[position[pos_index] + dice] == path2[position[1]]:
                position[1]=0
                startingOne[1]=0

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
path_yellow = [(1000, 1000)] + path_red[13:] + path_red[:13] + [(300, 60), (300, 100), (300, 140), (300, 180),
                                                                (300, 220), (300, 260)]
path_blue = [(1000, 1000)] + path_red[26:] + path_red[:26] + [(540, 300), (500, 300), (460, 300), (420, 300),
                                                              (380, 300), (340, 300)]
path_green = [(1000, 1000)] + path_red[39:] + path_red[:39] + [(300, 540), (300, 500), (300, 460), (300, 420),
                                                               (300, 380), (300, 340)]
path_red = [(1000, 1000)] + path_red + [(60, 300), (100, 300), (140, 300), (180, 300), (220, 300), (260, 300)]
del path_red[52], path_green[52], path_blue[52], path_yellow[52]
print path_red
print path_yellow
print path_blue
print path_green
WIDTH = 40


def gameloop():
    position = [0, 0, 0, 0]
    turn = 0
    startingOne = [0, 0, 0, 0]
    turnColor = {0: 'Red', 1: 'Yellow', 2: 'Blue', 3: 'Green'}
    FPS = 15
    clock = pygame.time.Clock()
    gameExit = False
    gameOver = False
    Board.draw_board()
    red_gatti.draw_initialpos()
    yellow_gatti.draw_initialpos()
    blue_gatti.draw_initialpos()
    green_gatti.draw_initialpos()
    # Main game loop
    while not gameExit:
        chance = 1
        while gameOver == True:
            Board.gameDisplay.fill(white)
            message("Game Over", black, display_height / 2, display_width / 2)
            message("Winner:" + turnColor[winner], black, display_width / 2, display_height / 2 - 30)
            message("Press Q to Quit and C to play again", blue, display_width / 2, display_height / 2 + 30)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameloop()

                    else:

                        break
        for event in pygame.event.get():
            message('TURN : ' + turnColor[turn % 4], red, display_width + 15, display_height / 2)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                dice = random.randrange(1, 7)
                if dice == 1 or dice == 6:
                    if dice == 1:
                        startingOne[turn % 4] += 1
                    chance += 1
                dice_roll(dice)
                if startingOne[turn % 4] >= 1:

                    checked = check_move(position, turn % 4, dice, path_red, path_green, path_blue, path_yellow)
                    check_kill(position, turn % 4, dice, path_red, path_yellow, path_blue, path_green,startingOne)
                    print checked
                    if checked == 0:
                        message("Invalid Move", black, display_width + 15, display_height / 2 - 40)
                        if dice != 1 and dice != 6:
                            turn += 1
                        break
                    elif checked == 2:
                        gameOver = True
                        winner = turn % 4
                        continue

                    else:
                        for _ in xrange(1, dice + 1):
                            Board.draw_board()
                            dice_roll(dice)
                            red_gatti.draw(path_red[position[0]])
                            yellow_gatti.draw(path_yellow[position[1]])
                            blue_gatti.draw(path_blue[position[2]])
                            green_gatti.draw(path_green[position[3]])
                            position[turn % 4] += 1
                            if turn % 4 == 0:
                                red_gatti.update(position[turn % 4], path_red)
                            elif turn % 4 == 1:
                                yellow_gatti.update(position[turn % 4], path_yellow)
                            elif turn % 4 == 2:
                                blue_gatti.update(position[turn % 4], path_blue)
                            else:
                                green_gatti.update(position[turn % 4], path_green)
                            pygame.time.delay(120)
                if chance == 1:
                    turn += 1

        pygame.display.update()
        clock.tick(FPS)


red_gatti = Gatti(red, [big_rectangle / 4, big_rectangle / 4], n)
green_gatti = Gatti(green, [big_rectangle / 4, display_height - 3 * big_rectangle / 4], n)
yellow_gatti = Gatti(yellow, [display_width - 3 * big_rectangle / 4, big_rectangle / 4], n)
blue_gatti = Gatti(blue, [display_width - 3 * big_rectangle / 4, display_height - 3 * big_rectangle / 4], n)
gameloop()
pygame.display.quit()
quit()