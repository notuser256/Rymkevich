from math import sin
from math import cos
v_0=40
a=60
g=10
h_m=round(pow(v_0*sin(a*3.14/180),2)/(2*g))
print(h_m)
l=round(2*pow(v_0,2)*sin(a*3.14/180)*cos(a*3.14/180)/g)
print(l)
