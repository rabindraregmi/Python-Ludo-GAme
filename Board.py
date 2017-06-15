import pygame
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


def draw_board():
    def uddrawcircle(centre1, centre2, radius1):
        pygame.draw.circle(gameDisplay, white, [centre1, centre2], radius1)
    global gameDisplay
    gameDisplay= pygame.display.set_mode((display_width + 200, display_height))
    pygame.display.update()
    pygame.display.set_caption("LUDO FOR EVERYONE")
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
