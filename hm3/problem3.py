import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def vanderpol_oscillator(mu):
    def fun(t, y):
        dydt = [y[1], mu * (1 - y[0]**2) * y[1] - y[0]]
        return dydt

    t_span = [0, 20]
    y0 = [1, 0]  # initial conditions
    sol = solve_ivp(fun, t_span, y0, t_eval=np.linspace(t_span[0], t_span[1], 200))
    return sol

sol = vanderpol_oscillator(1.5)

# Plotting the solution:
plt.plot(sol.t, sol.y[0], 'b', label='y(t)')
plt.plot(sol.t, sol.y[1], 'g', label='y\'(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
