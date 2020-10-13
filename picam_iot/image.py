
class image:
    """
    Manages all image operations. Allows capturing and storage of images, 
    setting up of camera image characteristics and interfacing images with face detection
    """
    def __init__(self):
        """
        Initializes the image manegement module 
        
        """
        pass
    
    def capture(self, name,  storage = "local"):
        """ 
        Captures and returns and image object.
        The image is saved to local storage by default but can be set to other storages.

        :param name: name of the image to be captured
        :param storage: specifies the storage platform for the image. can be (local, drive, mqtt). Default is local.
        :returns: An image object
        :rtype: jpg
        """
        pass

    def set_resolution(self, res = (1024, 768), width = 1024, height = 768 ):
        """ Sets the resolution of the images
        :param res: A tupple with the resolution as (width, height). Default is (1024, 768)
        :param width: Sets the camera width to the provided width. Default is 1024 pixels.
        :param height: Sets camera heigh to the specified height. Default is 768.
        """
    
    def face_capture(self, color = 'blue'):
        """ Captures an image and Draws a box around the frame with a face.
        :param color: The color of the box. Default is blue.
        """
        pass
    


    