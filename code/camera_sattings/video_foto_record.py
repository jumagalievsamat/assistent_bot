import cv2
from datetime import datetime, timedelta

date = datetime.today().strftime('%d/%m/%Y %H:%M')
def foto():
    global date
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
        ret, frame = videoCaptureObject.read()
        cv2.imwrite(f"D:/download/git/assistent_bot/videos/{date}.jpg", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
