#include <iostream>
#include <fstream>
#include <string>
#include <chrono>

using namespace std;

bool has_five_letter_palindrome(string str)
{
    for (int i = 0; i < str.length() - 4; i++)
    {
        string substring = str.substr(i, 5);
        if (substring == string(substring.rbegin(), substring.rend()))
        {
            return true;
        }
    }
    return false;
}

bool examine_strings(string str)
{
    for (int i = 0; i < str.length(); i++)
    {
        for (int j = i+1; j <= str.length(); j++)
        {
            if (has_five_letter_palindrome(str.substr(i, j-i)))
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int count = 0;
    auto start = chrono::high_resolution_clock::now();
    for (int i = 1; i <= 100; i++)
    {
        string filename = "palindrome_txts/" + to_string(i) + ".txt";
        ifstream file(filename);
        string data((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
        bool found = examine_strings(data);
        if (found)
        {
            count++;
        }
    }
    auto end = chrono::high_resolution_clock::now();
    double sequential_time = chrono::duration_cast<chrono::milliseconds>(end - start).count() / 1000.0;

    cout << "Palindromes Detected: " << count << endl;
    cout << "Elapsed Time: " << sequential_time << "s" << endl;

    return 0;
}
