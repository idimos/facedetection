import pyttsx3
from labmodules import logger

class LabSound:
    '''This a class created on 25/1/2019 by Yannis for speaking purposes'''
    log = logger.Log( __name__ )

    def __init__(self):
        try:
            self.engine = pyttsx3.init()
            voices = self.engine.getProperty( 'voices' )  # getting details of current voice
            self.engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            self.engine.setProperty('rate',125)
            rate = self.engine.getProperty( 'rate' )
            self.log.cout('Current speach rate is {0}'.format(rate))
            self.engine.setProperty('volume',1.0)
            self.log.cout('Current volume is {0}'.format(self.engine.getProperty('volume')))
            self.log.cout("Sound object created succesfully!")
        except:
            self.log.cout("Sound creation ERROR")

    def say(self, message):
        self.engine.say(message)
        self.engine.runAndWait()
