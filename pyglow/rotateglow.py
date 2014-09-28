#!/usr/bin/env python
import pyglow
import time

pyg = pyglow.PyGlow()

try:
    while True:
        for i in range(1,4):
            pyg.arm(i, 50)
            time.sleep(1)
            pyg.all(0)
except KeyboardInterrupt:
    pyg.all(0)
