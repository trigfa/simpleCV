from SimpleCV import Camera, Display, Image
import time


# initialise the camera
cam=Camera()

# initialise the display
display=Display()

# snap a picture using the camera
img = cam.getImage()

# show some text
img.drawText("Hello World")
# show n the display
img.save(display)
time.sleep(5)