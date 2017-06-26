import pygame
white=(255,255,255)
black=(0,0,0)
global gameDisplay
gameDisplay=pygame.display.set_mode((600,600))
class Gatti(object):
    radius = 10

    def __init__(self, color, pos, no):
        self.color = color
        self.pos = pos
        self.no = no


    def update(self, position, path):
        pygame.draw.circle(gameDisplay, black, path[position], self.radius + 5)
        pygame.draw.circle(gameDisplay, self.color, path[position], self.radius)
        #pygame.draw.circle(gameDisplay, white, path[position - 1], self.radius + 5)
        pygame.display.update()
        print position, path[position]

    def draw(self, position):
        pygame.draw.circle(gameDisplay, black, position, self.radius + 5)
        pygame.draw.circle(gameDisplay, self.color, position, self.radius)