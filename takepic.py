import picamera
import datetime as dt
import time

"""
Takes a picture, annotates with the timestamp and saves it to a
file. The filename is returned.
"""
def takepic(filename = None, dirname = None):
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.hflip = True
    camera.exif_tags['IFD0.Artist'] = 'Utpal\'s Pi!'
    timenow = dt.datetime.now()
    camera.annotate_text = timenow.strftime('%Y-%m-%d %H:%M:%S')
    if filename == None:
        filename = timenow.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
    if dirname != None:
        filename = dirname + filename
    time.sleep(2)
    camera.capture(filename)
    camera.close()
    return filename
