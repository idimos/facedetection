from labmodules import sound
from labmodules import logger

msg = "Terminator is on"
logger.log.cout(msg)
sound.robotVoice.say(msg)

