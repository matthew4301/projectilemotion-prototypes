import pygame
import math
import matplotlib.pyplot as plt
import time

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
font = pygame.font.SysFont("Comic Sans MS", 30, False)
mousex = (info.current_w)/2
mousey = (info.current_h)/2

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
    global hdistance,vdistance,vvelocity,hvelocity,angle,duration,mousex,mousey
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
    leny = (mousey-ground_r.y+10)/600
    lenx = (mousex-15)/600
    try:
        angle = (round(math.degrees(math.atan(leny/lenx)),1))*-1 
    except ZeroDivisionError:
        angle = 90
    hdistance = round((mousex)/600,2)
    vdistance = round(((info.current_h-210)-mousey)/600,2)
    velocity()
    duration = math.sqrt(vvelocity**2+hvelocity**2)/9.81
    window.blit(font.render(f"Vertical Velocity: {vvelocity}m/s", True, black, None), (2,40))
    window.blit(font.render(f"Horizonal Velocity: {hvelocity}m/s", True, black, None), (2,80))
    window.blit(font.render(f"Angle: {angle}°", True, black, None),(2,0))
    window.blit(font.render(f"Time: {round(duration,2)}s", True, black, None),(2,120))
    window.blit(font.render("1m", True, black, None),(600,ball_r.y+10))

def mainloop():
    global angle,vvelocity,hvelocity,duration
    run = True
    i=0
    j=0
    x = []
    y = []
    currenttime = []
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                plt.plot(x,y)
                plt.savefig(f'image.png')
        window.fill(white)
        pygame.draw.rect(window,green,ground_r)
        pygame.draw.rect(window,black,ball_r)
        ballmotion()   
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            currenttime.append(time.time())
            try:
                if currenttime[j] >= currenttime[0]+duration:
                    for i in range(len(x)):
                        newx = (ball_r.x+x[i]*5)
                        newy = (ball_r.y-y[i]*5)
                        if newy < 0:
                            newy*=-1
                            y[i]*=-1
                        if newx < 0:
                            newx*=-1
                            x[i]*=-1 
                        ball_r2 = pygame.Rect(newx,newy,5,5)
                        pygame.draw.rect(window,black,ball_r2)
                else:
                    window.blit(font.render("graph", True, black, None),(300,200))
                    r = vvelocity**2+hvelocity**2
                    x.append(i)
                    y.append(x[i]*math.tan(angle)-(9.81*x[i]**2)*((1+math.tan(angle)**2)/(2*r**2)))
                    i+=1
                j+=1
            except IndexError:
                currenttime = []
                j=0
        pygame.draw.line(window,blue,pygame.Vector2(ball_r.x,ball_r.y+10),pygame.Vector2((hdistance*600),(ball_r.y+10)),3)
        pygame.draw.line(window,green,pygame.Vector2(ball_r.x,ball_r.y+10),pygame.Vector2((ball_r.x),((info.current_h-210)-vdistance*600)),3)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

mainloop()