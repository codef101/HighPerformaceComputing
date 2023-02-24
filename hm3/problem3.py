import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
from multiprocessing import Pool
import os

def ode_func(x, t, epsilon):
    dxdt = [x[1], epsilon*(1-x[0]**2)*x[1] - x[0]]
    return dxdt

def solve_ode(epsilon):
    x0 = [0, 1]
    t = np.linspace(0, 10, 101)
    sol = odeint(ode_func, x0, t, args=(epsilon,))
    return sol

if __name__ == '__main__':
    t = np.linspace(0, 10, 101)
    epsilon_values = np.linspace(0.1, 4, 20)

    #  Sequntial Method
    start = time.time()
    for epsilon in epsilon_values:
        sol = solve_ode(epsilon)
        plt.plot(t, sol[:, 0])
    
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.legend()
    plt.show()

    end = time.time()
    sequential_time = end - start
    print("Sequential Elapsed Time:" , sequential_time)

    #  Nearly Embarrassing Method
    start = time.time()
    pool = Pool(os.cpu_count())
    solutions = pool.map(solve_ode, epsilon_values)
    end = time.time()
    parallel_time = end - start
    print("ParallelElapsed Time:", parallel_time)

    #Stats 
    speedup = sequential_time/parallel_time
    print("Speed UP: ", speedup)
    print("Efficiency : ", speedup/os.cpu_count())

    for i in range(len(epsilon_values)):
     plt.plot(t, solutions[i][:, 0], label=f'epsilon={epsilon_values[i]}')

    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.legend()
    plt.show()
