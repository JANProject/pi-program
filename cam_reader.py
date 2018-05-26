from SimpleCV import Color,Camera,Display
from picamera import PiCamera
from picamera.array import PiRGBArray
import requests
import datetime

cam = PiCamera()  # Starts the camera
display = Display()
rawCapture = PiRGBArray(cam, size=(640, 480))

while display.isNotDone():
  for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    img = frame.array
  
    barcode = img.findBarcode()  # Finds barcode data from image
    if barcode is not None:  # If there is some data processed
      barcode = barcode[0]
      result = barcode.data
      date = str(datetime.date.today())
      now = datetime.datetime.now()
      time = now.hour * 60 + now.minute;
      barcode = []  # Reset barcode data to empty set
  
      data = {'id': result, 'date': date, 'time': time, 'password': 'password'}
      r = requests.post('https://lavatory-logger-js0mmer.c9users.io/post', data=data)
      print r.text
    img.save(display)  # Shows the image on the screen
# This is the tutorial: https://technoobsite.wordpress.com/2016/02/02/raspberry-pi-barcode-scanner/