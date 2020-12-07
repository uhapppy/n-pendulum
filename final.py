import pygame
import math
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)


screen=pygame.display.set_mode((1000,920))


g=0.1
angle=10
theta=math.radians(angle) 
thetaspeed=0
n=7
lenght=400
lenghtpendulum=lenght/n
pendulum=[]
arondpendulum=[]
pendulumspeed=[]
l=[[500,400]]
time=1

#pendulum=[posx,posy,vitesse_angle,angle]




def update():
    global theta
    global thetaspeed
    global lenghtpendulum
    global time
    for i in range(0,len(pendulum)):
        if i==0:
            acceleration_angle=(-g/lenghtpendulum)*(pendulum[i][0]/lenghtpendulum)
            pendulum[i][2]+=acceleration_angle*time
            pendulum[i][3]+=pendulum[i][2]*time
            pendulum[i][0]=lenghtpendulum*math.sin(pendulum[i][3])
            pendulum[i][1]=lenghtpendulum*math.cos(pendulum[i][3])   

        else:
            acceleration_angle=(-g/lenghtpendulum)*((pendulum[i][0]-pendulum[i-1][0])/lenghtpendulum)
            pendulum[i][2]+=acceleration_angle*time
            pendulum[i][3]+=pendulum[i][2]*time

            pendulum[i][0]=lenghtpendulum*math.sin(pendulum[i][3])+pendulum[i-1][0]
            pendulum[i][1]=lenghtpendulum*math.cos(pendulum[i][3])+pendulum[i-1][1]
        
            

    updatearound()

def updatearound():
        for i in range(0,len(pendulum)):
            arondpendulum[i][0]=round(pendulum[i][0]+500)
            arondpendulum[i][1]=round(pendulum[i][1]+400)


def convert(angle):
    theta=math.radians(90-angle)
    return angle


#position intiale
for i in range(1,n+1):
    pendulum.append([math.cos(theta)*i*lenghtpendulum,math.sin(theta)*i*lenghtpendulum,0,theta])
for i in range(len(pendulum)):
    arondpendulum.append([round(pendulum[i][0]+500),round(pendulum[i][1]+400)])

print(len(pendulum))






while True:
    pygame.time.delay(10)
    #pygame.display.update()
    for event in pygame.event.get():
        pass
    pygame.display.update()
    screen.fill(white)
    pygame.draw.line(screen,red,[500,0],[500,920])
    pygame.draw.line(screen,blue,[0,400],[1000,400])
    pygame.draw.lines(screen,black,False,(l+arondpendulum),3)
    for i in range(len(pendulum)):
          pygame.draw.circle(screen,green,arondpendulum[i],round(lenghtpendulum*0.07))
    update()
