##radius, height, and orientation angles (x, y, z).
##These parameters describe a cylinder who's coordinate is the center point
##of the base of the cylinder. The function must calculate and return the
##center coordinate of the other face. 

##vol=pi*(r^2)*h
##pi and r are constant, h is variable and at center of 
##triple integrate to find new values for h

from scipy import integrate

f = (x, y, z)       ##function to integrate
[x1 = lambda y, z   ##lower boundary for x
x2 = lambda y, z    ##upper boundary for x
y1 = lambda z       ##lower boundary for y
y2 = lambda z       ##upper boundary for y
z1 = 0
z2 = 2*pi] 

integral = integrate.tplquad(f, z1, z2, y1, y2, x1, x2)
print(integral)

##so i can work more on this but in the meantime my C is rusty 
##and I'm having trouble getting the "grammar" of python correct 
##to get the coordinate of the opposing face of the cylinder
