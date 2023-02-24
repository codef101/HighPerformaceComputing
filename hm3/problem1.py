import numpy as np
from scipy.optimize import root_scalar
import time
import multiprocessing as mp
import os

f = lambda x: np.sin(3*np.pi*np.cos(2*np.pi*x)*np.sin(np.pi*x))
a, b, n = -3, 5, 4**9
x0 = np.linspace(a, b, n)  
q = np.zeros_like(x0)  

def find_root(i):
    return root_scalar(f, bracket=[a, b], x0=x0[i]).root

if __name__ == '__main__':
  
    tic = time.perf_counter()
    for i in range(n):
        q[i] = find_root(i)
    toc = time.perf_counter()
    sequential_time = toc - tic

    tic = time.perf_counter()
    with mp.Pool(os.cpu_count()) as pool:
        q = np.array(pool.map(find_root, range(n)))
    toc = time.perf_counter()
    parallel_time = toc - tic

    speedup = sequential_time/parallel_time

    print("Sequential Elapsed Time:", sequential_time)
    print("Parallel Elapsed Time:", parallel_time)
    print("Speed Up : ", speedup)
    print("Efficiency: ",  speedup/os.cpu_count())
