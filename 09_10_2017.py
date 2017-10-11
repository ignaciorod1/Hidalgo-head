# 10 de Octubre
# Control del cuello implementando clases
# basado en el codigo de PAC9685.py y PAC4242.py de Mr. Zafra

from __future__ import division
import time
import Adafruit_PCA9685 as PCA
from Tkinter import *
import random

f = 50		#frequency

# Declaration of  classes

class Resolution:
	"""Resolution of the servos Duty Cycle"""
	def __init__(self, mx, mn):
		self.max = mx
		self.min = mn
	
class Servo:
	"""Mother class for the different servos"""
	def __init__(self, pin, name):
		self.name = name
		self.pin = pin
		self.name = name
	
	def showPos(self):
		print (self.pos)
	
	def showName(self):
		print (self.name)
		

class MG15(Servo):	
	"""Class for the high torque servos 1501MG used for the neck movement"""
	
	def __init__(self, pin, name):
		Servo.__init__(self, pin, name)
		self.res = 	Resolution(560, 100)

class S3114:
	"""Class for the Futaba micro servos used in the eyes"""
	
	def __init__(self, pin, name):
		Servo.__init__(self, pin, name)
		self.res = 	Resolution(4096, 0)
	
def update_servos():

	#Vertical update
	ver = bottom + (bottom - top) * ver_slider_value.get() / 100
	up(ver, ver)
			#Horizontal update
	hor = servo_min + (servo_max - servo_min) * hor_slider_value.get() / 100 
	turn(hor)
			#Update frequency
	root.after(50, update_servos)
	
	
alpha, bravo, charlie = MG15(0, "Alpha"), MG15(1, "Bravo"), MG15(2, "Charlie")

pwm = PCA.PCA9685()
pwm.set_pwm_freq(f)

root = Tk()
frame = Frame(root)
frame.pack()

sliderV = Scale(root, from_ = 100, to= 0, orient=VERTICAL, variable = ver_slider_value)
sliderV.pack()

sliderH = Scale(root, from_ = 0, to=100, orient=HORIZONTAL, variable = hor_slider_value)
sliderH.pack()
	
root.after(1000, update_servos)
root.mainloop()




