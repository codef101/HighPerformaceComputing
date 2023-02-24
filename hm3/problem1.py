import math

def newton(f, df, x0, tol=1e-6, max_iter=100000):
    """
    Find a root of a function f(x) using Newton's method.

    Parameters:
    f: function
        The function to find the root of.
    df: function
        The derivative of the function f(x).
    x0: float
        The initial guess for the root.
    tol: float
        The tolerance for the root, default is 1e-6.
    max_iter: int
        The maximum number of iterations, default is 100.

    Returns:
    float
        The approximate root of f(x).
    """
    # Iterate using Newton's method until the tolerance or maximum number of iterations is reached
    for i in range(max_iter):
        fx = f(x0)
        if abs(fx) < tol:
            return x0
        x0 = x0 - fx / df(x0)
    raise ValueError("No root was found within the maximum number of iterations.")

def fzero(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Find a root of a function f(x) within the interval [x0, x1] using the fzero function in MATLAB.

    Parameters:
    f: function
        The function to find the root of.
    x0: float
        The left endpoint of the interval.
    x1: float
        The right endpoint of the interval.
    tol: float
        The tolerance for the root, default is 1e-6.
    max_iter: int
        The maximum number of iterations, default is 100.

    Returns:
    float
        The approximate root of f(x) within the interval [x0, x1].
    """
    # Check that the function has different signs at the endpoints of the interval
    if f(x0) * f(x1) >= 0:
        raise ValueError("Function must have different signs at endpoints of interval.")

    # Use the initial guess x0 as the starting point for Newton's method
    x = x0
    while x < x1:
        if f(x) * f(x + tol) <= 0:
            # Perform Newton's method starting at the midpoint of the bracketed interval
            return newton(f, lambda x: (f(x + tol) - f(x)) / tol, (x + x + tol) / 2, tol, max_iter)
        x += tol

    raise ValueError("No root was found within the maximum number of iterations.")

# Example usage: Find a root of the function f(x) = sin(3*pi*cos(2*pi*x))*sin(pi*x) within the interval [0, 1]
f = lambda x: math.sin(3*math.pi*math.cos(2*math.pi*x)) * math.sin(math.pi*x)
root = fzero(f, 0.5, 0.5)
print(f"Approximate root of f(x) within [-3, 5] is {root}")
