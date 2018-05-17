from SimpleCV import Color,Camera,Display
import requests
import datetime

cam = Camera()  # Starts the camera
display = Display() 

while display.isNotDone():
  img = cam.getImage()  # Gets image from the camera
  
  barcode = img.findBarcode()  # Finds barcode data from image
  if barcode is not None:  # If there is some data processed
    barcode = barcode[0]
    result = barcode.data
    date = str(datetime.date.today())
    now = datetime.datetime.now()
    time = now.hour * 60 + now.minute;
    barcode = []  # Reset barcode data to empty set
    
    faces = img.findHaarFeatures("facetrack-training.xml") # Load in trained face file
    if faces:
      faces.draw()
      faces[-1].crop().save(result + ".jpg")
            
    data = {'id': result, 'date': date, 'time': time, 'password': 'password'}
    r = requests.post('https://ep-web-interface-js0mmer.c9users.io/api/post.php', data=data)
  img.save(display)  # Shows the image on the screen
# This is the tutorial: https://technoobsite.wordpress.com/2016/02/02/raspberry-pi-barcode-scanner/
# Face recognition derived from https://gist.github.com/rishimukherjee/2220293
# Face tracking xml file comes from https://github.com/mmwanga/facetracking