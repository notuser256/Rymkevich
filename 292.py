from math import sin
from math import cos 
m=2
alf=30
u=0.3
g=10
f=(m*g*(sin(alf*3.14/180)+u*cos(alf*3.14/180)))/(cos(alf*3.14/180)-u*sin(alf*3.14/180))
print(f)