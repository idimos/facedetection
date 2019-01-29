import time
from gpiozero import DistanceSensor, Servo

# define pins
HCSR04_1_PIN_TRIG = 17
HCSR04_1_PIN_ECHO = 4
HCSR04_2_PIN_TRIG = 27
HCSR04_2_PIN_ECHO = 18
HCSR04_3_PIN_TRIG = 23
HCSR04_3_PIN_ECHO = 22
SERVO360_PIN_SIG = 24

ultrasonicLeft  = DistanceSensor(echo=4,trigger=17)
ultrasonicFront = DistanceSensor(echo=18,trigger=27)
ultrasonicRight = DistanceSensor(echo=22,trigger=23)