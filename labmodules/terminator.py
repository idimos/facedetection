from labmodules import logger
from labmodules import sound
import cv2, time,os

class Terminator:
    '''The robot created by LabSTEM called Terminator'''

    # def SaySomething(id):
    #     global engine
    #     path = 'speaking/textFiles'
    #     textfiles = [os.path.join( path, fl ) for fl in os.listdir( path )]
    #     facename = os.path.join( path, id + ".txt" )
    #     print( facename )
    #     for fl in textfiles:
    #         if fl == facename:
    #             f = open( facename, "r" )
    #             lines = [l for l in f.readlines()]
    #
    #             for l in lines:
    #                 print( l )
    #                 engine.say( l )
    #                 engine.runAndWait()
    #             f.close()
    #
    # def loadProfiles(self):
    #     profilepath = 'personsProfiles'
    #     # print(os.listdir(self.path))
    #     self.profileFiles = [os.path.join(profilepath,fn) for fn in os.listdir(profilepath)]
    #     logger.log.cout( self.profileFiles )

        # for fn in self.profileFiles:
        #     f = open( fn, "r" )
        #     self.lines = [l for l in f.readlines()]
        #     # for l in self.lines:
        #     #     print( l )
        #     f.close()

    def __init__(self,ymlPath,facecascadeXML):
        try:
            # self.loadProfiles()
            logger.log.cout("Robot building ... wait")
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
            self.names = ['None', 'Yannis', 'George', 'Zoe', 'Mirto', 'Miltiades', 'Socrates']
            # Initialize and start realtime video capture
            self.cam = cv2.VideoCapture( 0 )
            self.cam.set( 3, 640 )  # set video widht
            self.cam.set( 4, 480 )  # set video height
            logger.log.cout(" ... Camera ok")
            # Define min window size to be recognized as a face
            self.minW = 0.1 * self.cam.get( 3 )
            self.minH = 0.1 * self.cam.get( 4 )

            self.mouth = sound.LabSound()
            logger.log.cout(" ... Speaking ok")
        except:
            logger.log.cout("creation ERROR")
            exit(1)

    def greetings(self):
        self.mouth.say("Hello ladies and gentlement!")
        time.sleep(1)
        self.mouth.say("My name is TERMINATOR and I have been created by LabSTEM robotics")

    def run(self):
        try:
            while True:
                ret, img = self.cam.read()
                img = cv2.flip( img, 1 )  # Flip vertically
                gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

                self.faces = self.faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(int( self.minW ), int( self.minH )),
                )
                for (x, y, w, h) in self.faces:
                    cv2.rectangle( img, (x, y), (x + w, y + h), (0, 255, 0), 2 )
                    self.id, self.confidence = self.recognizer.predict( gray[y:y + h, x:x + w] )
                    # Check if confidence is less them 100 ==> "0" is perfect match
                    if (self.confidence < 100):
                        self.id = self.names[self.id]

                        self.confidence = "  {0}%".format( round( 100 - self.confidence ) )
                    else:
                        self.id = "unknown"
                        self.confidence = "  {0}%".format( round( 100 - self.confidence ) )

                    logger.log.cout( "Robot captured [{0}]".format(self.id) )
                    cv2.putText( img, str( self.id ), (x + 5, y - 5), self.font, 1, (255, 255, 255), 2 )
                    cv2.putText( img, str( self.confidence ), (x + 5, y + h - 5), self.font, 1, (255, 255, 0), 1 )
                cv2.putText( img, "LabSTEM Robotics", (10, int( self.cam.get( 4 ) ) - 15), self.font, 1, (255, 255, 255), 2 )

                cv2.imshow( 'LabSTEM Robotics camera', img )
                k = cv2.waitKey( 10 ) & 0xff  # Press 'ESC' for exiting video
                if k == 27:
                    break
        except:
            logger.log.cout("[ERROR] camera capturing ")
        finally:
            self.cam.release()
            cv2.destroyAllWindows()