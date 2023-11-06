from pylab import *
from numpy import *
#https://www.tutorialspoint.com/modelling-the-projectile-motion-using-python
u=100

# Angle of projectile at start
α=radians(1)

# Elevation of starting point above the ground
y0=0

# Acceleration due to gravity
g=9.81

# Time of flight
a=g
b=-2*u*sin(α)
c=-2*y0

# coefficient array
coeff=array([a,b,c])

# finding roots
t1,t2=roots(coeff)
print(f"t1= {t1} and t2= {t2}")

# Maximum Height
# From the throwing point
h1=u**2*(sin(α))**2/(2*g)

# total
h_max=h1+y0
print(f"h_max= {round(h_max,3)} m")

# Range
R=u*cos(α)*max(t1,t2)
#max(t1,t2) will return the positive value

print(f"R= {round(R,3)} m")
# Figure name
figure(1, dpi=300)

# plotting y=0 line
plot([0,R],[0,0],'k',linewidth=1)

# Array of x
x=linspace(0,R,50)

# Evaluating y based on x
y=x*tan(α)-(1/2)*(g*x**2)/(u**2*(cos(α))**2 )

# Plotting projectile
plot(x,y,'r-',linewidth=2)
xlabel('x')
ylabel('y')
savefig("Inc_Proj.jpg")