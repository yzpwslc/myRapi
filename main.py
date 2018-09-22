from __future__ import print_function
import os
import sys
import cv2
import time
import numpy
import socket
from PIL import Image
from io import StringIO, BytesIO


class SendVideo(object):
    IP = '192.168.50.60'
    PORT = 5000

    def __init__(self):
        self.init_param()

    def init_param(self):
        self.addr = (self.IP, self.PORT)

    def img_to_stream(self, pic):
        img_io = None
        with BytesIO() as stream:
            temp = Image.fromarray(pic)
            temp.save(stream, format='JPEG')
            img_io = stream.getvalue()
        return img_io

    def camera(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.cam = cv2.VideoCapture(1)
        while self.cam.isOpened():
            print('camera is opening!')
            ret, frame = self.cam.read()
            if ret:
                jpeg = self.img_to_stream(frame)
                self.sock.sendto(jpeg, self.addr)
            self.cam.release()
            self.sock.close()

    def close_source(self):
        self.cam.release()
        self.sock.close()
        print('closed camera!...')


if __name__ == '__main__':
    s = SendVideo()
    s.camera()
    # time.sleep(10)
    # s.close_source()



