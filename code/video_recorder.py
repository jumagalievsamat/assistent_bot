from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.common.exceptions import InvalidSessionIdException
import cv2
import numpy as np
import threading


class Record:
    def __init__(self, obj, file_name="video", size=(1920, 1080), flags=cv2.IMREAD_COLOR):
        self.obj = obj
        self.flags = flags
        self.size = size
        self.file_name = file_name
        self.recording = False
        self.lock = threading.Lock()
        self.thread = None
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        initial_frame = self.get_frame()
        if initial_frame is not None:
            self.out = cv2.VideoWriter(f"{self.file_name}.mp4", fourcc, 8.0, self.size)
        else:
            raise ValueError("Unable to capture the initial frame.")

    def get_frame(self):
        if self.obj is None:
            return None
        try:
            if isinstance(self.obj, (WebDriver, RemoteWebDriver)):
                current_window_handle = self.obj.current_window_handle
                self.obj.switch_to.window(current_window_handle)
                im_arr = np.frombuffer(self.obj.get_screenshot_as_png(), dtype=np.uint8)
                frame = cv2.imdecode(im_arr, flags=self.flags)
                return frame
            else:
                raise ValueError(f"Unsupported object type: {type(self.obj)}")
        except InvalidSessionIdException:
            self.obj = None
        except Exception as e:
            print(f"Error capturing frame: {e}")
            return None

    def capture(self):
        frame = self.get_frame()
        if frame is not None:
            frame = cv2.resize(frame, self.size)
            with self.lock:
                self.out.write(frame)
        return frame

    def save(self):
        with self.lock:
            self.out.release()

    def start(self):
        self.recording = True
        self.thread = threading.Thread(target=self.record, daemon=True)
        self.thread.start()

    def stop(self):
        self.recording = False
        # self.thread.join()
        self.save()

    def record(self):
        while self.recording:
            if self.obj is None:
                self.stop()
                break
            else:
                frame = self.get_frame()
                if frame is None:
                    self.stop()
                    break
                else:
                    self.capture()
