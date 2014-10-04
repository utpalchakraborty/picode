#!/usr/bin/env python

"""
import semail
import datetime

now = str(datetime.datetime.now())
semail.sendEmail('Pi is up at ' + now, 'Pi up!')
"""
import semail
import takepic as tp
import os

imagedir = '/home/pi/pipics/'
imagedirlocal = '/home/pi/pipicslocal/'

def noop():pass

def donormal():
    filename = tp.takepic(None, imagedirlocal)
    semail.sendEmail2("", "Pi Pic", [filename])
    

if __name__ == '__main__':
    noop()
    donormal()
