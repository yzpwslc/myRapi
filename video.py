# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 18:07:24 2018

@author: yzp1011
"""

#import os
#import sys
#from time import time
#
#
#class Camera(object):
#    base_dir = './'
#    dir_dict = {
#            'in':'DIN',
#                } 
#    def __init__(self):
#        self.init_param()
#        
#    def init_param(self):
#        self.in_dir = os.path.join(self.base_dir,self.dir_dict.get('in'))
#        self.print_(self.in_dir)
#        self.frames = [open(os.path.join(self.in_dir,x),'rb').read() for x in os.listdir(self.in_dir)]
#    
#    def get_frame(self):
#        return self.frames[int(time()) % 3]
#    
#    def print_(self,param):
#        print(param)
#        
#        
#if __name__ == '__main__':
#    cam = Camera()
import os
import sys
import cv2
import time
import numpy
import socket
from PIL import Image
from io import StringIO,BytesIO

class send_video(object):
    IP = '192.168.50.60'
    PORT = 5000
    address = (IP,PORT)
    def __init__(self):
        self.camera()
    
    def img_to_stream(self,pic):
        img_io = None
        with BytesIO() as stream:
            temp = Image.fromarray(pic)
            temp.save(stream,format='JPEG')
            img_io = stream.getvalue()
        return img_io
    
    def camera(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        cam = cv2.VideoCapture(0)
        while (cam.isOpened()):
            ret,frame = cam.read()
            if ret == True:
#                cv2.imshow('transmitting',frame)
                jpeg = self.img_to_stream(frame)
                sock.sendto(jpeg,self.address)
        cam.release()
        sock.close()
        
if __name__ == '__main__':
    s = send_video()
    
 
    