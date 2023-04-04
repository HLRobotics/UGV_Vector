"""ugv_controller_constants.py"""
UGV_IP_ADDRESS = str(input("Enter the UGV IP Address: "))
UGV_DEFAULT_SPEED = 50
FORWARD = "w"
BACKWARD = "s"
LEFT = "d"
RIGHT = "a"
STOP = "x"
HLROBOTICS_TITLE = (
    "[************* HLRobotics and Software Automation *************] \n "
)
UGV_CONTROL_SYSTEM_TITLE = "[UGV CONTROL SYSTEM]"
UGV_MAX_SPEED = 120
UGV_MIN_SPEED = 50
MAX_SPEED_MESSAGE = "[ Reached Maximum Speed ]"
MIN_SPEED_MESSAGE = "[ Reached Minimum Speed ]"

"""COMMON FUNCTIONALITY"""


def display_message(message):
    """display message"""
    print(message)
