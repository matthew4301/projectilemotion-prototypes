import pygame
import math
import matplotlib.pyplot as plt
import pylab as plb
import time as t
#import time

pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Projectile Motion")
clock = pygame.time.Clock()

#please go through this and make it better please

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
back = False

ground_r = pygame.Rect(0, height-100, width, 100)
groundcoll_r = pygame.Rect(0, height-110, width+100, 10)
ball_r = pygame.Rect(5,ground_r.y-10,10,10)

def round_nearest(num: float, to: float) -> float:
    return round(num / to) * to 

def velocity():
    global hdistance,vdistance,vvelocity,hvelocity,angle,x,y,mag,h_max
    try:
        vvelocity = round(math.sqrt(2*gravity*vdistance),2) 
    except ValueError:
        vvelocity = 0
    try:
        hvelocity = round(math.sqrt(2*gravity*hdistance),2)
    except ValueError:
        hvelocity = 0 
    y0=100
    mag = math.sqrt(vvelocity**2+hvelocity**2)/5 
    a=gravity
    b=-2*mag*math.sin(angle)
    c=-2*y0
    coeff=plb.array([a,b,c])
    t1,t2=plb.roots(coeff)
    h1=mag**2*(math.sin(angle))**2/(2*gravity)
    h_max=h1*10+y0
    R=mag*math.cos(angle)*plb.max(t1,t2)
    x=plb.linspace(0,R,50)
    y=x*math.tan(angle)-(1/2)*(gravity*x**2)/(mag**2*(math.cos(angle))**2 )
    
def ballmotion():
    global hdistance,vdistance,vvelocity,hvelocity,angle,duration,mousex,mousey,lenx,leny,ball_r2,back
    #mousex, mousey = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mousex-=5
    if keys[pygame.K_RIGHT]:
        mousex+=5
    if keys[pygame.K_UP]:
        mousey-=5
    if keys[pygame.K_DOWN]:
        mousey+=5
    pygame.draw.line(window,red,pygame.math.Vector2(ball_r2.x+10,ball_r2.y),pygame.math.Vector2(mousex,mousey),5)
    leny = height-((mousey+ball_r.y)-380)
    lenx = mousex-(ball_r.x+10)
    try:
        angle = math.radians((round(math.degrees(math.atan(leny/lenx)),1)))
        if angle < 0:
            back = True
            angle*=-1
        else:
            back = False
    except ZeroDivisionError:
        angle = 90
    hdistance = round((lenx/meter),2)
    vdistance = round((leny/meter),2)
    velocity()
    window.blit(font.render(f"Vertical Velocity: {round(vvelocity/50,2)}m/s", True, black, None), (2,40))
    window.blit(font.render(f"Horizonal Velocity: {round(hvelocity/50,2)}m/s", True, black, None), (2,80))
    window.blit(font.render(f"Angle: {round(angle,2)} radians", True, black, None),(2,0))
    window.blit(font.render(f"Time: {round(duration,2)}s", True, black, None),(2,120))
    window.blit(font.render("1m", True, black, None),((100),ball_r.y+10))

def mainloop():
    global angle,vvelocity,hvelocity,duration,lenx,leny,ball_r2,back,x,y,mag,h_max
    run = True
    veloc = []
    time = []
    newx = ball_r.x
    newy = ball_r.y
    stop = False
    down = False
    first = True
    i = 0
    duration = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plt.plot(time,veloc)
                gradient = (2*mag)/veloc[1]
                c = veloc[1]/(gradient*time[1])
                print(f"y = {gradient}x + {c}")
                plt.savefig(f'image.png')
                run = False
        window.fill(white)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            duration = 0
            ball_r.x = 5
            ball_r.y = height-110
            newx = ball_r.x
            newy = ball_r.y
            stop = False
            down = False
        pygame.draw.rect(window,green,ground_r)
        pygame.draw.rect(window,white,groundcoll_r)
        pygame.draw.rect(window,white,ball_r)
        ball_r2 = pygame.Rect(newx,newy,10,10) 
        pygame.draw.rect(window,black,ball_r2) 
        ballmotion()
        if keys[pygame.K_SPACE] and stop == False:
            newx = ball_r2.x+x[i]
            newy = ball_r2.y-y[i]
            if newy <= height-h_max:
                down = True
            if down == True:
                veloc.append(-mag)
                time.append(duration)
            if first == True:
                veloc.append(mag)
                time.append(0) 
                first = False          
            i+=1
            t.sleep(0.05)      
            duration+=0.05      
        if pygame.Rect.contains(ground_r,ball_r2):
            stop = True
            i=0
            duration = 0
            ball_r.x = ball_r2.x
            ball_r.y = ball_r2.y-15
            stop = False
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

mainloop()