import cv2
import time

class QrScanner:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        self.cam.set(5, 50)
        self.cam.set(6, 50)

        self.camera = True

    def run_scan(self):
        while self.camera:
            self.success, self.frame = self.cam.read()
            self.data, self.one, _ = self.detector.detectAndDecode(self.frame)
            if self.data:
                self.value = self.data
                self.camera = False
                break
            cv2.imshow("QR_scanner, ENTRANCE/EXIT (PRESS <SPACEBAR> TO FORCE CLOSE)", self.frame)
            if cv2.waitKey(1) == ord(' '):
                cv2.destroyAllWindows()
                break
        try:
            self.value_list = self.value.split(',')
            self.value_list.append(self.get_time())
            # print(self.value_list)
        except AttributeError:
            pass

    def get_value_list(self):
        return self.value_list

    def release_cam(self):
        self.cam.release()
        cv2.destroyAllWindows()

    def get_time(self):
        self.time = time.strftime('%I:%M:%S %p')
        return self.time











