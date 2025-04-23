import RPi.GPIO as GPIO
from time import *

dac = [6, 12, 5, 0, 1, 7, 11, 8]
leds = [9, 10, 22, 27, 17, 4, 3, 2]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

arr = [0, 0, 0, 0, 0, 0, 0, 0]

def num_to_bin(num):
    global arr
    num2 = bin(num)[2:]


    for i in range (len(num2), 8):
        num2 = '0' + num2

    for i in range(8):
        arr[i] = int(num2[7 - i]) - int('0')

def adc():
    n = 0
    for i in range(7, -1, -1):
        n += 2**i
        num_to_bin(n)
        GPIO.output(dac, arr)
        sleep(0.01)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            n -= 2**i
    return n

def volume(val):
    val = int(val/256*10)
    arr = [0]*8
    for i in range(val - 1):
        arr[i] = 1
    return arr
    

try:
    while True:
        adc_val = adc()
        if adc_val: 
            volume_val = volume(adc_val)
            GPIO.output(leds, volume_val)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("END")