import RPi.GPIO as GPIO
import time

dac = [6, 12, 5, 0, 1, 7, 11, 8]
zero = [0, 0, 0, 0, 0, 0, 0, 0]
arr = [0, 0, 0, 0, 0, 0, 0, 0]

def num_to_bin(num):
    global arr
    num2 = bin(num)[2:]


    for i in range (len(num2), 8):
        num2 = '0' + num2

    print("num2: ", num2)

    for i in range(8):
        arr[i] = int(num2[7 - i]) - int('0')
    

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

nums = [255, 127, 64, 32, 5, 0]

for num in nums:
    num_to_bin(num)
    GPIO.output(dac, arr)
    time.sleep(20)
    GPIO.output(dac, zero)

