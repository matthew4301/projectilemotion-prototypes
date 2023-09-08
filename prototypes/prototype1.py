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
    leny = (mousey-ground_r.y+10)/150
    lenx = (mousex-15)/150
    try:
        angle = (round(math.degrees(math.atan(leny/lenx)),1))*-1 
    except ZeroDivisionError:
        angle = 90
    hdistance = round((mousex)/150,2)
    vdistance = round(((info.current_h-210)-mousey)/150,2)
    velocity()
    duration = math.sqrt(vvelocity**2+hvelocity**2)/9.81
    window.blit(font.render(f"Vertical Distance: {vdistance}m", True, black, None),(2,120))
    window.blit(font.render(f"Horizontal Distance: {hdistance}m", True, black, None),(2,160))
    window.blit(font.render(f"Vertical Velocity: {vvelocity}m/s", True, black, None), (2,40))
    window.blit(font.render(f"Horizonal Velocity: {hvelocity}m/s", True, black, None), (2,80))
    window.blit(font.render(f"Angle: {angle}°", True, black, None),(2,0))
    window.blit(font.render(f"duration: {round(duration,2)}s", True, black, None),(2,200))
    window.blit(font.render("1m", True, black, None),(150,ball_r.y+10))

def mainloop():
    global angle,vvelocity,hvelocity,duration
    run = True
    i=0
    x = []
    y = []
    x2 = []
    y2 = []
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                x2.reverse()
                y2.reverse()
                up = (y2[0]*-1)
                right = (x2[0]*-1)
                for i in range(len(x2)):
                    x2[i]+=right
                for i in range(len(x)):
                    x[i]+=right
                for i in range(len(y2)):
                    y2[i]+=up
                for i in range(len(y)):
                    y[i]+=up
                #plt.plot((x2+x),(y2+y))
                plt.plot(x,y)
                plt.savefig(f'image{i}.png')
        window.fill(white)
        pygame.draw.rect(window,green,ground_r)
        pygame.draw.rect(window,black,ball_r)
        ballmotion()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            window.blit(font.render("graph", True, black, None),(300,200))
            r = math.sqrt(vvelocity**2+hvelocity**2)
            x.append(i)
            x2.append(-i)
            y.append(r * math.sin(angle) * x[i] - (0.5) * 9.81 * x[i]**2)
            y2.append(-(r * math.sin(angle) * x[i] - (0.5) * 9.81 * x[i]**2))           
            #y.append((math.tan(angle))*x[i] - (4.905/(r**2)*(math.cos(angle)**2))*(x[i]**2))
            #y2.append(-((math.tan(angle))*x2[i] - (4.905/(r**2)*(math.cos(angle)**2))*(x2[i]**2))*-1)
            i+=1
        pygame.draw.line(window,blue,pygame.Vector2(ball_r.x,ball_r.y+10),pygame.Vector2((hdistance*150),(ball_r.y+10)),3)
        pygame.draw.line(window,green,pygame.Vector2(ball_r.x,ball_r.y+10),pygame.Vector2((ball_r.x),((info.current_h-210)-vdistance*150)),3)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

mainloop()