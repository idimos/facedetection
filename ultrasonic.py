from time import sleep
from gpiozero import DistanceSensor,Servo
import pyttsx3

# define pins
HCSR04_1_PIN_TRIG = 4
HCSR04_1_PIN_ECHO = 17
HCSR04_2_PIN_TRIG = 27
HCSR04_2_PIN_ECHO = 18
HCSR04_3_PIN_TRIG = 23
HCSR04_3_PIN_ECHO = 22
SERVO360_PIN_SIG = 25

ultrasonicLeft  = DistanceSensor(echo = HCSR04_1_PIN_ECHO, trigger = HCSR04_1_PIN_TRIG)
ultrasonicFront = DistanceSensor(echo = HCSR04_2_PIN_ECHO, trigger = HCSR04_2_PIN_TRIG)
#ultrasonicRight = DistanceSensor(echo = HCSR04_3_PIN_ECHO, trigger = HCSR04_3_PIN_TRIG)

myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

servo = Servo(SERVO360_PIN_SIG,min_pulse_width=minPW,max_pulse_width=maxPW)

engine = pyttsx3.init()

def turnLeft():
    print("Turn Left")
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.max()
    print("max")
    
def turnFront():
    print("Turn Front")
    engine.say("Turn Front")
    engine.runAndWait()
    

print("Terminator project")
engine.say("Turn Front")
engine.runAndWait()
ultrasonicLeft.when_in_range = turnLeft
ultrasonicLeft.when_out_of_range = turnFront


