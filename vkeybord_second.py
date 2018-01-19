#!/usr/bin/env python3
import virtkey
import time

v = virtkey.virtkey()

v.press_unicode(ord('l'))#按下字母l
v.release_keysym(ord('l'))#释放字母l
v.press_unicode(ord('s'))#按下字母s
v.release_keysym(ord('s'))
v.press_unicode(ord('u'))#按下字母u
v.release_keysym(ord('u'))
v.press_unicode(ord('s'))#按下字母s
v.release_keysym(ord('s'))
v.press_unicode(ord('b'))#按下字母b
v.release_keysym(ord('b'))
v.press_keysym(65421)#按下ENTER
v.release_keysym(65421)#释放ENTER
