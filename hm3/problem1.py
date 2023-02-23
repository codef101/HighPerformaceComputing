import numpy

def func(x, K, H, u):
    return (u - K * (log(1 + H / x) * (x + H) - H)
            / log(2) / x ** 2 / log2((x + H) / x) ** 2 / (x + H))

sol = root_scalar(func, args=(5, 6, 100), method='toms748', bracket=[1e-3, 1])
print(sol.root, func(sol.root, 5, 6, 100))