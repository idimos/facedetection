from labmodules import logger
import speake3

class LabSound:
    '''This a class created on 25/1/2019 by Yannis for speaking purposes'''

    def __init__(self):
        try:
            logger.log.cout("Voice of Robot is setting up ...")
            self.engine = speake3.Speake() # Initialize the speake engine
            self.engine.set('voice', 'en-us')
            self.engine.set('speed', '130')
            self.engine.set('pitch', '30')
            logger.log.cout('... done!')
        except:
            logger.log.cout("Sound creation ERROR")

    def say(self, message):
        self.engine.say(message) #String to be spoken
        self.engine.talkback()
        
try:
    robotVoice
except:
    robotVoice = LabSound()
else:
    pass