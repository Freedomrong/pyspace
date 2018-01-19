#!/usr/bin/env python3
import os
import sys
import virtkey

print('\n')
os.system('pwd')
os.chdir('../')
os.chdir('workspace/simple-gcc-stm32-project/')
os.system('make clean')
os.system('make')
os.system('arm-none-eabi-gdb LED_project.elf')

v = virtkey.virtkey()

# v.press_unicode(ord('m'))
# v.release_keysym(ord('m'))
# v.press_unicode(ord('o'))
# v.release_keysym(ord('o'))
# v.press_unicode(ord('n'))
# v.release_keysym(ord('n'))
# v.press_unicode(ord('i'))
# v.release_keysym(ord('i'))
# v.press_unicode(ord('t'))
# v.release_keysym(ord('t'))
# v.press_unicode(ord('o'))
# v.release_keysym(ord('o'))
# v.press_unicode(ord('r'))
# v.release_keysym(ord('r'))
#
# v.press_keysym(65408)#按下SPACE
# v.release_keysym(65408)#释SPACE
#
# v.press_unicode(ord('r'))
# v.release_keysym(ord('r'))
# v.press_unicode(ord('e'))
# v.release_keysym(ord('e'))
# v.press_unicode(ord('s'))
# v.release_keysym(ord('s'))
# v.press_unicode(ord('e'))
# v.release_keysym(ord('e'))
# v.press_unicode(ord('t'))
# v.release_keysym(ord('t'))
#
# v.press_keysym(65421)#按下ENTER
# v.release_keysym(65421)#释放ENTER
