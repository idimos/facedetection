import time
from labmodules import terminator
from labmodules import logger
# from labmodules import distanceSensors

log = logger.Log(__name__)

def main():
    try:
        log.cout('Powering on the Robot!')
        robot = terminator.Terminator()
        robot.greetings()
        robot.run()
    except:
        log.cout("Initialasation error")

if __name__ == "__main__":
    main()

