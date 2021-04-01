from math import ceil
m=0.6
t=10
h=35/100
C=100
q=29*pow(10,6)
r=2.3*pow(10,6)
c=4190
u=3.33*pow(10,-5)
t_v=(m*c+C)*(100-t)/(h*u*q)
t_v=round(t_v/60)
print(t_v,"минут")
m1= h*u*q/r*1000
print(m1)
