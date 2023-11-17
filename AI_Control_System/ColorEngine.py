"""ColorEngine.py"""
import cv2
import numpy as np
from EngineConstants import *


class ColorEngine:
    """Color Engine"""

    def process_selected_image(self):
        """Process selected image"""
        input_img = cv2.imread(PROCESSED_IMG)
        img = cv2.resize(input_img, RESOLUTION)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # define range of red color in HSV
        lower_red = np.array(LOWER_RED)
        upper_red = np.array(UPPER_RED)

        # define range of green color in HSV
        lower_green = np.array(LOWER_GREEN)
        upper_green = np.array(UPPER_GREEN)

        # define range of blue color in HSV
        lower_blue = np.array(LOWER_BLUE)
        upper_blue = np.array(UPPER_BLUE)

        # create a mask for red color
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        # create a mask for green color
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        # create a mask for blue color
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        # find contours in the red mask
        contours_red, _ = cv2.findContours(
            mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        # find contours in the green mask
        contours_green, _ = cv2.findContours(
            mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        # find contours in the blue mask
        contours_blue, _ = cv2.findContours(
            mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        # loop through the red contours and draw a rectangle around them

        cv2.line(img, (2, 300), (1276, 300), (0, 0, 255), 2)
        cv2.line(img, (18, 1), (18, 1024), (255, 255, 0), 2)
        cv2.line(img, (1143, 1), (1143, 1024), (255, 255, 0), 2)

        status = False
        # loop through the blue contours and draw a rectangle around them
        for cnt in contours_blue:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(
                    img,
                    BLUE,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (255, 0, 0),
                    2,
                )
                cx, cy = self.calculate_cendroid(x, y, w, h)
                cv2.circle(img, (cx, cy), 1, (0, 0, 255), 2)
                if cy > 300 and cx > 75 and cx < 1151:
                    print("cx:", str(cx), "cy:", str(cy))

                    """logic below"""

        # loop through the green contours and draw a rectangle around them
        for cnt in contours_green:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    img,
                    GREEN,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                )
                cx, cy = self.calculate_cendroid(x, y, w, h)
                cv2.circle(img, (cx, cy), 1, (0, 0, 255), 2)
                if cy > 300 and cx > 75 and cx < 1151:
                    print("cx:", str(cx), "cy:", str(cy))

                    """logic below"""

        for cnt in contours_red:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(
                    img,
                    RED,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    2,
                )
                cx, cy = self.calculate_cendroid(x, y, w, h)
                cv2.circle(img, (cx, cy), 1, (0, 0, 255), 2)
                if cy > 300 and cx > 75 and cx < 1151:
                    print("cx:", str(cx), "cy:", str(cy))

                    """logic below"""
