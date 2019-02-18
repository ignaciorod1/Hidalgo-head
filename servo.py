#servo class

class Servo:
    """class for the different servos"""

    def __init__(self, pin, name, mn, mx):
        self.name = name
        self.pin = pin
        self.pos = 0		
        self.minPos = mn 	# min pos in 12 bits range
        self.maxPos = mx 	# max pos in 12 bits range
    
    def showPos(self):
        print (self.pos)
    
    def showName(self):
        print (self.name)

    def showVal(self):
        print(self.res.value)

    def move(self):
        pwm.set_pwm(self.pin, self.pin, self.pos)

    def setPos(self, pos):
        if pos <= self.maxPos and pos >= self.minPos:
            self.pos = pos
            
        else:
            pass