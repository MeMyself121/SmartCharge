from threading import Timer
import time
import scipy.io
import numpy as np
import scipy.spatial.distance
import time
import matplotlib.pyplot as plt
from operator import itemgetter
from itertools import groupby
import random
def consecutive(data, stepsize=1):
    return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)
def timeout():
    global eix_temporal
    print("Timeout executed!")
    if(eix_temporal[0]==1):
        print("CHARGER ON")
    if(eix_temporal[0]==-1):
        print("CHARGER OFF")

    eix_temporal = np.roll(eix_temporal,-1)
    eix_temporal[-1] = 0
    print(eix_temporal)
    t = Timer(2, timeout)
    t.start()

def timeout2():
    print("Timeout2 executed!")
    data_recived()
    t2 = Timer(random.randint(48, 60), timeout2)
    t2.start()


def data_recived():
    global eix_temporal
    mode = random.randint(0, 1)
    if(mode == 0):
        t_start  = random.randint(1, 24)
        t_end = (t_start + random.randint(1, 24))%24
        params = [t_start, t_end,0]
        print("new task started! charging from ",t_start," to ",t_end)
    if(mode ==1):
        charge_time = random.randint(1,24)
        charge_time_limit = random.randint(1,24)
        params = [charge_time, charge_time_limit,1]
        print("new task started! charging for ",charge_time," before ",charge_time_limit)


    print(params)


    t_time = time.gmtime().tm_hour +1
    if(params[2]) == 0:
        offset_end = t_start - t_end
        t_start = (params[0] - t_time)%24
        t_end = (t_start + offset_end)
        print(t_time)
        print(t_start)
        print(t_end)
        eix_temporal[t_start] = 1
        eix_temporal[t_end] = -1


    if(params[2]) == 1:
        charge_time = params[0]
        charge_time_limit = (params[1] -t_time)%24
        if (charge_time_limit<charge_time):
            charge_time_limit = charge_time_limit+12

        f = scipy.io.loadmat("serie.mat")
        serie = f["serie"]
        serie = serie[t_time:t_time+48]
        serie = serie.reshape((1,-1))[0]
        serie_sorted = np.sort(serie, axis=0)
        serie_sorted_indexes = np.argsort(serie, axis=0)
        time_axis = np.arange(eix_temporal.size)

        index_bons = serie_sorted_indexes[:charge_time]
        index_bons = np.sort(index_bons)
        ilist = index_bons.tolist()
        index_bons_grouped = consecutive(ilist)

        for aux in index_bons_grouped:
            eix_temporal[aux[0]] = 1
            eix_temporal[aux[-1]+1] = -1
    print(eix_temporal)

eix_temporal = np.zeros(48)
t = Timer(1, timeout)
t.start()
time.sleep(1.5)
t2 = Timer(1, timeout2)
t2.start()



# do something else, such as
t_time = time.gmtime().tm_hour +1
time_axis = np.arange(48)
f = scipy.io.loadmat("serie.mat")
serie = f["serie"]
serie = serie[t_time:t_time+48]
serie = serie.reshape((1,-1))[0]
serie_sorted = np.sort(serie, axis=0)
serie_sorted_indexes = np.argsort(serie, axis=0)
while True:
    input("Press Enter to continue...")
    print("Capturnig Plot!")

    plt.plot(time_axis, serie)

    indices_one = np.where(eix_temporal == 1)[0]
    indices_eno = np.where(eix_temporal == -1)[0]

    number_ones = np.count_nonzero(eix_temporal==1)
    number_enos = np.count_nonzero(eix_temporal==-1)
    print("Number ones: ",number_ones)
    print("Number enos: ",number_enos)
    i = 0
    if( number_enos>number_ones):
        plt.hlines(20,time_axis[0],time_axis[indices_eno[i]],linewidth=3000, color='#d62728',alpha=0.5)
        indices_eno[i] = 0

    for i in range(0,number_ones):
        plt.hlines(20,time_axis[indices_one[i]],time_axis[indices_eno[i]],linewidth=3000, color='#d62728',alpha=0.5)
        print("Dibuixant linea de ", time_axis[indices_one[i]], " a ", time_axis[indices_eno[i]])
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.title('ROC curves mean vectors')
    plt.grid(True)
    plt.show()
    plt.savefig("testmean_505.png")
