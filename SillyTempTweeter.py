#!/usr/bin/env python
import sys
from twython import Twython
import os

CONSUMER_KEY = 'V953Z63QVRV29g5k8AEvig'
CONSUMER_SECRET = 'pMdEj4upojdJPUW6X4GgiifYEYcFuXUW4IBXcQWFz0'
ACCESS_KEY = '2197297674-xTXUt8e6g0x7bkJhOqcwvT5cB3XbQwDvAc8g78N'
ACCESS_SECRET = 'Ba5RcDq2BMsYt89Bo4iESlj9o9sfX1WdWSvjiDj9S5bSr'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
api.update_status(status='My current CPU temperature is '+temp+' C')
