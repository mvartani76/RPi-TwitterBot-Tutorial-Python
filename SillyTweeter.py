#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'V953Z63QVRV29g5k8AEvig'
CONSUMER_SECRET = 'pMdEj4upojdJPUW6X4GgiifYEYcFuXUW4IBXcQWFz0'
ACCESS_KEY = '2197297674-xTXUt8e6g0x7bkJhOqcwvT5cB3XbQwDvAc8g78N'
ACCESS_SECRET = 'Ba5RcDq2BMsYt89Bo4iESlj9o9sfX1WdWSvjiDj9S5bSr'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
