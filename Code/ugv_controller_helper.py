"""ugv_console_controller_helper"""
from ugv_controller_constants import *
import requests
import time


class UGVControllerHelper:
    """UGV Controller Helper"""

    def __init__(self):
        """initializing the repository"""
        self._ip_address = input("Enter the IP address: ")
        self.speed = UGV_DEFAULT_SPEED

    def url_generator(self, control):
        try:
            generated_url = "http://" + self._ip_address + "/" + str(control)
            requests.get(generated_url)
        except:
            pass

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
        if self.speed <= 120:
            self.speed = self.speed + 10
            print("velocity => ", self.speed)
            self.url_generator(self.speed)
        else:
            display_message(MAX_SPEED_MESSAGE)

    def decrease_speed(self):
        """decrease seed"""
        if self.speed <= 0:
            self.speed = self.speed - 10
            print("velocity => ", self.speed)
            self.url_generator(self.speed)
        else:
            display_message(MIN_SPEED_MESSAGE)
