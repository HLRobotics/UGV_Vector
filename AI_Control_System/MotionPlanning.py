"""MotionPlanning.py"""

from EngineConstants import *


class MotionPlanning:
    """Motion Planning"""

    def __init__(self):
        self.ipAddress = UGV_IP_ADDRESS
        self.speed = UGV_DEFAULT_SPEED
        self.defaultAngle = UGV_DEFAULT_ANGLE
        self.defaultPanAngle = UGV_DEFAULT_PAN_ANGLE
        self.baseServoAngleData = BASE_SERVO_ANGLE_LIST
        self.speedEstimationMap = SPEED_ESTIMATION_LIST
        for angle in range(0, 190, 10):
            self.baseServoAngleData.append(angle)
