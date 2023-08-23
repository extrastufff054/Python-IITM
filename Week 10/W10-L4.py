# Introduction to NumPy Library

# NumPy : Numerical Python 
# ndarray : N-dimensional array

a = [42]
b = [1,2,3,4,5]
c = [[1,2,3],[4,5,6]]
d = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]

print(a,"\n",b,"\n",c,"\n",d)
print('----'*20)
# Using NumPy

import numpy as np

a = np.array([42])
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a,a.ndim,'\n')
print(b,b.ndim,'\n')
print(c,c.ndim,'\n')
print(d,d.ndim,'\n')

