#include <chrono>
#include <thread>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::this_thread;    
using namespace std::chrono_literals; 
using std::chrono::system_clock;

void timeconsuming()
{
    sleep_for(5s);
}

void for_loop(int n)
{
    for (int i = 0; i < n; i++)
    {
        timeconsuming();
    }
}

void worker_threads(int n)
{
    std::vector<thread> threads(4);
    for (int i = 0; i < 4; i++)
    {
        threads[i] = thread(timeconsuming);
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
    for_loop(n);
    auto end = chrono::steady_clock::now();
    auto sequential_time = end - start;

    start = chrono::steady_clock::now();
    worker_threads(n);
    end = chrono::steady_clock::now();
    auto parallel_time = end - start;

    float speedup = sequential_time/parallel_time;

    cout << "Sequential Elapsed time: " << std::chrono::duration_cast<std::chrono::seconds>(sequential_time).count() << endl;
    cout << "Parallel Elapsed time: " << std::chrono::duration_cast<std::chrono::seconds>(parallel_time).count() << endl;
    cout << "Speed Up: " << speedup << endl;
    cout << "Average Efficiency: " << speedup/4  << endl;
}


