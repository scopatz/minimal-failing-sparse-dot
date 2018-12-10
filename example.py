# coding: utf-8

# # Minimal failing sparse dot product example
import time
import numpy as np
import sparse

A = sA = sparse.load_npz('A.npz')
B = np.load('B.npz')['B']


print(sparse.__version__)

sB = sparse.COO(B)


t0 = time.time()
sC = sA.dot(sB)
print("run time is:", (time.time() - t0) / 60.0)
