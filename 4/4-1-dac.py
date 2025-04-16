import RPi.GPIO as GPIO

GPIO.setwarnings(False)

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

try:
    while True:
        num = input("enter num 0-255: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                num_to_bin(num)
                GPIO.output(dac, arr)
                voltage = float(num) / 256 * 3.3
                print(f"voltage: {voltage} V")
            elif num < 0:
                print("error, num < 0")
            else:
                print("error, num > 255")
        except Exception:
            if num == "q": break
            print("error, input need to be num")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("the end")

