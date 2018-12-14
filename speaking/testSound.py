import os
import keyboard
import pyttsx3

def speakfile(fn):
    global engine
    f = open(fn,"r")
    lines = [l for l in f.readlines()]
    for l in lines:
        keyboard.write(l)
        engine.say(l)
        engine.runAndWait()
    f.close()

engine = pyttsx3.init()
path = 'textFiles'
textfiles = [os.path.join(path,f) for f in os.listdir(path)]

while (True):
    try: #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):#if key 'q' is pressed
            break#finishing the loop
        elif keyboard.is_pressed('l'):
            speakfile(os.path.join(path,'toLeft.txt'))
        elif keyboard.is_pressed('r'):
            speakfile( os.path.join(path,'toRight.txt'))
        elif keyboard.is_pressed('y'):
            speakfile( os.path.join(path,'john.txt'))
        elif keyboard.is_pressed( 'a' ):
            for f in textfiles:
                speakfile( f )
        else:
            print()
    except:
        break #if user pressed a key other than the given key the loop will break


