from __future__ import division
import time
import Adafruit_PCA9685 as PCA
from Tkinter import *
import random

# Configure min and max servo pulse lengths
servo1 = 0
servo2 = 1
servoJaw = 2
servo2_pos = 350
servo1_pos = 250
servo_min = 101 # Min pulse length out of 4096
servo_max = 540  # Max pulse length out of 4096
top = 100
bottom = 60
f = 50

random_flag = False

pwm = PCA.PCA9685()

root = Tk()
frame = Frame(root)
frame.pack()

hor_slider_value = IntVar()
hor_slider_value.set(50)
ver_slider_value = IntVar()
ver_slider_value.set(50)

bottomframe = Frame(root, height = 50, width = 40)
bottomframe.pack( side = BOTTOM )

def toggle_random():
	global random_flag	
	random_flag = not random_flag
	
	if(random_flag):
		print("RANDOM MODE ENGAGED")
	else:
			print("RANDOM MODE DISENGAGED")


def MIN(): 	
	 pwm.set_pwm(servoJaw, servoJaw, servo_min)
	 
def MAX():
	 pwm.set_pwm(servoJaw, servoJaw, servo_max) 
	 
def turn(angle):
	pwm.set_pwm(servoJaw, servoJaw, int(angle))
	 
pwm.set_pwm_freq(f)

pwm.set_pwm(servo2, servo2, servo2_pos) 
pwm.set_pwm(servo1, servo1, servo1_pos)
    
def up(angle1, angle2):
	pwm.set_pwm(servo2, servo2, int(23/9*angle1 + 100))
	pwm.set_pwm(servo1, servo1, int(-3*angle2 + 540))


def update_servos():

	if(random_flag):
		
		#Random angles
		rand_ver = random.randint(bottom, top)
		up(rand_ver, rand_ver)
		rand_hor = random.randint(servo_min, servo_max)
		turn(rand_hor)
		
		#Random update frequency
		rand_frec  = random.randint(200, 3000)
		#print(rand_ver, rand_hor, rand_frec)
		root.after(rand_frec, update_servos)
		
	else:
		#Vertical update
		ver = bottom + (bottom - top) * ver_slider_value.get() / 100
		up(ver, ver)
	
		#Horizontal update
		hor = servo_min + (servo_max - servo_min) * hor_slider_value.get() / 100 
		turn(hor)
	
		#Update frequency
		root.after(50, update_servos)
 
aButton = Button(frame, justify = LEFT, text = "MAX", fg = "green", command = MIN, padx = 40, pady = 10)
aButton.pack(fill = BOTH, expand = 1)

hButton = Button(frame,  justify = LEFT, text = "MIN", fg = "green", command = MAX, padx = 40, pady = 10)
hButton.pack(fill = BOTH, expand = 1)

xButton = Button(frame,  justify = LEFT, text = "UP", fg = "green", command = lambda:  up(120, 120), padx = 40, pady = 10)
xButton.pack(fill = BOTH, expand = 1)

aButton = Button(frame,  justify = LEFT, text = "DOWN", fg = "green", command = lambda:  up(80, 80), padx = 40, pady = 10)
aButton.pack(fill = BOTH, expand = 1)

sliderV = Scale(root, from_ = 100, to= 0, orient=VERTICAL, variable = ver_slider_value)
sliderV.pack()

sliderH = Scale(root, from_ = 0, to=100, orient=HORIZONTAL, variable = hor_slider_value)
sliderH.pack()

randomButton = Button(frame,  justify = LEFT, text = "RANDOM MODE", fg = "blue", command = lambda:  toggle_random(), padx = 40, pady = 10)
randomButton.pack(fill = BOTH, expand = 1)

root.after(1000, update_servos)
root.mainloop()







