import time
import picamera
import picamera.array

width = 100
height = 75
threshold = 25
sensitivity = 25

def takepic():
    with picamera.PiCamera() as camera:
        time.sleep(1)
        camera.resolution = (width, height)
        with picamera.array.PiRGBArray(camera) as stream:
            camera.capture(stream, format='rgb')
            return stream.array


if __name__ == '__main__':
    print 'Taking first pic'
    data1 = takepic()

    time.sleep(10)
    print 'Taking second pic'
    data2 = takepic()
    print 'Diffing'
    
    diffCount = 0L;
    for w in range(0, width):
        for h in range(0, height):
            # get the diff of the pixel. Conversion to int
            # is required to avoid unsigned short overflow.
            diff = abs(int(data1[h][w][1]) - int(data2[h][w][1]))
            if  diff > threshold:
                diffCount += 1
		if diffCount > sensitivity:
                    break; # break inner loop
        if diffCount > sensitivity:
            break; #break outer loop.

    if diffCount > sensitivity:
        print 'Motion Detected'
            


    
    
