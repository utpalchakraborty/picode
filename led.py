import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'


GPIO.setmode(GPIO.BCM) ## Use GPIO pin numbering.

class LED():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)


    def ledon(self):
        GPIO.output(self.pin, True)

    def ledoff(self):
        GPIO.output(self.pin, False)

    def blink(self, numtimes = 1, pause = 1):
        self.ledoff()
        for i in range(0, numtimes):
            self.ledon()
            time.sleep(pause)
            self.ledoff()
            time.sleep(pause)
            
        
if __name__ == '__main__':
    pin1 = 12
    pin2 = 16
    led1 = LED(pin1)
    led2 = LED(pin2)
    led1.ledon();
    led2.blink(10, .5)
    led1.ledoff();
    GPIO.cleanup()
