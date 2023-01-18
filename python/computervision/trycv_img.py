import cv2

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('wednesday.png')
# img = cv2.imread('classpic.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cords = face_data.detectMultiScale(gray_img)

for (x, y, w, h) in face_cords:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Sample image', img)
cv2.waitKey()

print('Tapos na')