#include <chrono>
#include <thread>
#include <iostream>
#include <vector>

using namespace std;

using namespace std::this_thread;     // sleep_for, sleep_until
using namespace std::chrono_literals; // ns, us, ms, s, h, etc.
using std::chrono::system_clock;

void pauseExec()
{
    sleep_for(5s);
}

void loopFunction(int n)
{
    for (int i = 0; i < n; i++)
    {
        pauseExec();
    }
}

void spawnThreads(int n)
{
    std::vector<thread> threads(4);

    // spawn n threads:
    for (int i = 0; i < 4; i++)
    {
        threads[i] = thread(pauseExec);
    }

    for (auto &th : threads)
    {
        th.join();
    }
}
int main()
{

    int n = 20;
    auto start = chrono::steady_clock::now();
    loopFunction(n);
    auto end = chrono::steady_clock::now();
    auto sequential_time = end - start;

    start = chrono::steady_clock::now();
    spawnThreads(n);
    end = chrono::steady_clock::now();
    auto parallel_time = end - start;

    float speedup = sequential_time/parallel_time;

    cout << "Sequential Elapsed time: " << std::chrono::duration_cast<std::chrono::seconds>(sequential_time).count() << endl;
    cout << "Parallel Elapsed time: " << std::chrono::duration_cast<std::chrono::seconds>(parallel_time).count() << endl;
    cout << "Speed Up: " << speedup << endl;
    cout << "Average Efficiency: " << speedup/4  << endl;
}


