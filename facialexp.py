
# face emotion detection in live camera

def faceexp(frame):

    import cv2
    import json

    # You sould install the deep face library
    #pip install deepface
    # this code was tested in Python 3.8
    from deepface import DeepFace

    # You can download the file 'haarcascade_frontalface_default.xml'
    # from cv2 Git hub
    face_cascade = cv2.CascadeClassifier("C:/Users/karee/kkkk/haarcascade_frontalface_default.xml")

    result = DeepFace.analyze(img_path = frame , actions=['emotion'], enforce_detection=False )

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    if result[0]["dominant_emotion"][:] == 'sad' or result[0]["dominant_emotion"][:] == 'angry' or result[0]["dominant_emotion"][:] == 'fear': 
        return False
    else:
        return True 

#faceexp()