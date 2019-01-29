import pyttsx3
from labmodules import logger

class LabSound:
    '''This a class created on 25/1/2019 by Yannis for speaking purposes'''

    def __init__(self):
        try:
            logger.log.cout("Sound setting up")
            self.engine = pyttsx3.init()
            voices = self.engine.getProperty( 'voices' )  # getting details of current voice
            self.engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            self.engine.setProperty('rate',125)
            rate = self.engine.getProperty( 'rate' )
            logger.log.cout('... speach rate: {0}'.format(rate))
            self.engine.setProperty('volume',1.0)
            logger.log.cout('... volume: {0}'.format(self.engine.getProperty('volume')))
        except:
            logger.log.cout("Sound creation ERROR")

    def say(self, message):
        self.engine.say(message)
        self.engine.runAndWait()
