"""EngineConstants.py"""

PROCESSED_IMG = "Processed_Image/color_body_source.jpg"
LOWER_RED = [0, 50, 50]
UPPER_RED = [10, 255, 255]
LOWER_GREEN = [40, 20, 50]
UPPER_GREEN = [90, 255, 255]
LOWER_BLUE = [100, 50, 50]
UPPER_BLUE = [130, 255, 255]
RESOLUTION = (1280, 1024)
RED = "Red"
BLUE = "Blue"
GREEN = "Green"

"""movement_constants"""
UGV_IP_ADDRESS = str(input("Enter the UGV IP Address: "))
UGV_DEFAULT_SPEED = 50
UGV_DEFAULT_ANGLE = 80
UGV_DEFAULT_PAN_ANGLE = 130
HLROBOTICS_TITLE = (
    "[************* HLRobotics and Software Automation 2023*************] \n "
)
UGV_CONTROL_SYSTEM_TITLE = "[ Autonomous Control System ]"
UGV_MAX_SPEED = 120
UGV_MIN_SPEED = 50
MAX_SPEED_MESSAGE = "[ Reached Maximum Speed ]"
MIN_SPEED_MESSAGE = "[ Reached Minimum Speed ]"
MAX_LIMIT_MESSAGE = "[ Reached the Maximum ]"
MIN_LIMIT_MESSAGE = "[ Reached the Minimum ]"
BASE_SERVO_ANGLE_LIST = []
SPEED_ESTIMATION_LIST = []

"""COMMON FUNCTIONALITY"""


def display_message(message):
    """display message"""
    print(message)
