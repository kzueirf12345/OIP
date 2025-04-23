import RPi.GPIO as GPIO
from time import *

dac = [6, 12, 5, 0, 1, 7, 11, 8]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
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
    

try:
    while True:
        adc_val = adc()
        voltage = adc_val * 3.3 / 256.0
        if adc_val: 
            print(f"voltage: {voltage:.4f}")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("END")