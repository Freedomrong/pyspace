#!/usr/bin/env/ python3
#-*- coding = utf-8 -*-

import os
import sys
import struct

def jieyasuo():
    print('de tar.gz is doing')
    os.system('rm -f -r /home/pi/pyspace/new_simple-gcc-stm32-project')
    os.system('tar zxvf new_simple-gcc-stm32-project.tar.gz')
    print('end de tar.gz')


if __name__ == '__main__':
    jieyasuo()
