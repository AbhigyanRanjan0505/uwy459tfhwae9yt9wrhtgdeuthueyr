import cv2
import time
import numpy

four_cc = cv2.VideoWriter_fourcc(*"XVID")
output_file = cv2.VideoWriter("output.avi", four_cc, 20.0, (640, 480))
cap = cv2.VideoCapture(0)

for i in range(60):
    ret, bg = cap.read()

bg = numpy.flip(bg, axis=1)

video = cv2.VideoCapture(0)
image = cv2.imread("bg.jpg")

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    frame = numpy.flip(frame, axis=1)

    upper_black = numpy.array([104, 153, 70])
    lower_black = numpy.array([30, 30, 0])

    mask = cv2.inRange(frame, lower_black, upper_black)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    result = frame - res
    result = numpy.where(result == 0, image, result)

    cv2.imshow("Magic", result)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
