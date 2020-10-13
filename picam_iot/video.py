
class image:
    """
    Manages all video operations. Allows recording and storage of videos, 
    setting up of camera video characteristics and interfacing videos with motion and face detection
    """
    def __init__(self):
        """
        Initializes the video manegement module 
        
        """
        pass
    
    def start(self):
        """ Start recording a video
        """
        pass

    def stop(self, storage = "local"):
        """Stops video recording and saves video file into the specified storage.

        :param storage: The target location of the video. Default is local
        :returns: A video file
        :rtype:  format specified
        
        """
        pass

    def record(self, duration = 15 , storage = "local"):
        """ Records a video with a specified duration and saves it to the specified storage.
        
        :param duration: Video duration in seconds. Default is 15 seconds.
        :param storage: target storage. Default is local.
        :returns: A video with the specified duration. 
        :rtype: format specified
        """
        pass

    def set_resolution(self, res = (1024, 768), width = 1024, height = 768 ):
        """ Sets the resolution of the videos
        :param res: A tupple with the resolution as (width, height). Default is (1024, 768)
        :param width: Sets the camera width to the provided width. Default is 1024 pixels.
        :param height: Sets camera heigh to the specified height. Default is 768.
        """
        pass

    def local_stream(self,motion = False, motion_save = False, storage = "local"):
        """ Records and display locally a continous stream.
        :param motion: Enables/disables motion detection.
        :param motion_save: Allows/Disallow streams where motion was detected to be saved to the specified storage.
        :param storage: Target storage to save streams. Default is local.

        """
        pass
    def network_stream(self, motion = False, motion_save = False):
        """ Records and display locally a continous stream to a network.
        :param motion: Enables/disables motion detection.
        :param motion_save: Allows/Disallow streams where motion was detected to be saved to the specified storage.

        """
        pass

    def motion_detect():
        """ Detects motion in a video stream.
        :returns: a flag to indicate the presence of motion within a video stream.
        :rtype: Boolean
        """
        pass

    def face_detect():
        """ Detects faces within a video stream
        :returns: a flag to indicate presence of a face
        :rtype: Boolean
        
        """
        pass

    def draw_box(self, frame, color = 'blue'):
        """ Draws a box around the specified frame
        :param frame: A tuple with frame to draw the box around
        """
        pass

