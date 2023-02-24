#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono> // For profiling execution time
#include <numeric> // For std::inner_product()

using namespace std;

int dot_product_for_loop(const vector<int>& vec1, const vector<int>& vec2)
{
    int dot_product = 0;
    for (size_t i = 0; i < vec1.size(); i++)
    {
        dot_product += vec1[i] * vec2[i];
    }
    return dot_product;
}

int dot_product_std(const vector<int>& vec1, const vector<int>& vec2)
{
    return inner_product(vec1.begin(), vec1.end(), vec2.begin(), 0);
}

vector<int> create_random_vector(int n)
{
    vector<int> vec(n);
    srand(time(0));
    for (int i = 0; i < n; i++)
    {
        vec[i] = rand() % 100; 
    }
    return vec;
}

vector<vector<int>> create_random_matrix(int n)
{
    vector<vector<int>> mat(n, vector<int>(n));
    srand(time(0));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            mat[i][j] = rand() % 100;
        }
    }
    return mat;
}

vector<int> matrix_vector_product(const vector<vector<int>>& mat, const vector<int>& vec)
{
    vector<int> result(mat.size());
    for (size_t i = 0; i < mat.size(); i++)
    {
        result[i] = dot_product_for_loop(mat[i], vec);
    }
    return result;
}

vector<int> matrix_vector_product_inner_product(const vector<vector<int>>& mat, const vector<int>& vec)
{
    vector<int> result(mat.size());
    for (size_t i = 0; i < mat.size(); i++)
    {
        result[i] = dot_product_std(mat[i], vec);
    }
    return result;
}


vector<vector<int>> matrix_multiplication(const vector<vector<int>>& mat1, const vector<vector<int>>& mat2)
{
    vector<vector<int>> result(mat1.size(), vector<int>(mat2.size()));
    for (size_t i = 0; i < mat1.size(); i++)
    {
        for (size_t j = 0; j < mat2.size(); j++)
        {
            vector<int> mat2_col(mat2.size());
            for (size_t k = 0; k < mat2.size(); k++)
            {
                mat2_col[k] = mat2[k][j];
            }
            result[i][j] = dot_product_for_loop(mat1[i], mat2_col);
        }
    }
    return result;
}


int main()
{
    int n = 1000;

    const vector<int> vec1 = create_random_vector(n);
    const vector<int> vec2 = create_random_vector(n);

    vector<vector<int>> mat = create_random_matrix(n);

    auto start_for_loop = chrono::steady_clock::now();
    int dot_product_for = dot_product_for_loop(vec1, vec2);
    auto end_for_loop = chrono::steady_clock::now();

    auto start_std = chrono::steady_clock::now();
    int dot_product_std_sum = dot_product_std(vec1, vec2);
    auto end_std = chrono::steady_clock::now();

    float speedup= (end_for_loop - start_for_loop).count()/(end_std - start_std).count();

    cout << "\n";
    cout << "The dot product of the two vectors using a for loop is: " << dot_product_for << endl;
    cout << "The dot product of the two vectors using std::inner_product() is: " << dot_product_std_sum << endl;

    cout << endl;
    cout << "Execution time using a for loop: " << chrono::duration_cast<chrono::microseconds>(end_for_loop - start_for_loop).count() << " microseconds" << endl;
    cout << "Execution time using std::inner_product(): " << chrono::duration_cast<chrono::microseconds>(end_std - start_std).count() << " microseconds" << endl;
    cout << endl;
    cout << "SpeedUp " <<speedup<< " microseconds" << endl;


    auto start = chrono::steady_clock::now();
    vector<int> result = matrix_vector_product(mat, vec1);
    auto end = chrono::steady_clock::now();
    auto for_loop_duration = end - start;

    cout << "Execution time of matrix by vector using a for loop: " << chrono::duration_cast<chrono::microseconds>(end - start).count() << " microseconds" << endl;
    cout << endl;
    
    start = chrono::steady_clock::now();
    result = matrix_vector_product_inner_product(mat, vec1);
    end = chrono::steady_clock::now();
    speedup = (end-start)/for_loop_duration;
    
    cout << "Execution of time of matrix by vector using std::inner_product(): " << chrono::duration_cast<chrono::microseconds>(end - start).count() << " microseconds" << endl;
    cout << "SpeedUp " <<speedup<< " microseconds" << endl;

    vector<vector<int>> mat1 = create_random_matrix(n);
    vector<vector<int>> mat2 = create_random_matrix(n);

    start = chrono::steady_clock::now();
    vector<vector<int>> res = matrix_multiplication(mat1,mat2);
    end = chrono::steady_clock::now();
    cout << "Execution of time of matrix by matrix using std::inner_product(): " << chrono::duration_cast<chrono::microseconds>(end - start).count() << " microseconds" << endl;

    return 0;
}
