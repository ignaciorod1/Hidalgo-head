    # 10 de Octubre
# Control del cuello implementando clases
# basado en el codigo de PAC9685.py y PAC4242.py de Mr. Zafra y Hermes

from __future__ import division
import time
import math
import Adafruit_PCA9685 as PCA  

f = 50      #frequency
pwm = PCA.PCA9685()
pwm.set_pwm_freq(f)
# Declaration of  classes

class Resolution:
    """Resolution of the servos Duty Cycle in ms"""
    def __init__(self, tmx, tmn):
        self.tmx = tmx
        self.tmn = tmn
        self.value = (self.tmx + self.tmn) / 2

    def min_ang(self):
        return 0
                            
    def max_ang(self):
        return (abs(self.tmx - self.tmn)*60)

    def updateVal(self, angle):
        if (self.tmn < self.tmx): 
            self.value = ((angle/60) + self.tmn )*(4096/20)
        else:
             self.value = (- (angle/60) + self.tmn )*(4096/20)
        
    def check(self):
        if self.value > self.tmx:
            self.value = self.tmx
            print("No es posible conseguir un valor superior")
            return False
            
        elif self.value < self.tmn:
            self.value = self.tmn
            print("No es posible conseguir un valor inferior")
            return False
        else:
                return True

    
class Servo:
    """class for the different servos"""

    def __init__(self, pin, name, tmx, tmn):
        self.name = name
        self.pin = pin
        self.name = name
        self.angle = 0
        self.res = Resolution(tmx, tmn)
    
    def showAngle(self):
        print (self.angle)
    
    def showName(self):
        print (self.name)

    def showVal(self):
        print(self.res.value)
        
    def move(self):
        pwm.set_pwm(self.pin, self.pin, int(self.res.value))
        
    def fkine(self, angle):
        if angle <= self.res.max_ang()  and angle >= 0: 
            self.res.updateVal(angle)
            self.angle = angle
            
        else:
            pass
    
########   Neck servos

alpha = Servo(0, "Alpha", 2.1, 1.1) 
bravo = Servo(1, "Bravo", 1.1, 2.1)
charlie = Servo(2, "Charlie", 0.7, 2.55)

######## Eye servos

L1 = Servo(15, "Lou1", 1.75, 2.05)
L2 = Servo(14, "Lou2", 1.1, 1.7)
R1 = Servo(12, "Ro1", 1.75, 2.05)
R2 = Servo(13, "Ro2 ", 1.1, 1.7)       #servo para prueba

def update_servos():    
        alpha.move()
        bravo.move()
        charlie.move()

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
        
        




