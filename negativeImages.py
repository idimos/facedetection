import urllib.request
import cv2
import numpy as np  
import os

def store_raw_images():
    #http://image-net.org/api/text/imagenet.synset.geturls?wnid=n 00523513
    #http: // image - net.org / api / text / imagenet.synset.geturls?wnid = n03493792
    #Blender
    # http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02830157
    #Cutting
    # http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03154446
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    neg_image_urls = urllib.request.urlopen( neg_images_link ).read().decode()
    pic_num = 119

    if not os.path.exists( 'neg' ):
        os.makedirs( 'neg' )

    for i in neg_image_urls.split( '\n' ):
        try:
            print( i )
            urllib.request.urlretrieve( i, "neg/" + str( pic_num ) + ".jpg" )
            img = cv2.imread( "neg/" + str( pic_num ) + ".jpg", cv2.IMREAD_GRAYSCALE )
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize( img, (100, 100) )
            cv2.imwrite( "neg/" + str( pic_num ) + ".jpg", resized_image )
            pic_num += 1

        except Exception as e:
            print( str( e ) )


def create_pos_n_neg():
    for file_type in ['neg']:

        for img in os.listdir( file_type ):

            if file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open( 'info.dat', 'a' ) as f:
                    f.write( line )
            elif file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open( 'bg.txt', 'a' ) as f:
                    f.write( line )

#create_pos_n_neg()

if __name__ == "__main__":
    store_raw_images()