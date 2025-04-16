import RPi.GPIO as GPIO
import time


dac = [6, 12, 5, 0, 1, 7, 11, 8]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

arr = [0, 0, 0, 0, 0, 0, 0, 0]

def num_to_bin(num):
    global arr
    num2 = bin(num)[2:]


    for i in range (len(num2), 8):
        num2 = '0' + num2

    for i in range(8):
        arr[i] = int(num2[7 - i]) - int('0')

do_inc = 1
x = 0

try:
    period = float(input("input period: "))
    while True:
        num_to_bin(x)
        GPIO.output(dac, arr)
        print(bin(x))

        if x == 255: do_inc = 0
        if x == 0:   do_inc = 1

        if do_inc: x += 1
        else:      x -= 1

        time.sleep(period/1024)

except Exception:
    print("error period value")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("the end")
