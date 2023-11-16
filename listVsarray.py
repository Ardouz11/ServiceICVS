# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:59:35 2021

@author: Ardouz11
"""
import timeit
import numpy as np
import matplotlib.pyplot as plt
def comparing_append_operation():
    """Function of comparaison"""
    time=[]
    # Python list with append()
    list_time=np.mean(timeit.repeat(setup="a = []", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
    print("lists :",list_time)
    # Python array with append()
    array_time=np.mean(timeit.repeat(setup="import array; a = array.array('f')", stmt="a.append(1.0)", number=1000, repeat=5000)) * 1000
    print("array of array :",array_time)
    # Numpy array with append()
    array_numpy_time=np.mean(timeit.repeat(setup="import numpy as np; a = np.array([])", stmt="np.append(a, [1.0])", number=1000, repeat=5000)) * 1000
    print("array of numpy :",array_numpy_time)
    time=[list_time,array_time]
    return time
"""



# Python list using +=
np.mean(timeit.repeat(setup="a = []", stmt="a += [1.0]", number=1000, repeat=5000)) * 1000

# Python array using += 
np.mean(timeit.repeat(setup="import array; a = array.array('f')", stmt="a += array.array('f', [1.0]) ", number=1000, repeat=5000)) * 1000


# Python list using extend()
np.mean(timeit.repeat(setup="a = []", stmt="a.extend([1.0])", number=1000, repeat=5000)) * 1000


# Python array using extend()
np.mean(timeit.repeat(setup="import array; a = array.array('f')", stmt="a.extend([1.0]) ", number=1000, repeat=5000)) * 1000
"""
if __name__=="__main__":
    y=comparing_append_operation()
    axis=["lists","array module"]
    plt.plot(axis,y,'b')
    plt.xlabel('different types ').set_color('blue')
    plt.ylabel('time/s').set_color('blue')