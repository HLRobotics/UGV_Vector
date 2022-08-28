"""ugv_console_controller_helper"""

from ugv_controller_constants import *
import requests
import time


class UGVControllerHelper:
    """UGV Controller Helper"""

    def __init__(self):
        self._ip_address = UGV_IP
        self.speed = UGV_DEFAULT_SPEED

    def url_generator(self, control):
        generated_url = "http://" + self._ip_address + control
        requests.post(generated_url)
        time.sleep(0.1)
        requests.post(self.speed)

    def move_forward(self):
        """move forward"""
        control = FORWARD
        self.url_generator(control)

    def move_backward(self):
        """move backward"""
        control = BACKWARD
        self.url_generator(control)

    def move_left(self):
        """move left"""
        control = LEFT
        self.url_generator(control)

    def move_right(self):
        """move right"""
        control = RIGHT
        self.url_generator(control)

    def stop(self):
        """stop  moving"""
        control = STOP
        self.url_generator(control)

    def increase_speed(self):
        """increase speed"""
        self.speed = self.speed + 10
        requests.post(self.speed)

    def decrease_speed(self):
        """decrease soeed"""
        self.speed = self.speed - 10
        requests.post(self.speed)
