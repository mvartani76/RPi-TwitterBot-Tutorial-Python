#!/usr/bin/env python
import sys
from twython import Twython
import os

import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()
pygame.image.save(image,'webcam.jpg')

CONSUMER_KEY = 'V953Z63QVRV29g5k8AEvig'
CONSUMER_SECRET = 'pMdEj4upojdJPUW6X4GgiifYEYcFuXUW4IBXcQWFz0'
ACCESS_KEY = '2197297674-xTXUt8e6g0x7bkJhOqcwvT5cB3XbQwDvAc8g78N'
ACCESS_SECRET = 'Ba5RcDq2BMsYt89Bo4iESlj9o9sfX1WdWSvjiDj9S5bSr'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

photo = open('webcam.jpg','rb')
api.update_status_with_media(media=photo, status='My RPi be tweeting images now => ')
