 # programa para encontrar el rango de pwm de funcionamiento de los servos


import Adafruit_PCA9685 as PCA
import time

test = PCA.PCA9685()
test.set_pwm_freq(50)

def s(s1):
    return int(s1*(4096/20))

while True:
    for i in range(s(1.1), s(2.1), 1):
        test.set_pwm(0, 0, i)
        time.sleep(0.001)
    for k in range(s(2.1), s(1.1), -1):
        test.set_pwm(0,0, k)
        time.sleep(0.001)
    
#servos MG1501
#   0.5-2.75ms
#servos S3114
#   1-2.5 ms

