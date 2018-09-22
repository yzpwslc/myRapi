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
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cam = cv2.VideoCapture(0)
        while cam.isOpened():
            ret, frame = cam.read()
            if ret:
                jpeg = self.img_to_stream(frame)
                sock.sendto(jpeg, self.addr)
            cam.release()
            sock.close()


if __name__ == '__main__':
    s = SendVideo()


