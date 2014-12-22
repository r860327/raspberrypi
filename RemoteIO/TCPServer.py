#!/usr/bin/env python
from socket import *
from time import ctime
import time as timer
import RPi.GPIO as GPIO

#define a function which used to blink GPIO
def blinkGPIO(io):
    GPIO.output(io, GPIO.HIGH)
    timer.sleep(1)
    GPIO.output(io, GPIO.LOW)
#    timer.sleep(1)

#init GPIO
GPIO.setmode(GPIO.BOARD)
UP = 21
DOWN = 22
LEFT = 23
RIGHT = 24

CAM_UP = 11
CAM_DOWN = 12
CAM_LEFT = 13
CAM_RIGHT = 15
# need to set up every channel which are using as an input or an output
GPIO.setup(UP, GPIO.OUT)
GPIO.setup(DOWN, GPIO.OUT)
GPIO.setup(LEFT, GPIO.OUT)
GPIO.setup(RIGHT, GPIO.OUT)
GPIO.setup(CAM_UP, GPIO.OUT)
GPIO.setup(CAM_DOWN, GPIO.OUT)
GPIO.setup(CAM_LEFT, GPIO.OUT)
GPIO.setup(CAM_RIGHT, GPIO.OUT)

#init socket
HOST = ''
PORT = 20000 
BUFSIZE = 1024    #1KB
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpClientSock,clientAddr = tcpSerSock.accept()
    print '...connected from :', clientAddr
    while True:
        data = tcpClientSock.recv(BUFSIZE)
        if not data:
            break
        if(data == 'ud'):
            GPIO.output(UP, GPIO.HIGH)
        if(data == 'uu'):
            GPIO.output(UP, GPIO.LOW)
        if(data == 'ld'):
            GPIO.output(LEFT, GPIO.HIGH)
        if(data == 'lu'):
            GPIO.output(LEFT, GPIO.LOW)
        if(data == 'rd'):
            GPIO.output(RIGHT, GPIO.HIGH)
        if(data == 'ru'):
            GPIO.output(RIGHT, GPIO.LOW)
        if(data == 'dd'):
            GPIO.output(DOWN, GPIO.HIGH)
        if(data == 'du'):
            GPIO.output(DOWN, GPIO.LOW)
        if(data == 'udc'):
            GPIO.output(CAM_UP, GPIO.HIGH)
        if(data == 'uuc'):
            GPIO.output(CAM_UP, GPIO.LOW)
        if(data == 'ldc'):
            GPIO.output(CAM_LEFT, GPIO.HIGH)
        if(data == 'luc'):
            GPIO.output(CAM_LEFT, GPIO.LOW)
        if(data == 'rdc'):
            GPIO.output(CAM_RIGHT, GPIO.HIGH)
        if(data == 'ruc'):
            GPIO.output(CAM_RIGHT, GPIO.LOW)
        if(data == 'ddc'):
            GPIO.output(CAM_DOWN, GPIO.HIGH)
        if(data == 'duc'):
            GPIO.output(CAM_DOWN, GPIO.LOW)
        print '[%s] %s' % (ctime(), data)
        tcpClientSock.send('[%s] %s' % (ctime(), data))
    tcpClientSock.close()
tcpSerSock.close()

