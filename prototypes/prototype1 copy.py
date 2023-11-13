<<<<<<< HEAD
import pygame
import math
import matplotlib.pyplot as plt
#import time

pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Projectile Motion")
clock = pygame.time.Clock()

#please go through this and make it better please

fps = 10
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
        angle = (round(math.degrees(math.atan(leny/lenx)),1))
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
    window.blit(font.render(f"Angle: {angle}°", True, black, None),(2,0))
    window.blit(font.render(f"Time: {round(duration,2)}s", True, black, None),(2,120))
    window.blit(font.render("1m", True, black, None),((100),ball_r.y+10))

def mainloop():
    global angle,vvelocity,hvelocity,duration,lenx,leny,ball_r2,back
    run = True
    x = []
    y = []
    veloc = []
    time = []
    newx = ball_r.x
    newy = ball_r.y
    stop = False
    first = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plt.plot(x,y)
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
            first = True
        pygame.draw.rect(window,green,ground_r)
        pygame.draw.rect(window,white,groundcoll_r)
        pygame.draw.rect(window,white,ball_r)
        ball_r2 = pygame.Rect(newx,newy,10,10) 
        pygame.draw.rect(window,black,ball_r2) 
        ballmotion()
        if keys[pygame.K_SPACE] and stop == False:
            if first == True:
                statichvel = hvelocity
                staticvvel = vvelocity
                mag = math.sqrt(hvelocity**2+vvelocity**2)
                print(mag)
                veloc.append(mag)
                first = False
            duration+=0.1
            time.append(duration)
            distancex = (statichvel/2)*duration
            distancey = ((staticvvel/2)*duration)+((-4.9 * (duration**2))/2)
            if back == True:
                newx = ((ball_r.x)-distancex)
            else:
                newx = ((ball_r.x)+distancex)
            x.append(newx)
            newy = (ball_r.y-distancey)
            y.append(height-newy)                   
        if pygame.Rect.contains(ground_r,ball_r2):
            stop = True
            first = True
            duration = 0
            ball_r.x = ball_r2.x
            ball_r.y = ball_r2.y-15
            stop = False
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

=======
import pygame
import math
import matplotlib.pyplot as plt
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
        angle = (round(math.degrees(math.atan(leny/lenx)),1))
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
    window.blit(font.render(f"Angle: {angle}°", True, black, None),(2,0))
    window.blit(font.render(f"Time: {round(duration,2)}s", True, black, None),(2,120))
    window.blit(font.render("1m", True, black, None),((100),ball_r.y+10))

def mainloop():
    global angle,vvelocity,hvelocity,duration,lenx,leny,ball_r2,back
    run = True
    x = []
    y = []
    veloc = []
    time = []
    newx = ball_r.x
    newy = ball_r.y
    stop = False
    first = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plt.plot(x,y)
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
            first = True
        pygame.draw.rect(window,green,ground_r)
        pygame.draw.rect(window,white,groundcoll_r)
        pygame.draw.rect(window,white,ball_r)
        ball_r2 = pygame.Rect(newx,newy,10,10) 
        pygame.draw.rect(window,black,ball_r2) 
        ballmotion()
        if keys[pygame.K_SPACE] and stop == False:
            if first == True:
                statichvel = hvelocity
                staticvvel = vvelocity
                mag = math.sqrt(hvelocity**2+vvelocity**2)
                print(mag)
                veloc.append(mag)
                first = False
            duration+=0.1
            time.append(duration)
            distancex = (statichvel/2)*duration
            distancey = ((staticvvel/2)*duration)+((-4.9 * (duration**2))/2)
            if back == True:
                newx = ((ball_r.x)-distancex)
            else:
                newx = ((ball_r.x)+distancex)
            x.append(newx)
            newy = (ball_r.y-distancey)
            y.append(height-newy)                   
        if pygame.Rect.contains(ground_r,ball_r2):
            stop = True
            first = True
            duration = 0
            ball_r.x = ball_r2.x
            ball_r.y = ball_r2.y-15
            stop = False
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

>>>>>>> 6ad169fec5b342d595b5edf49dadadeeccc8845e
mainloop()