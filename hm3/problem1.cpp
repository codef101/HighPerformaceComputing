#include <iostream>
#include <cmath>

using namespace std;

double f(double x)
{
    return sin(3 * M_PI * cos(2 * M_PI * x)) * sin(M_PI * x);
}

double df(double x)
{
    return -2 * M_PI * sin(2 * M_PI * x) * sin(3 * M_PI * cos(2 * M_PI * x)) + 3 * M_PI * cos(2 * M_PI * x) * cos(3 * M_PI * cos(2 * M_PI * x)) * sin(M_PI * x);
}

double newton(double (*f)(double), double (*df)(double), double x0, double tol=1e-6, int max_iter=100)
{
    // Iterate using Newton's method until the tolerance or maximum number of iterations is reached
    for (int i = 0; i < max_iter; i++)
    {
        double fx = f(x0);
        if (abs(fx) < tol)
        {
            return x0;
        }
        x0 = x0 - fx / df(x0);
    }
    throw invalid_argument("No root was found within the maximum number of iterations.");
}

double fzero(double (*f)(double), double x0, double x1, double tol=1e-6, int max_iter=100)
{
    // Check that the function has different signs at the endpoints of the interval
    if (f(x0) * f(x1) >= 0)
    {
        throw invalid_argument("Function must have different signs at endpoints of interval.");
    }

    // Use the initial guess x0 as the starting point for Newton's method
    double x = x0;
    while (x < x1)
    {
        if (f(x) * f(x + tol) <= 0)
        {
            // Perform Newton's method starting at the midpoint of the bracketed interval
            return newton(f, df, (x + x + tol) / 2, tol, max_iter);
        }
        x += tol;
    }

    throw invalid_argument("No root was found within the maximum number of iterations.");
}

int main()
{
    // Example usage: Find a root of the function f(x) = sin(3*pi*cos(2*pi*x))*sin(pi*x) within the interval [0, 1]
    double root = fzero(f, -3, 5);
    cout << "Approximate root of f(x) within [0, 1] is " << root << endl;

    return 0;
}
