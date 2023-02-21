#include<iostream>
#include<numeric>
#include<vector>

#include <chrono>
using namespace std;
vector<int> randomVector (int n, int upperBound);
int main(){
    
    int size = 500;
  
    vector<int> v1 = randomVector(size, 4);

    vector<int> v2 = randomVector(size, 4);

    int for_loop_sum = 0;

    cout << "=================================================================="<<endl;
    cout << "                           Slide 12                           "<<endl;
    cout << "=================================================================="<<endl;
    auto start = chrono::steady_clock::now();
    for (int i = 0; i < v1.size(); i++){
       for_loop_sum = for_loop_sum + v1[i] * v2[i];
    }
    auto end = chrono::steady_clock::now();
    auto diff = end - start;

    cout << "For Loop Product : " << for_loop_sum << endl;
    cout << "Execution time: " << chrono::duration <double, milli> (diff).count() << " ms" << endl;

    int product = 0;
    start = chrono::steady_clock::now();
    product = inner_product(v1.begin(), v1.end(), v2.begin(), 0);
    end = chrono::steady_clock::now();
    diff = end - start;
    cout << "Library Dot Product : " << product << endl;
    cout << "Execution time: "<< chrono::duration <double, milli> (diff).count() << " ms" << endl;

    cout << "Speed Up Product : " << for_loop_sum/product << endl;


    cout << "=================================================================="<<endl;
    cout << "                           Slide 13                           "<<endl;
    cout << "=================================================================="<<endl;
    auto start = chrono::steady_clock::now();
    for (int i = 0; i < v1.size(); i++){
       for_loop_sum = for_loop_sum + v1[i] * v2[i];
    }
    auto end = chrono::steady_clock::now();
    auto diff = end - start;

    cout << "For Loop Product : " << for_loop_sum << endl;
    cout << "Execution time: " << chrono::duration <double, milli> (diff).count() << " ms" << endl;

    int product = 0;
    start = chrono::steady_clock::now();
    product = inner_product(v1.begin(), v1.end(), v2.begin(), 0);
    end = chrono::steady_clock::now();
    diff = end - start;
    cout << "Library Dot Product : " << product << endl;
    cout << "Execution time: "<< chrono::duration <double, milli> (diff).count() << " ms" << endl;

    cout << "Speed Up Product : " << for_loop_sum/product << endl;



}
vector<int> randomVector (int n, int upperBound) {
  vector<int> vec (n);
  for (size_t i = 0; i < vec.size(); i++) {
    vec[i] = rand () % upperBound;
  }
  return vec;
}