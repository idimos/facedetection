from labmodules import logger
from labmodules import sound

class Terminator:
    '''The robot created by LabSTEM called Terminator'''
    log = logger.Log(__name__)

    def __init__(self):
        try:
            self.log.cout("Terminator creation starting...")
            self.mouth = sound.LabSound()
        except:
            self.log.cout("creation ERROR")
        finally:
            self.log.cout("Terminator has created succesfully!!!")
            self.log.cout("... is up and running")

    def greetings(self):
        self.mouth.say("Hello ladies and gentlement!")
        self.mouth.say("My name is TERMINATOR and I have been created by LabSTEM robotics")

    def run(self):
        while True:
            self.log.cout("run")