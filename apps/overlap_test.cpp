#include <iostream>
#include <vector>

// g++ overlap_test.cpp -std=gnu++17

using namespace std;

int main(){
    vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    double block_size = 0.5;

    int N = 9;
    int n = N*block_size;

    int over_lap = n / 2;

    int size = ((v.size() - 1) / n + 1) + ((v.size() - 1 - over_lap) / n + 1);

    vector<int> vec[size];

    cout << "end 1" << endl;

    //このループの各反復は、次の`n`要素のセットを処理します
    //そしてそれを`vec`のk番目のインデックスのvectorに格納します
    for (int k = 0; k < size; ++k)
    {
        //次の`n`要素のセットの範囲を取得します
        auto start_itr = next(v.cbegin(), k*n - over_lap * k);
        auto end_itr = next(v.cbegin(), k*n + n - over_lap * k);

        cout << "end 2" << endl;
 
        //サブvectorにメモリを割り当てます
        vec[k].resize(n);
 
        //最後のサブvectorを処理するコード
        //含まれる要素が少ない
        if (k*n - over_lap*k + n - over_lap*k > v.size())
        {
            end_itr = v.cend();
            vec[k].resize(v.size() - k*n);
        }
 
        //入力範囲からサブvectorに要素をコピーします
        copy(start_itr, end_itr, vec[k].begin());
    }

    // id をブロック化
    vector<vector<int>> block_id(size);
    for(int i = 0; i < size; i++){
        for(int id : vec[i]){
            block_id[i].push_back(id);
        }
    }



    for(vector<int> v1 : block_id){
        for(int id : v1){
            cout << id << " ";
        }
        cout << endl;
    }

    return 0;
}