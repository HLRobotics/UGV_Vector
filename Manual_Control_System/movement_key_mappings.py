"""ugv_key_press_controls.py"""
from pynput import keyboard
from movement_engine import *


class KeyboarController:
    """Key board controller class"""

    def __init__(self):
        """initializing the class"""
        self.movementEngine = MovementEngine()

    def on_press(self, key):
        """key press action"""
        try:
            print("Alphanumeric key pressed: {0} ".format(key.char))
            if key.char == "w":
                self.movementEngine.move_forward()
            if key.char == "s":
                self.movementEngine.move_backward()
            if key.char == "a":
                self.movementEngine.move_left()
            if key.char == "d":
                self.movementEngine.move_right()
            if key.char == "x":
                self.movementEngine.stop()
            if key.char == "+":
                self.movementEngine.increase_speed()
            if key.char == "-":
                self.movementEngine.decrease_speed()
            if key.char == "i":
                self.movementEngine.control_base_servo_increase_angle()
            if key.char == "o":
                self.movementEngine.control_base_servo_decrease_angle()
            if key.char == "y":
                self.movementEngine.control_vertical_servo_increase_angle()
            if key.char == "u":
                self.movementEngine.control_vertical_servo_decrease_angle()

        except AttributeError:
            print("special key pressed: {0}".format(key))

    def on_release(self, key):
        """key release action"""
        print(" Key released: {0}".format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def start_listening(self):
        """start listening"""
        with keyboard.Listener(
            on_press=KeyboarController().on_press,
            on_release=KeyboarController().on_release,
        ) as listener:
            listener.join()
