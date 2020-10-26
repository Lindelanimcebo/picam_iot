import os.path
from os import path

class storage:
    """ A class to manage storage functionality.
    """
    def __init__(self, local = "./"):
        """ Initializes the storage menagement class

        :param local: sets the target local storage. Default is the working directory
        
        """
        self.local = local
    
    def get_local(self):
        return self.local
    
    def set_local(self, local):

        if (path.exists(local)):
            self.local = local
        else:
            raise Exception("path {} does not exist.".format(local))