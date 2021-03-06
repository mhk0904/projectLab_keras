from idna import valid_contextj
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2 as cv
import speech_recognition as sr 
from gtts import gTTS 
import os 
import time 
import playsound 
from threading import Thread
from multiprocessing import Process, Queue

def speak(text):
    tts = gTTS(lang='en', text=text ) #ko')
    filename='voice.mp3' 
    tts.save(filename) 
    playsound.playsound(filename) 

# Load the model
def object_detect(result):
    model = load_model('C:/Users/Owner/Downloads/keras_model.h5')     # \\

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
#image = Image.open('D:\\vsc_ws_voice_learning\\converted_keras/test.jpg')
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
    # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
    # Our operations on the frame come here
            image1 = cv.resize(frame, size, interpolation=cv.INTER_AREA)
            image_array = np.asarray(image1)
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            data[0] = normalized_image_array
       
            prediction = model.predict(data)
    #print(prediction[0])
            cv.imshow('frame', image1)
            if (prediction[0][0] > 0.7):
                result.put("mask")
                #speak('mask')
     # Display the resulting frame
    
            if cv.waitKey(1) == ord('q'):
                break
            # cap.release()
            # cv.destroyAllWindows()
# When everything done, release the capture

if __name__ == "__main__":
    result = Queue()
    th1 = Thread(target= object_detect,args=(result))
    th1.start()
    th1.join()    
    
    while(True):
        tmp = result.get() 
        speak(tmp)




