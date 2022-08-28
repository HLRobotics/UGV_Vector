"""image_processing_class"""
from cv2 import cv2
from image_processing_constants import *


class ImageProcessingHelper:
    """Image Processing Helper Class"""

    def open_ip_camera(self, ip_address):
        """open ip camera"""
        cap = cv2.VideoCapture(ip_address)
        while True:
            _, frame = cap.read()
            frame = cv2.resize(frame, (FRAME_RESIZE_X, FRAME_RESIZE_Y))
            cv2.imshow("Capturing", frame)
            if cv2.waitKey(1) & 0xFF == ord("x"):
                """close the application"""
                break
