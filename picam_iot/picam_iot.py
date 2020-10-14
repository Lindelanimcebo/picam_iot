from picamera import PiCamera
import time

class picam_iot:
    """Main module."""

    def __init__(self):
        """ Initialises the camera object, opencv and provide these to all subclasses where necessary
        """