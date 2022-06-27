class MyImage(object):
    def __init__(self):
         self._image = None
      
    # getter method
    def get_image(self):
        return self._image
      
    # setter method
    def set_image(self, image):
        self._image = image
