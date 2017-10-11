# 10 de Octubre
# Control del cuello implementando clases
# basado en el codigo de PAC9685.py y PAC4242.py de Mr. Zafra

from __future__ import division
import time
import Adafruit_PCA9685 as PCA
from Tkinter import *
import random
import abc		#Abstract class module
from abc	import ABCMeta		

f = 50		#frequency
pwm = PCA.PCA9685()
pwm.set_pwm_freq(f)
# Declaration of  classes

class Resolution:
	"""Resolution of the servos Duty Cycle"""
	def __init__(self, mx, mn):
		self.max = mx
		self.min = mn
		self.value = (self.max + self.min) / 2
		
	def check(self):
		print("val:", self.value)
		if self.value > self.max:
			self.value = self.max
			print("No es posible conseguir un valor superior")
			
		elif self.value < self.min:
			self.value = self.min
			print("No es posible conseguir un valor inferior")

	
class Servo:
	"""Mother class for the different servos"""
	
	__metaclass__ = ABCMeta
	def __init__(self, pin, name):
		self.name = name
		self.pin = pin
		self.name = name
		self.position = 45
	
	def showPos(self):
		print (self.position)
	
	def showName(self):
		print (self.name)
		
	@abc.abstractmethod
	def move(self):
		pass
		

class MG15(Servo):	
	"""Class for the high torque servos 1501MG used for the neck movement
	'm' and 'n' are the parameters of the angle-pwm linear function, which are different for each object"""
	
	def __init__(self, pin, name, m, n):
		Servo.__init__(self, pin, name)
		self.res = 	Resolution(560, 100)
		self.m = m
		self.n = n			
		
	def move(self):
		pwm.set_pwm(self.pin, self.pin, self.position) 
		
	def pos(self, angle):
		if angle < 100 and angle > 20:
			self.position = self.m * angle + self.n
			self.res.value = self.pos 
			self.res.check()
		else:
			pass
		

class S3114:
	"""Class for the Futaba micro servos used in the eyes"""
	
	def __init__(self, pin, name):
		Servo.__init__(self, pin, name)
		self.res = 	Resolution(4096, 0)
	
	def move(self):
		pwm.set_pwm(self.pin, self.pin, self.pos) 

alpha = MG15(0, "Alpha", -3, 540) 
bravo = MG15(1, "Bravo", 3, 100)
charile = MG15(2, "Charlie", -3, 540)


def update_servos():
	
	a = input("Test value for alpha")
	alpha.pos(a)
	alpha.move()
	bravo.move()
	charlie.move()

#root.after(50, update_servos)

a = input("Test value for alpha")
b = input("Test value for bravo")
alpha.pos(a)
bravo.pos(b)
alpha.move()
bravo.move()



"""
root = Tk()
frame = Frame(root)
frame.pack()

root.after(1000, update_servos)
root.mainloop()


"""

