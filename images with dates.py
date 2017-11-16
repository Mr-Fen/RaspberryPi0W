from picamera import PiCamera
from time import sleep
from datetime import datetime

now = datetime.now()
print("{0:%H}:{0:%M} {0:%a} {0:%d}-{0:%b}-{0:%y}".format(now))

camera = PiCamera()
camera.annotate_text = ("{0:%H}:{0:%M} {0:%a} {0:%d}-{0:%b}-{0:%y}".format(now))
camera.resolution = (1920, 1080)
camera.framerate = 15
camera.start_preview()
for i in range(3):
  sleep(3)
  camera.capture('/home/pi/Pictures/image%03d.jpg' % i)
camera.stop_preview()
               
