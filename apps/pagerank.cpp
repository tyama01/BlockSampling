#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <filesystem>
#include <utility>
#include <algorithm>
#include "../include/graph.h"
#include "../include/read.h"

// Files to compile
// g++ pagerank.cpp graph.cpp read.cpp -std=gnu++17

using namespace std;
namespace fs = filesystem;

int main(int argc, char* argv[]){

    /* グラフ選択 */
    string graph_name;
    cout << "Enter graph name : ";
    cin >> graph_name;

    /* グラフのデータセットがあるか確認 */
    string datasets;
    cout << "Enter dic (datasets or sampling datasets) : ";
    cin >> datasets;
    string real_datasets;
    cout << "Enter dic (real datasets) : ";
    cin >> real_datasets;
    string dataset_path = "../" + datasets + "/" + real_datasets + "/" + 
    graph_name +".txt";
    if(!fs::is_regular_file(dataset_path)){ // なければ異常終了
        cout << "There are no such datasets" << endl;
        return 1;
    }

    /* グラフ読み込み */
    Graph graph;
    read_graph_from_text_file(dataset_path, graph);
    cout << "Compleate reading graph" << endl;

    int N = graph.get_number_of_nodes();
    int E = graph.get_number_of_edges();

    cout << "Nodes : " << N << endl;
    cout << "Edges : " << E << endl;

    unordered_map<int, double> score = graph.pagerank();
    cout << "Complete PageRank" << endl;

    // map valueソート
    typedef pair<int, double> pair;
    vector<pair> vec;

    copy(score.begin(), score.end(), back_inserter<vector<pair>>(vec));

    sort(vec.rbegin(), vec.rend(), [](const pair &l, const pair &r)
    {
        if(l.second != r.second){
            return l.second < r.second;
        }
        return l.first < r.first;
    });

    // txtファイル出力
    //string pr_result_file;
    //cout << "Enter PageRank dic/file name : ";
    //cin >> pr_result_file;

    string pr_result_path = "../pr_result/" + real_datasets + "/" + 
    graph_name + "_pr.txt";
    ofstream ofs;
    ofs.open(pr_result_path);

    for(auto const &pair: vec){
        ofs << pair.first << " " << pair.second << endl;
    }


    return 0;
}

