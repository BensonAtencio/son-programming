import cv2

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)# 1 pag naka on droid cam

while True:
    _, frame = cam.read()
    
    gray_cam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cords = face_data.detectMultiScale(gray_cam)

    for (x, y, w, h) in face_cords:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'({x}, {y})', (x - 10, y - 10), font, .5,(0,255,0),1,cv2.LINE_AA)

    cv2.imshow('Live Video', frame)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()