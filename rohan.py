#!/usr/bin/env python
import os
import datetime
import semail

def getSalutation():
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 12:
        return 'Good morning'
    elif hour < 18:
        return 'Good afternoon'
    else:
        return 'Good evening'

def spacelines():
    for i in range(1,4): print '\n'
    
if __name__ == '__main__':
    date = os.popen('date').readlines()[0]
    spacelines()
    print getSalutation() + ' Rohan. Date & Time now is:' + date
    print 'Today\'s tasks are the following:\n'
    for num, line in enumerate(open('tasks.txt')):
        print '%d: %s' % (num + 1, line.strip())
    spacelines()

    #also email me that the program was executed by Rohan.
    semail.sendEmail('Rohan.py was executed at ' + date)
    
