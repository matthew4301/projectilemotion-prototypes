import pygame
import math
import matplotlib.pyplot as plt

pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Projectile Motion")
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont("Arial", 30, False)
ground = pygame.Rect(5,height-100,width,100)
collision = pygame.Rect(0,height-110,width+100,10)
bounds = pygame.Rect(0,0,width,height)
back = False
white = (255,255,255)
green = (0,100,0)
red = (255,0,0)
black = (0,0,0)
velocities = []
time = []
x = []
y = []

class Ball():
    def __init__(self) -> None:
        self.ball_r = pygame.Rect(5,ground.y-10,10,10)
        self.duration = 0
        self.newx = 0
        self.newy = 0

    def controls(self,mousex,mousey):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mousex-=5
        if keys[pygame.K_RIGHT]:
            mousex+=5
        if keys[pygame.K_UP]:
            mousey-=5
        if keys[pygame.K_DOWN]:
            mousey+=5
        return mousex,mousey
    
    def movement(self,hvelocity,vvelocity,duration,first,back):
        if first == True:
            mag = math.sqrt(hvelocity**2+vvelocity**2)
            velocities.append(mag)
            first = False
        duration+=0.1
        time.append(duration)
        distancex = (hvelocity/2)*duration            
        distancey = ((vvelocity/2)*duration)+((-4.9 * (duration**2))/2)
        if back == True:
            newx = ((b.ball_r.x)-distancex)
        else:
            newx = ((b.ball_r.x)+distancex)
        back = False
        x.append(newx)
        newy = (b.ball_r.y-distancey)
        y.append(height-newy)
        ball_r2 = pygame.Rect(newx,newy,10,10)
        return duration,ball_r2

    def reset(self):
        self.duration = 0
        b.ball_r.x = 5
        b.ball_r.y = height-110
        self.newx = b.ball_r.x
        self.newy = b.ball_r.y
        self.stop = False
        first = True
        return first

class Calculations():
    def __init__(self) -> None:
        self.gravity = 9.81

    def velocity(self,gravity,vdistance,hdistance,angle):
        try:
            vvelocity = round(math.sqrt(2*gravity*vdistance),2)
        except ValueError:
            vvelocity = 0
        try:
            hvelocity = round(math.sqrt(2*gravity*hdistance),2)
        except ValueError:
            hvelocity = 0
        return vvelocity,hvelocity
    
    def angle(self,back,lenx,leny,ball_r):
        try:
            angle = round(math.degrees(math.atan(leny/lenx)))
            if angle < 0:
                back = True
                angle*=-1
        except ZeroDivisionError:
            angle = 90
        return angle,back
    
    def distance(self,lenx,leny):
        hdistance = round(lenx*10,2)
        vdistance = round(leny*10,2)
        return hdistance,vdistance
    
    def graphs(self,x,y):
        plt.plot(x,y)
        plt.savefig("xy.png")
        plt.plot(velocities,time)
        plt.savefig("velocitytime.png")

class Graphics():
    def draw(self,ball_r2,mousex,mousey):
        pygame.draw.rect(window,white,bounds)
        pygame.draw.rect(window,green,ground)
        pygame.draw.rect(window,white,collision)
        pygame.draw.rect(window,white,b.ball_r)
        pygame.draw.line(window,red,pygame.math.Vector2(ball_r2.x+10,ball_r2.y),pygame.math.Vector2(mousex,mousey),5)
        pygame.draw.rect(window,black,ball_r2)

    def bounds(self,ball_r2,mousex,mousey):
        if pygame.Rect.contains(bounds,ball_r2) == False:
            # if y > 600 mousey-600-mousey
            # if y < 0 mousey+600+mousey
            # same for x??????????
            ball_r2.x+=10
            ball_r2.y-=10

    def text(self,vvelocity,hvelocity,mousex,mousey,angle,duration):
        window.blit(font.render(f"Vertical Velocity: {round(vvelocity/50,2)}m/s", True, black, None), (2,40))
        window.blit(font.render(f"Horizonal Velocity: {round(hvelocity/50,2)}m/s", True, black, None), (2,80))
        window.blit(font.render(f"Angle: {angle}°", True, black, None),(2,0))
        window.blit(font.render(f"Time: {round(duration,2)}s", True, black, None),(2,120))
        window.blit(font.render("1m", True, black, None),((100),b.ball_r.y+10))
        window.blit(font.render(f"x: {mousex} y: {mousey}", True, black, None),(2,160))

def mainloop():
    run = True
    back = False
    stop = False
    first = True
    duration = 0
    mousex = width/2
    mousey = height/2
    ball_r2 = pygame.Rect(5,ground.y-10,10,10)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c.graphs(x,y)
                run = False
        mousex,mousey = b.controls(mousex,mousey)
        leny = (height-((mousey+b.ball_r.y)-380))/10
        lenx = (mousex-(b.ball_r.x+10))/10
        g.draw(ball_r2,mousex,mousey)
        g.bounds(ball_r2)
        hdistance,vdistance = c.distance(lenx,leny)
        angle,back = c.angle(back,lenx,leny,b.ball_r)
        if first == True:
            vvelocity,hvelocity = c.velocity(c.gravity,vdistance,hdistance,angle)
        g.text(vvelocity,hvelocity,mousex,mousey,angle,duration)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            first = b.reset()
        if keys[pygame.K_SPACE] and stop == False:
            duration,ball_r2 = b.movement(hvelocity,vvelocity,duration,first,back)
        if pygame.Rect.contains(ground,ball_r2):
            stop = True
            first = True
            duration = 0
            b.ball_r.x = ball_r2.x
            b.ball_r.y = ball_r2.y-15
            stop = False
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

c = Calculations()
b = Ball()
g = Graphics()
mainloop()