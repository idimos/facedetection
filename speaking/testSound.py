import os,time, keyword
import pyttsx3

def speakfile(fn):
    global engine
    f = open(fn,"r")
    lines = [l for l in f.readlines()]
    print(lines)
    for l in lines:
        print(l)
        engine.say(l)
        engine.runAndWait()
    f.close()
def onStart(name):
    print('starting',name)

engine = pyttsx3.init()
engine.connect('finished-utterance',onStart)
path = 'textFiles'
textfiles = [os.path.join(path,f) for f in os.listdir(path)]

while (True):

    try: #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):#if key 'q' is pressed
            print('You Pressed A Key!')
            break#finishing the loop
        else:
            pass
    except:
        break #if user pressed a key other than the given key the loop will break

for f in textfiles:
    speakfile(f)
