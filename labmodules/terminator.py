from labmodules import logger
from labmodules import sound
from labmodules.videocaptureasync import VideoCaptureAsync
import cv2, time, os

class Terminator:
    '''The robot created by LabSTEM called Terminator'''

    def salute(self,p):
        logger.log.cout(self.profiles[p]['name'])
        sound.robotVoice.say('Hello mister {0} {1}'.format(self.profiles[p]['name'],self.profiles[p]['surname']))
        sound.robotVoice.say('You are a {0} and you are {1} years old'.format(self.profiles[p]['job'],self.profiles[p]['age']))
        sound.robotVoice.say('Your favourit team is {0} and you live at {1}'.format(self.profiles[p]['team'],self.profiles[p]['city']))
        
    def loadProfiles(self):
        try:
            self.profilepath = 'labmodules/personsProfiles'
            self.profileFiles = [os.path.join(self.profilepath,fn) for fn in os.listdir(self.profilepath)]
            logger.log.cout('loading profiles from {0}'.format(self.profilepath ))

            for fn in self.profileFiles:
                f = open( fn, "r" )
                self.lines = [l.rstrip() for l in f.readlines()]
                self.profileInfo = dict()
                
                for ln in self.lines:
                    dd = ln.split('#')
                    self.profileInfo[dd[0]] = [x for x in dd[1:]]
                self.profiles[os.path.splitext(os.path.basename(fn))[0]] = self.profileInfo
        except:
            logger.log.cout("loading profiles error")
        else:
            logger.log.cout("Profiles loaded succesfully!")
            
    def personExists(self,p):
        '''True, if person p exists into profiles Dictionary'''
        if p in self.profiles:
            return True
        else:
            return False
        
    def __init__(self,ymlPath,facecascadeXML,src=0):
        try:
            msg = "Robot is initialising, please wait!"
            logger.log.cout(msg)
            sound.robotVoice.say(msg)
            
            self.profiles = dict()
            self.loadProfiles()
            
            self.recognizer = cv2.face.LBPHFaceRecognizer_create()
            self.recognizer.read(ymlPath )
            logger.log.cout( " ... Recognizer ok" )
            
            cascadePath = facecascadeXML
            self.faceCascade = cv2.CascadeClassifier( cascadePath )
            logger.log.cout( " ... FaceCascade ok" )
            
            self.font = cv2.FONT_HERSHEY_SIMPLEX
            # iniciate id counter
            self.id = 0
            # names related to ids: example ==> Yannis: id=1,  etc
            self.names = ['None', 'Yannis', 'George','Miltiades','Socrates','Stefanos']
            # Initialize and start realtime video capture
            self.cam = VideoCaptureAsync( src )
            #self.cam.set( 3, 640 )  # set video widht
            #self.cam.set( 4, 480 )  # set video height
            self.cam.start()
            logger.log.cout(" ... Camera ok")
            # Define min window size to be recognized as a face
            self.minW = 0.1 * self.cam.cap.get( 3 )
            self.minH = 0.1 * self.cam.cap.get( 4 )
        except Exception as e:
            logger.log.cout("Robot Creation ERROR [{0}]".format(e))
            exit(1)

    def greetings(self):
        '''Greeting message from Robot '''
        logger.log.cout("Greetings from Robot")
        sound.robotVoice.say("Hello ladies and gentlement!")
        time.sleep(0.5)
        sound.robotVoice.say("My name is Terinator and I have been created by LabSTEM robotics")

    def run(self):
        try:
            while True:
                _, img = self.cam.read()
                img = cv2.flip( img, 1 )  # Flip vertically
                gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

                self.faces = self.faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(int( self.minW ), int( self.minH )),
                )
                for (x, y, w, h) in self.faces:
                    cv2.rectangle( gray, (x, y), (x + w, y + h), (0, 255, 0), 2 )
                    self.id, self.confidence = self.recognizer.predict( gray[y:y + h, x:x + w] )
                    # Check if confidence is less them 100 ==> "0" is perfect match
                    if (self.confidence < 100):
                        self.id = self.names[self.id]
                        self.confidence = "  {0}%".format( round( 100 - self.confidence ) )
                        
                        if self.personExists(self.id):
                            self.salute(self.id)
                            #print('I found {0}'.format(self.id))
                            
                    else:
                        self.id = "unknown"
                        self.confidence = "  {0}%".format( round( 100 - self.confidence ) )

                    logger.log.cout( "Robot captured face of [{0}]".format(self.id) )
                    cv2.putText( img, str( self.id ), (x + 5, y - 5), self.font, 1, (255, 255, 255), 2 )
                    cv2.putText( img, str( self.confidence ), (x + 5, y + h - 5), self.font, 1, (255, 255, 0), 1 )
                cv2.putText( img, "LabSTEM Robotics", (10, int( self.cam.cap.get( 4 ) ) - 15), self.font, 1, (255, 255, 255), 2 )

                cv2.imshow( 'LabSTEM Robotics, Terminator camera', img )
                k = cv2.waitKey( 1 ) & 0xff  # Press 'ESC' for exiting video
                if k == 27:
                    break
        except Exception as e:
            logger.log.cout("[ERROR] camera capturing [{0}]".format(e))
        finally:
            self.cam.stop()
            cv2.destroyAllWindows()