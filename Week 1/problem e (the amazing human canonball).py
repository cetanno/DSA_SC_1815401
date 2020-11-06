import math

n = int(input())
for i in range(n):
    v,theta,x,h1,h2 = map(float,input().split())
    rad = theta * math.pi / 180
    t = x/(v* math.cos(rad))
    h = v * t * math.sin(rad) - (9.81 * pow(t,2) / 2)
    # print (h)
    if h > h1 + 1 and h < h2 - 1:
        print ("Safe")
    else:
        print ("Not Safe")

