import numpy as np

A = np.array([ [3,7, 6], [11,-1, -8] ])
B = np.array([ [7,1,-1], [5,3,1] ])

print(A+B)
print(A*B)
print(2*A)
print(A.transpose())

print(((A*B).transpose()) == (A.transpose() * B.transpose()))
print((A*B).transpose())
print(A.transpose() * B.transpose())