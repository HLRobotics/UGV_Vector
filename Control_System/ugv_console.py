"""ugv_console.py"""
from ugv_controller_constants import *
from ugv_key_press_controls import *


class UGVConsole:
    """UGV Console Class"""

    def __init__(self):
        """initializing"""
        self.controller_helper = UGVControllerHelper()
        self.ugv_key = KeyboarController()

    def load_welcome_note(self):
        """load welcome note"""
        print(HLROBOTICS_TITLE)
        print(UGV_CONTROL_SYSTEM_TITLE)

    def activate_console(self):
        """activate console"""
        self.load_welcome_note()
        self.ugv_key.start_listening()


if __name__ == "__main__":
    trigger = UGVConsole()
    trigger.activate_console()
    while True:
        if len(UGV_IP_ADDRESS) > 0:
            from ugv_controller_helper import *

            break
