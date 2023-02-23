#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <utility>

#define MINX (-3)
//MAXX Happens to be an upper bound for all zeroes of the function...
#define MAXX (5)
#define NUM_INTERVALS (pow(4, 9))
#define NUM_BISECTION_ITERATIONS (30)

using namespace std;

double f(double x){
    return 5 * x * exp(-x) * cos(x) + 1;
}

double bisection_method(double x0, double x1){
    for (unsigned int i = 0; i < NUM_BISECTION_ITERATIONS; i++){
        double midpoint = 0.5*x0 + 0.5*x1;
        f(x0) * f(midpoint) < 0 ? x1 = midpoint : x0 = midpoint;
    }
    return 0.5*x0 + 0.5*x1;
}

int main(int argc, char** argv){
    vector<pair<double, double>> relevant_intervals;
    for (unsigned int i = 0; i < NUM_INTERVALS - 1; i++){
        double x0 = MINX + (MAXX - MINX) / NUM_INTERVALS * (i);
        double x1 = MINX + (MAXX - MINX) / NUM_INTERVALS * (i + 1);
        if (f(x0) * f(x1) < 0)
            relevant_intervals.push_back(make_pair(x0, x1));
    }
    cout << fixed << setprecision(20);
    for (const auto & x : relevant_intervals){
        cout << "One solution is approximately " << bisection_method(x.first, x.second) << endl;
    }
}