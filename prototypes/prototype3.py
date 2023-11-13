import math
import matplotlib.pyplot as plt

g = 9.81
v = 30
k = 0.05
angle = 30
t = [0]
dt = 0.1
i = 0
vmag = [0]

vx = [v*math.cos(angle/180*math.pi)]
vy = [v*math.sin(angle/180*math.pi)]
f = k*v**2
ax = [-(f*math.cos(angle/180*math.pi))]
ay = [-g-(f*math.sin(angle/180*math.pi))]

while i < 10:
    t.append(t[i]+dt)
    vx.append(vx[i]+dt*ax[i])
    vy.append(vy[i]+dt*ay[i])
    vmag.append(math.sqrt(vx[i+1]**2+vy[i+1]**2))
    f = k * vmag[i]**2
    ax.append(-(f*math.cos(angle/180*math.pi)))
    ay.append(-g-(f*math.sin(angle/180*math.pi)))
    i+=1

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(t,vx)
ax2.plot(t,vy)
fig.savefig("3.png")