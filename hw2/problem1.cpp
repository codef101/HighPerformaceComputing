#include <chrono>
#include <thread>
#include <iostream>
using namespace std;

using namespace std::this_thread;     // sleep_for, sleep_until
using namespace std::chrono_literals; // ns, us, ms, s, h, etc.
using std::chrono::system_clock;

void pauseExec(int t);

int main() {

    int n = 3;
    auto start = chrono::steady_clock::now();
    for (int i = 0; i < n; i++)
    {
        pauseExec(5);
    }
    auto end = chrono::steady_clock::now();
    auto diff = end - start;
    cout << "Execution time: " << std::chrono::duration_cast<std::chrono::seconds> (diff).count() << " ms" << endl;

}

void pauseExec(int t) {
    sleep_for(5s);
}