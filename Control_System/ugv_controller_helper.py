"""ugv_console_controller_helper"""
from ugv_controller_constants import *
import requests
import time


class UGVControllerHelper:
    """UGV Controller Helper"""

    def __init__(self):
        """initializing the repository"""
        self._ip_address = UGV_IP_ADDRESS
        self.speed = UGV_DEFAULT_SPEED
        self.default_angle = UGV_DEFAULT_ANGLE

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
        if self.speed >= 0:
            self.speed = self.speed - 10
            print("velocity => ", self.speed)
            self.url_generator(self.speed)
        else:
            display_message(MIN_SPEED_MESSAGE)

    def control_base_servo_increase_angle(self):
        """control base servo increase angle"""
        self.default_angle = self.default_angle + 10
        print(self.default_angle)
        self.url_generator("B" + str(self.default_angle))

    def control_base_servo_decrease_angle(self):
        """control base servo increase angle"""
        self.default_angle = self.default_angle - 10
        print(self.default_angle)
        self.url_generator("B" + str(self.default_angle))

    def control_vertical_servo_increase_angle(self):
        """control base servo increase angle"""
        self.default_angle = self.default_angle + 10
        print(self.default_angle)
        self.url_generator("P" + str(self.default_angle))

    def control_vertical_servo_decrease_angle(self):
        """control base servo increase angle"""
        self.default_angle = self.default_angle - 10
        print(self.default_angle)
        self.url_generator("P" + str(self.default_angle))
