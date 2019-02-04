import time
from labmodules import terminator
from labmodules import logger

def main():
    try:
        logger.log.cout('Powering on the Robot!')
        robot = terminator.Terminator('trainer/trainer.yml','Cascades/haarcascade_frontalface_default.xml',0)
        robot.greetings()
        robot.run()
    except Exception as e:
        logger.log.cout("Initialasation error [{0}]".format(e))

if __name__ == "__main__":
    main()

