import pygame
import math
#import matplotlib.pyplot as plt
import time

# https://www.youtube.com/watch?v=Y4xlUNfrvow try this video please
# use this and get it to show the trajectory path of the object and calc velocity
pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Projectile Motion")
clock = pygame.time.Clock()

fps = 60
distance = 0
vdistance = 0
white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 255)
font = pygame.font.SysFont("Comic Sans MS", 30, False)
mousex = (width)/2
mousey = (height)/2
gravity = 9.81
duration = 0    
meter = 1

ground_r = pygame.Rect(0, height-100, width, 100)
groundcoll_r = pygame.Rect(0, height-110, width, 10)
ball_r = pygame.Rect(5,ground_r.y-10,10,10)

def velocity():
    global hdistance,vdistance,vvelocity,hvelocity,angle
    try:
        vvelocity = round(math.sqrt(2*gravity*vdistance),2) 
    except ValueError:
        vvelocity = 0
    try:
        hvelocity = round(math.sqrt(2*gravity*hdistance),2)
    except ValueError:
        hvelocity = 0  
    
def ballmotion():
    global hdistance,vdistance,vvelocity,hvelocity,angle,duration,mousex,mousey,lenx,leny
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mousex-=5
    if keys[pygame.K_RIGHT]:
        mousex+=5
    if keys[pygame.K_UP]:
        mousey-=5
    if keys[pygame.K_DOWN]:
        mousey+=5
    pygame.draw.line(window,red,pygame.math.Vector2(ball_r.x+10,ball_r.y),pygame.math.Vector2(mousex,mousey),5)
    leny = height-((mousey+ball_r.y)-380)
    lenx = mousex-(ball_r.x+10)
    try:
        angle = (round(math.degrees(math.atan(leny/lenx)),1))
    except ZeroDivisionError:
        angle = 90
    hdistance = round((lenx/meter),2)
    vdistance = round((leny/meter),2)
    velocity()
    #duration = ((math.sqrt(vvelocity**2+hvelocity**2))*math.sin(angle)/gravity)*2
    window.blit(font.render(f"Vertical Velocity: {round(vvelocity/300,2)}m/s", True, black, None), (2,40))
    window.blit(font.render(f"Horizonal Velocity: {round(hvelocity/300,2)}m/s", True, black, None), (2,80))
    window.blit(font.render(f"Angle: {angle}°", True, black, None),(2,0))
    window.blit(font.render(f"Time: {round(duration,2)}s", True, black, None),(2,120))
    window.blit(font.render("1m", True, black, None),((300),ball_r.y+10))

def mainloop():
    global angle,vvelocity,hvelocity,duration,lenx,leny
    run = True
    #x = []
    #y = []
    newx = 0
    newy = 0
    stop = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                #plt.plot(x,y)
                #plt.savefig(f'image.png')
        window.fill(white)
        pygame.draw.rect(window,green,ground_r)
        pygame.draw.rect(window,white,groundcoll_r)
        pygame.draw.rect(window,black,ball_r)
        ball_r2 = pygame.Rect(newx,newy,10,10) 
        pygame.draw.rect(window,black,ball_r2) 
        ballmotion()   
        keys = pygame.key.get_pressed()
        if keys [pygame.K_a]:
            duration = 0
            stop = False
        if keys[pygame.K_SPACE] and stop == False:
            duration+=0.075
            distancex = (hvelocity/2)*duration
            distancey = ((vvelocity/2)*duration)+((-4.9 * (duration**2))/2)
            newx = ((ball_r.x)+distancex)
            newy = (ball_r.y-distancey)                      
        if pygame.Rect.contains(groundcoll_r,ball_r2):
            stop = True
        pygame.draw.line(window,blue,pygame.Vector2(ball_r.x,ball_r.y+10),pygame.Vector2((hdistance),(ball_r.y+10)),3)
        pygame.draw.line(window,green,pygame.Vector2(ball_r.x,ball_r.y+10),pygame.Vector2((ball_r.x),((height-210)-vdistance)),3)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

mainloop()