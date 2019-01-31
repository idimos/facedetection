from labmodules import sound
from labmodules import logger
import os

#sound.robotVoice.say("hello")

def loadProfiles():
    profilepath = 'labmodules/personsProfiles'
    print(os.listdir(profilepath))
    profileFiles = [os.path.join(profilepath,fn) for fn in os.listdir(profilepath)]
    logger.log.cout( profileFiles )

    for fn in profileFiles:
        f = open( fn, "r" )
        lines = [l for l in f.readlines()]
        for l in lines:
            print( l )
        f.close()
        
loadProfiles()