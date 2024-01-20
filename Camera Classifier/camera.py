import cv2 as cv

class Camera :
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Camera didn't opeed")
        
    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            ret , frame =self.camera.read()

            if ret:
                return(ret,cv.cvtColor(frame,cv.COLOR_BGR2RGB))
            
            else:
                return(ret,net)
            
        else :
            return None