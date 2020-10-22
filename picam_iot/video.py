from picamera import PiCamera
from picamera.array import PiRGBArray
import datetime
import imutils
import cv2
import numpy as np
from time import sleep
from storage import storage

class video:
    """
    Manages all video operations. Allows recording and storage of videos, 
    setting up of camera video characteristics and interfacing videos with motion and face detection
    """
    def __init__(self, local = "./"):
        """
        Initializes the video manegement module 
        
        """
        self.local = local
        self.camera = PiCamera()
        self.storage = storage()
        self.storage.set_local(local)

    def start(self, name):
        """ Start recording a video

        :param name: name and extension of the video
        """
        self.camera.start_preview()
        self.camera.start_recording(self.storage.get_local() + name)

    def stop(self):
        """Stops video recording and saves video file into the specified storage.

        :returns: A video file
        :rtype:  format specified
        
        """
        self.camera.stop_recording()
        self.camera.stop_preview()

    def record(self, name,duration = 15 , storage = "local"):
        """ Records a video with a specified duration and saves it to the specified storage.
        
        :param duration: Video duration in seconds. Default is 15 seconds.
        :param storage: target storage. Default is local.
        :returns: A video with the specified duration. 
        :rtype: format specified
        """
        if self.camera._check_camera_open():
            self.stop()
        self.start(name)
        sleep(duration)
        self.stop()

    def set_resolution(self, res = (1024, 768), width = 1024, height = 768 ):
        """ Sets the resolution of the videos
        :param res: A tupple with the resolution as (width, height). Default is (1024, 768)
        :param width: Sets the camera width to the provided width. Default is 1024 pixels.
        :param height: Sets camera heigh to the specified height. Default is 768.
        """
        self.camera.resolution = res

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

    def motion_detect(self, images = False, videos = False):
        """ Detects motion in a video stream.
        :returns: a flag to indicate the presence of motion within a video stream.
        :rtype: Boolean
        """
        self.camera.framerate = 16
        raw = PiRGBArray(self.camera)
        sleep(1)

        avg_frame = None
        lastCheck = datetime.datetime.now()
        motion = False
        img_count = 0
        video_count = 0
        motion_count = 0

        motion_frames = []

        for capture in self.camera.capture_continuous(raw, format="bgr", use_video_port=True):

            frame = capture.array
            timestamp = datetime.datetime.now()
            motion = False
            
            frame = imutils.resize(frame, width=500)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

            if avg_frame is None:
                avg_frame = gray_frame.copy().astype("float")
                raw.truncate(0)
                continue
            
            cv2.accumulateWeighted(gray_frame, avg_frame, 0.5)
            frame_difference = cv2.absdiff(gray_frame, cv2.convertScaleAbs(avg_frame))
            
            threshold = cv2.threshold(frame_difference, 5, 255, cv2.THRESH_BINARY)[1]
            threshold = cv2.dilate(threshold, None, iterations=2)
            contours = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)

            for contour in contours:

                if cv2.contourArea(contour) < 5000:
                    continue
                
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
                motion = True
            
            ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
            cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 0, 0), 1)
            
            if motion:

                motion_count += 1

                if (images):
                    if (timestamp - lastCheck).seconds >= 5:
                        img_count += 1
                        cv2.imwrite(self.local + "motion" + str(img_count) + ".jpg", gray_frame)

                        motion_count = 0
                        lastCheck = timestamp
                if (videos):
                    motion_frames.append(frame)

            else:
                if self.frames_to_video(motion_frames, name = "video" + str(video_count+1) ):
                    video_count +=1
                    motion_frames = []
                motion_count = 0
            
            raw.truncate(0)
    
    def frames_to_video(self,frames = [], name = "video", video_type = ".avi"):

        if len(frames) < 1:
            return False
        print("making video")
        h, w, l = frames[0].shape
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        video = cv2.VideoWriter(self.local + name + video_type, fourcc, 16, (h,w))

        for i in range(len(frames)):
            video.write(frames[i])

        video.release()
        print("video saved")

        return True


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