__author__ = 'abao2k'

import threading
from  TestAllCass import *
import time
def threads():
    btime  = time.time()
    threads=[]
    threads.append(threading.Thread(target = demo1))
    threads.append(threading.Thread(target = demo2))
    threads.append(threading.Thread(target = demo3))
    threads.append(threading.Thread(target = demo4))

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    print ("threads end")
    etime = time.time()
    print ("count time="+str(etime-btime))




