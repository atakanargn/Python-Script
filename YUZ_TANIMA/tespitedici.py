import cv2
from flask_opencv_streamer.streamer import Streamer

port = 8080
require_login = False
streamer = Streamer(port, require_login)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/atakan/DESKTOP/Python Projeler/YUZ_TANIMA/training/trainer.yml')
cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = '/home/atakan//DESKTOP/Python Projeler/YUZ_TANIMA/yuzverileri/'

cam = cv2.VideoCapture(0)

while True:
    ret, im =cam.read()
    im = cv2.flip(im, 1)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)

    for(x,y,w,h) in faces:
        
        tahminEdilenKisi, conf = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        
        if (tahminEdilenKisi == 0):
            tahminEdilenKisi = 'Atakan'
        elif (tahminEdilenKisi == 1):
            tahminEdilenKisi = 'Aydın'
        else:
            tahminEdilenKisi= "Bilinmeyen kişi"
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontColor = (255, 255, 255)
        cv2.putText(im, str(tahminEdilenKisi), (x, y + h), fontFace, fontScale, fontColor)
        cv2.imshow('im',im)
        cv2.waitKey(1)
    streamer.update_frame(im)

    if not streamer.is_streaming:
        streamer.start_streaming()

    cv2.imshow('im',im)
    cv2.waitKey(10)







