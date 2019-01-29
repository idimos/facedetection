import pyttsx3
import time, os
import keyboard, random

def fileToSound(filename,person):
    f = open(filename)
    textlines = [line for line in f.readlines()]
    for line in textlines:
        engine.say( line+person)
        engine.runAndWait()
        time.sleep(0.5)
def speakFiles(path):
    allfiles = [ os.path.join(path,f) for f in os.listdir(path)]
    for f in allfiles:
        print(f)
        fileToSound(f)
        time.sleep(1)

engine = pyttsx3.init()
l, r, f = 0,0,0
persons = [' George',' Socrates',' Miltiades',' Yannis']
pathToLeft = 'textToVoice/left/'
pathToRight = 'textToVoice/right/'
pathToFront = 'textToVoice/front/'
while (True):
    if keyboard.is_pressed('r'):
        r += 1
        k = random.randint(0,3)
        fileToSound(pathToRight+str(r)+'.txt',persons[k])
    elif keyboard.is_pressed('l'):
        l += 1
        k = random.randint(0,3)
        fileToSound(pathToLeft+str(l)+'.txt',persons[k])
    elif keyboard.is_pressed('q'):
        breakpoint()
    else:
        pass
