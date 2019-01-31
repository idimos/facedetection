import time
from labmodules import terminator
from labmodules import logger
# from labmodules import distanceSensors

def main():
    try:
        logger.log.cout('Powering on the Robot!')
        robot = terminator.Terminator('trainer/trainer.yml','Cascades/haarcascade_frontalface_default.xml')
        #robot.greetings()
        robot.run()
    except:
        logger.log.cout("Initialasation error")

if __name__ == "__main__":
    main()

