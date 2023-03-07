import RPi.GPIO as GPIO
import time


class raspberry:

        def startBlinking(self):

                GPIO.setmode(GPIO.BCM)
                GPIO.setup(24, GPIO.OUT)

                for x in range(1, 10):
                        GPIO.output(24, GPIO.HIGH)
                        time.sleep(2)
                        GPIO.output(24, GPIO.LOW)
                        time.sleep(2)


                GPIO.cleanup()




