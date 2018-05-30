import gdb
import time

time.sleep(2)
gdb.execute('target remote localhost:3333')
gdb.execute('monitor reset')
gdb.execute('monitor halt')
