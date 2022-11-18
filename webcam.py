import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("Cam Example")
img_counter = 0
arr = []

while True:
    ret, frame = cam.read()
    if not ret:
        print("Can't get frame")
        break
    cv2.imshow("I'm working...", frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        print("You've hit the Escape button, closing the app...")
        break
    elif k%256 == 32:
        img_name = "frame_{}.jpeg".format(img_counter)
        arr.append(frame)
        cv2.imwrite(img_name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        print("Screenshot taken")
        cv2.imshow("Picture_{}.".format(img_counter), arr[img_counter])
        img_counter += 1

cam.release()
cam.destroyAllWindows()