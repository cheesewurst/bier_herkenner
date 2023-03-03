import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

cam = cv2.VideoCapture(1) 

while True:
    ret, frame = cam.read()

    bbox, label, conf = cv.detect_common_objects(frame)
    output_frame = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Object detector", output_frame)

    key = cv2.waitKey(1)
    if key == ord('q') or cv2.getWindowProperty('Object detector', cv2.WND_PROP_VISIBLE) < 1:
        break

cam.release()
cv2.destroyAllWindows() 