import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(28, GPIO.IN)
GPIO.setup(21, GPIO.OUT)


GPIO.output(21, GPIO.input(28))

GPIO.cleanup()