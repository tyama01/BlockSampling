#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <filesystem>
#include <utility>
#include "../include/graph.h"
#include "../include/read.h"

// Files to compile
// g++ main.cpp graph.cpp read.cpp -std=gnu++17

using namespace std;
namespace fs = filesystem;

int main(int argc, char* argv[]){

    /* グラフ選択 */
    string graph_name;
    cout << "Enter graph name : ";
    cin >> graph_name;

    /* グラフのデータセットがあるか確認 */
    string dataset_path = "../datasets/" + graph_name + ".txt";
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

    vector<vector<int>> block_id = graph.get_block_id(0.00001);
    cout << block_id.size() << endl;

    return 0;
}

