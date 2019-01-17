import os
"""
The last step is we need to create the descriptor file for these negative images
"""

def create_neg_descriptor():

    for img in os.listdir( 'neg' ):
        line = 'neg' + '/' + img + '\n'
        with open( 'bg.txt', 'a' ) as f:
            f.write( line )

if __name__ == "__main__":
    create_neg_descriptor()