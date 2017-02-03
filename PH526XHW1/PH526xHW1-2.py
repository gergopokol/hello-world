import math

print(math.pi/4.)

import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   return(random.uniform(-1,1))

print(rand())

def distance(x, y):
   return(math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2))

x=(0,0)
y=(1,1)

print(distance(x,y))

random.seed(1)

def in_circle(x, origin = [0]*2):
   if distance(x,origin) < 1:
       return True
   else:
       return False

x=(1,1)

print(in_circle(x))

R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    inside.append(in_circle(point))

print(inside.count(True)/R)

print(math.pi/4-inside.count(True)/R)