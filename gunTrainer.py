import cv2 as cv
import numpy as np
import urllib.request
import os

# Training positive images
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