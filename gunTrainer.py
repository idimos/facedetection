import cv2 as cv
import numpy as np
import urllib.request
import os

# Training positive images
def store_pos_images():
    images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03467984'
    images_urls = urllib.request.urlopen(images_link).read().decode()
    pic_num = 1
    if not os.path.exists('pos'):
        os.makedirs('pos')

    for i in images_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i,"pos/"+str(pic_num)+".jpg")
            img = cv.imread("pos/"+str(pic_num)+".jpg",cv.IMREAD_GRAYSCALE)
            resized_image = cv.resize(img,(50,50))
            cv.imwrite("pos/"+str(pic_num)+".jpg",resized_image)
            pic_num +=1
        except Exception as e:
            print( str(e))

# Training negative images
def store_negs_images():
    # Sport, Athletics Images
    images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    images_urls = urllib.request.urlopen(images_link).read().decode()
    pic_num = 1
    if not os.path.exists('negs'):
        os.makedirs('negs')

    for i in images_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i,"negs/"+str(pic_num)+".jpg")
            img = cv.imread("negs/"+str(pic_num)+".jpg",cv.IMREAD_GRAYSCALE)
            resized_image = cv.resize(img,(100,100))
            cv.imwrite("negs/"+str(pic_num)+".jpg",resized_image)
            pic_num +=1
        except Exception as e:
            print( str(e))

def find_uglies():
    match = False
    for file_type in ['pos']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv.imread('uglies/'+str(ugly))
                    question = cv.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

# store_negs_images()
find_uglies()