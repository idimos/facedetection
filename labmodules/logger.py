class Log:
    '''Labstem logger'''
    seq = 0

    def __init__(self,pfx):
        self.prefix = pfx

    def cout(self,msg):
        print('[{0} : {1}] {2}'.format(Log.seq, self.prefix,msg))
        Log.seq += 1

