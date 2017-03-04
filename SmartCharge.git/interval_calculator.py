import scipy.io
import numpy as np
import scipy.spatial.distance
import time
import matplotlib.pyplot as plt
from operator import itemgetter
from itertools import groupby


class Interval:

   def __init__(self,t_start, t_end):

      self.t_start = t_start
      self.t_end = t_end


   def duration(self):
       print(self.t_end-self.t_start)

def consecutive(data, stepsize=1):
    return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)


charge_time = 4
charge_time_limit = 23

f = scipy.io.loadmat("serie.mat")
serie = f["serie"]
serie = serie[0:48]
serie = serie.reshape((1,-1))[0]
print(serie[0])
serie_sorted = np.sort(serie, axis=0)
print(serie_sorted)
serie_sorted_indexes = np.argsort(serie, axis=0)
print(serie_sorted_indexes)
print(serie.size)
time_axis = np.arange(serie.size)

index_bons = serie_sorted_indexes[:charge_time]
index_bons = np.sort(index_bons)


# selected_times = np.zeros(serie.size)
# for aux in index_bons:
#     selected_times[aux]  = serie[aux]
#     selected_times[aux + 1] = serie[aux + 1]
#
#plt.plot(time_axis, serie, 'r-', selected_times, 'bs')

data = [27,28 , 29, 5, 6, 7, 14, 15, 16, 17]
print(consecutive(data))
print(index_bons)
ilist = index_bons.tolist()
index_bons_grouped = consecutive(ilist)

print(index_bons_grouped)

plt.plot(time_axis, serie)

for aux in index_bons_grouped:
    plt.hlines(serie[aux],time_axis[aux[0]],time_axis[aux[-1]] + 1,linewidth=3000, color='#d62728',alpha=0.5)
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC curves mean vectors')
plt.grid(True)
plt.show()

plt.savefig("testmean_505.png")
