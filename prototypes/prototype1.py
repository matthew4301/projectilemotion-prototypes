import pygame
import math
import matplotlib.pyplot as plt
import datetime as dt

# 150 pixels is a meter

pygame.init()
info = pygame.display.Info()
window = pygame.display.set_mode((info.current_w,info.current_h))
pygame.display.set_caption("Projectile Motion")
clock = pygame.time.Clock()

fps = 60
distance = 0
vdistance = 0
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 255)
font = pygame.font.SysFont("Comic Sans MS", 20, False)

flist = []
tlist = []

ground_r = pygame.Rect(0, info.current_h-200, info.current_w, 100)
ball_r = pygame.Rect(5,ground_r.y-10,10,10)

def velocity():
    global hdistance,vdistance,vvelocity,hvelocity,angle
    try:
        vvelocity = round(math.sqrt(2*9.81*vdistance),2) 
    except ValueError:
        vvelocity = 0
    try:
        hvelocity = round(math.sqrt(2*9.81*hdistance),2)
    except ValueError:
        hvelocity = 0  
    
def ballmotion():
    global hdistance,vdistance,vvelocity,hvelocity,angle
    if pygame.mouse.get_pressed():
        mousex,mousey = pygame.mouse.get_pos()
    pygame.draw.line(window,red,pygame.math.Vector2(ball_r.x+10,ball_r.y),pygame.math.Vector2(mousex,mousey),5)
    leny = (mousey-ground_r.y+10)/150
    lenx = (mousex-15)/150
    try:
        angle = (round(math.degrees(math.atan(leny/lenx)),1))*-1 
    except ZeroDivisionError:
        angle = 90
    hdistance = round((mousex)/150,2)
    vdistance = round(((info.current_h-210)-mousey)/150,2)
    velocity()
    time = math.sqrt(vvelocity**2+hvelocity**2)/9.81
    window.blit(font.render(f"Vertical Distance: {vdistance}m", True, black, None),(2,60))
    window.blit(font.render(f"Horizontal Distance: {hdistance}m", True, black, None),(2,80))
    window.blit(font.render(f"Vertical Velocity: {vvelocity}m/s", True, black, None), (2,20))
    window.blit(font.render(f"Horizonal Velocity: {hvelocity}m/s", True, black, None), (2,40))
    window.blit(font.render(f"Angle: {angle}°", True, black, None),(2,0))
    window.blit(font.render(f"Time: {round(time,2)}s", True, black, None),(2,100))
    window.blit(font.render("1m", True, black, None),(150,ball_r.y+10))

def mainloop():
    run = True
    i=0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plt.savefig('graph.png')  
                run = False
        i+=1
        if i%2 == 0:
            flist.append(clock.get_fps())
            tlist.append(dt.datetime.now().strftime('%H:%M:%S'))
            plt.xticks(rotation=45, ha='right',fontsize=4)
            plt.plot(tlist,flist)
        window.fill(white)
        pygame.draw.rect(window,green,ground_r)
        pygame.draw.rect(window,black,ball_r)
        ballmotion()
        pygame.draw.line(window,blue,pygame.Vector2(ball_r.x,ball_r.y+10),pygame.Vector2((hdistance*150),(ball_r.y+10)),3)
        pygame.draw.line(window,green,pygame.Vector2(ball_r.x,ball_r.y+10),pygame.Vector2((ball_r.x),((info.current_h-210)-vdistance*150)),3)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

mainloop()