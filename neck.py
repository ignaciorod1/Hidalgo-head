# 19 de Febrero, Ignacio Rodriguez
# Control del cuello y los okos de Hidalgo

from __future__ import division
import time
import math
import servo
import Adafruit_PCA9685 as PCA

f = 50      #frequency in Hz
pwm = PCA.PCA9685()
pwm.set_pwm_freq(f)
    
########   Neck servos

alpha = Servo(0, "Alpha", 220, 425) #down, top middle = 
bravo = Servo(1, "Bravo", 400, 230) #down, top
charlie = Servo(2, "Charlie", 550, 120) #left, right

######## Eye servos

L1 = Servo(11, "Lou1", 200, 271)  #right, left
L2 = Servo(10, "Lou2", 200, 283)  #bottom, top
R1 = Servo(9, "Ro1", 409, 491)   #right, left
R2 = Servo(8, "Ro2 ", 345, 438)  #bottom, top

def update_servos():    
        alpha.move()
        bravo.move()
        charlie.move()
        R1.move()
        L1.move()
        R2.move()
        L2.move()

while True:
        a = int(input("Percentage of Pitch: "))
        b = int(input("Percentage of Yaw: "))
        
        angle1 = (a/100) * alpha.res.max_ang()
        angle2 = (b/100) * charlie.res.max_ang()
        
        alpha.fkine(angle1)
        bravo.fkine(angle1)
        charlie.fkine(angle2)
        
        print ("Angulos: ")
        print("Alpha: " )
        alpha.showVal()
        print("Bravo: " )
        bravo.showVal()
        print("Charlie: ")
        charlie.showVal()

        update_servos()
        
        




