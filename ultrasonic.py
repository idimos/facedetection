from time import sleep
from gpiozero import DistanceSensor,Servo
import pyttsx3

# define pins
HCSR04_1_PIN_TRIG = 17
HCSR04_1_PIN_ECHO = 4
HCSR04_2_PIN_TRIG = 27
HCSR04_2_PIN_ECHO = 18
HCSR04_3_PIN_TRIG = 6
HCSR04_3_PIN_ECHO = 5
SERVO360_PIN_SIG = 24

ultrasonicLeft  = DistanceSensor(echo = HCSR04_1_PIN_ECHO, trigger = HCSR04_1_PIN_TRIG,threshold_distance=0.2,max_distance=1)
ultrasonicFront = DistanceSensor(echo = HCSR04_2_PIN_ECHO, trigger = HCSR04_2_PIN_TRIG)
#ultrasonicRight = DistanceSensor(echo = HCSR04_3_PIN_ECHO, trigger = HCSR04_3_PIN_TRIG)

myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

servo = Servo(SERVO360_PIN_SIG,min_pulse_width=minPW,max_pulse_width=maxPW)

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


def main():
    i=1
    while True:
        try:
            print('Left Sensor {0:.3f}'.format(ultrasonicLeft.distance * 100))
            if (ultrasonicLeft.distance < 0.3):
                print("Turn Left")
                engine.say("Turn Left")
                engine.runAndWait()
                sleep(2)
            print('Front Sensor {0:.3f}'.format(ultrasonicFront.distance * 100))
            #print('Right Sensor {0:.3f}'.format(ultrasonicRight.distance * 100))
            print("{0} ================================================".format(i))
            i+=1
            sleep(1)
        except KeyboardInterrupt:
            print("Interupted")
            exit(0)


            
if __name__ == "__main__":
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say("Project is starting")
    engine.runAndWait()
    main()


