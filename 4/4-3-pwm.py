import RPi.GPIO as GPIO

shim = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(shim, GPIO.OUT)

p = GPIO.PWM(shim, 1000)
p.start(0)

try:
    while True:
        duty = int(input("input duty: "))

        if duty < 0:
            print("duty < 0")
        elif duty > 100:
            print("duty > 100")
        else:
            p.ChangeDutyCycle(duty)
            print(3.3*duty/100)

except Exception:
    print("error duty val")

finally:
    p.stop()
    GPIO.output(shim, 0)
    GPIO.cleanup()
    print("the end")