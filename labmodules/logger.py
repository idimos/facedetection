import time

class Log:
    '''Labstem logger'''
    seq = 0

    def cout(self,msg):
        print('[{0} - {1}] {2}'.format(Log.seq, time.asctime( time.localtime(time.time()) ),msg))
        Log.seq += 1

log = Log()