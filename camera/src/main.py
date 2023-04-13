import asyncio
import cv2
import numpy as np
from moving_average import moving_average

lower = np.array([15, 150, 20])
upper = np.array([35, 255, 255])
average = 0
prevAverage = 0
cam = cv2.VideoCapture(1) 

def get_average():
    return average

async def timer(seconds):
    global prevAverage
    while True:
        await asyncio.sleep(seconds)
        print("timer reset")
        newAverage = int(get_average())
        if newAverage != 0 and newAverage != prevAverage:
            prevAverage = newAverage
            print(f'new value: {newAverage}')

async def run_async_timer():
    while True:
        task = asyncio.create_task(timer(1))
        await task

async def main():
    asyncio.create_task(run_async_timer())

    while True:
        await asyncio.sleep(0) # Allow other tasks to run

        objects_detected = 0
        success, frame = cam.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(image, lower, upper)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    objects_detected += 1
                    cv2.putText(frame, f'{objects_detected}', (x + 1, y - 6), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

        global average
        average = moving_average(objects_detected)

        cv2.imshow("Geel herkenner", frame)

        key = cv2.waitKey(1)
        if key == ord('q') or cv2.getWindowProperty('Geel herkenner', cv2.WND_PROP_VISIBLE) < 1:
            break

    cam.release()
    cv2.destroyAllWindows()

asyncio.run(main())
