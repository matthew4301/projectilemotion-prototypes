import pygame
import math
import matplotlib.pyplot as plt

pygame.init()
width = 800
height = 600
mousex = width/2
mousey = height/2
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Projectile Motion")
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont("Arial", 30, False)
ground = pygame.Rect(5,height-100,width,100)
collision = pygame.Rect(0,height-110,width+100,10)
back = False
white = (255,255,255)
green = (0,100,0)
red = (255,0,0)
black = (0,0,0)

class Ball():
    def __init__(self) -> None:
        self.ball_r = pygame.Rect(5,ground.y-10,10,10)
        self.ball_r2 = pygame.Rect(5,ground.y-10,10,10)
        self.velocities = []
        self.time = []
        self.x = []
        self.y = []
        self.mousex = width/2
        self.mousey = height/2
        self.duration = 0
    def controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.mousex-=5
        if keys[pygame.K_RIGHT]:
            self.mousex+=5
        if keys[pygame.K_UP]:
            self.mousey-=5
        if keys[pygame.K_DOWN]:
            self.mousey+=5
        return self.mousex,self.mousey
    def movement(self,vvelocity,hvelocity):
        first = True
        self.stop = False
        self.newx = self.ball_r.x
        self.newy = self.ball_r.y
        distancex = 0
        distancey = 0
        duration = 0
        if self.stop == False:
            if first == True:
                statichvel = hvelocity
                staticvvel = vvelocity
                mag = math.sqrt(hvelocity**2+vvelocity**2)
                self.velocities.append(mag)
                first = False
            self.duration+=0.1
            self.time.append(self.duration)
            distancex = (statichvel/2)*self.duration
            distancey = ((staticvvel/2)*self.duration)+((-4.9*(duration**2))/2)
        if back == True:
            self.newx = ((self.ball_r.x)-distancex)
        else:
            self.newx = ((self.ball_r.x)+distancex)
        self.x.append(self.newx)
        self.newy = (self.ball_r.y-distancey)
        self.y.append(height-self.newy)
        self.ball_r2 = pygame.Rect(self.newx,self.newy,10,10)
        pygame.draw.rect(window,black,self.ball_r2)
        return self.x,self.y
    def collsion(self):
        self.stop = True
        self.first = True
        self.duration = 0
        self.ball_r.x = self.ball_r2.x
        self.ball_r.y = self.ball_r2.y-15
    def reset(self):
        self.duration = 0
        self.ball_r.x = 5
        self.ball_r2.y = height-110
        self.newx = self.ball_r.x
        self.newy = self.ball_r.y
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
        hdistance = round(lenx,2)
        vdistance = round(leny,2)
        return hdistance,vdistance
    def graphs(self,x,y):
        plt.plot(x,y)
        plt.savefig("graph.png")

def mainloop():
    run = True
    back = False
    c = Calculations()
    b = Ball()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c.graphs(x,y)
                run = False
        window.fill(white)
        mousex,mousey = b.controls()
        pygame.draw.rect(window,green,ground)
        pygame.draw.rect(window,white,collision)
        pygame.draw.rect(window,black,b.ball_r)
        pygame.draw.rect(window,black,b.ball_r2)
        pygame.draw.line(window,red,pygame.math.Vector2(b.ball_r2.x+10,b.ball_r2.y),pygame.math.Vector2(mousex,mousey),5)
        leny = height-((mousey+b.ball_r.y)-380)
        lenx = mousex-(b.ball_r.x+10)
        hdistance,vdistance = c.distance(lenx,leny)
        angle,back = c.angle(back,lenx,leny,b.ball_r)
        vvelocity,hvelocity = c.velocity(c.gravity,vdistance,hdistance,angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            b.reset()
        if keys[pygame.K_SPACE]:
            x,y = b.movement(vvelocity,hvelocity)
        if pygame.Rect.contains(ground,b.ball_r2):
            b.collision()
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

mainloop()