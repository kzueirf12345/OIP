import RPi.GPIO as GPIO
import time


leds = [9, 10, 22, 27, 17, 4, 3, 2]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(aux, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))