#!/usr/bin/env python
import sys
from twython import Twython
import os
import time
import RPi.GPIO as GPIO

CONSUMER_KEY = 'V953Z63QVRV29g5k8AEvig'
CONSUMER_SECRET = 'pMdEj4upojdJPUW6X4GgiifYEYcFuXUW4IBXcQWFz0'
ACCESS_KEY = '2197297674-xTXUt8e6g0x7bkJhOqcwvT5cB3XbQwDvAc8g78N'
ACCESS_SECRET = 'Ba5RcDq2BMsYt89Bo4iESlj9o9sfX1WdWSvjiDj9S5bSr'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 


GPIO.setmode(GPIO.BOARD)

# set up GPIOs 7,11,13,15 as inputs
GPIO.setup(7,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.IN)

gpioconcatold = 5555
testgpvar = 1

while (testgpvar <> 0):

	gpvar7 = GPIO.input(7)
	gpvar11 = GPIO.input(11)
	gpvar13 = GPIO.input(13)
	gpvar15 = GPIO.input(15)
	

	gpioconcat = str(gpvar7)+str( gpvar11)+str(gpvar13)+str(gpvar15)
	localtime = time.asctime( time.localtime(time.time()))

	# Cannot tweet duplicates so only update if the GPIO position changes and add time info
	if (gpioconcat <> gpioconcatold):
		api.update_status(status='GPIO79111315 is '+str(gpioconcat)+' at time: '+str(localtime))
		
	gpioconcatold = gpioconcat

	# end loop if all GPIOs selected are 0
	testgpvar = gpvar7 or gpvar11 or gpvar13 or gpvar15

	
GPIO.cleanup()
