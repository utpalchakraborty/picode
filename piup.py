#!/usr/bin/env python
import semail
import datetime

now = str(datetime.datetime.now())
semail.sendEmail('Pi is up at ' + now, 'Pi up!')
