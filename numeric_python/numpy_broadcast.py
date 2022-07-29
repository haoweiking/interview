# NumPy广播机制
import numpy as np


a = np.array([0.1,0.2,0.3,0.4])
b = np.array([10,20,30,40])
c = a * b
print(c)

a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
#b数组与a数组形状不同
b = np.array([1,2,3])
print(a + b)
