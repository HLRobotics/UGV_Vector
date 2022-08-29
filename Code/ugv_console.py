"""ugv_console.py"""
from ugv_controller_constants import *
from ugv_controller_helper import *
from ugv_key_press_controls import *


class UGVConsole:
    """UGV Console Class"""

    def __init__(self):
        """initializing"""
        self.controller_helper = UGVControllerHelper()
        self.ugv_key = KeyboarController()

    def load_welcome_note(self):
        print(HLROBOTICS_TITLE)
        print(UGV_CONTROL_SYSTEM_TITLE)

    def activate_console(self):
        """activate console"""
        self.load_welcome_note()
        self.ugv_key.start_listening()


trigger = UGVConsole()
trigger.activate_console()
