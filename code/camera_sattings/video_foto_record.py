import cv2
from datetime import datetime, timedelta
import numpy as np

date = datetime.today().strftime('%d-%m-%Y %H-%M')


def photo():
    global date
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
        ret, frame = videoCaptureObject.read()
        cv2.imwrite(f"D:/download/git/assistent_bot/photo/foto_{str(date)}.jpg", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def video():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f"D:/download/git/assistent_bot/videos/video_{str(date)}.avi",fourcc ,60.0, (1920, 1080))
    result = True
    while result:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow(f"D:/download/git/assistent_bot/videos/video_{str(date)}.avi", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): result = False
    cap.release()
    out.release()
    cv2.destroyAllWindows()


video()

def clear_photo_video_folder():
    date_now = datetime.today().strftime('%d-%m-%Y %H-%M')


