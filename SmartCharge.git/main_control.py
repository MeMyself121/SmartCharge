from threading import Timer
import time
import scipy.io
import numpy as np
import scipy.spatial.distance
import time
import matplotlib.pyplot as plt
from operator import itemgetter
from itertools import groupby

def timeout():
    global eix_temporal
    print("Timeout executed")
    if(eix_temporal[0]==1):
        print("CHARGER ON")
    if(eix_temporal[0]==-1):
        print("CHARGER OFF")

    eix_temporal = np.roll(eix_temporal,-1)
    eix_temporal[-1] = 0
    print(eix_temporal)
    t = Timer(1, timeout)
    t.start()


eix_temporal = [0,0,1,0,0,0,0,-1,0,0,0,1,0,0,-1,0]

print(eix_temporal)


t = Timer(1, timeout)
t.start()

# do something else, such as
time.sleep(100000)
