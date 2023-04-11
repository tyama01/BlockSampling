#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <map>
#include <sstream>
#include "../include/graph.h"


using namespace std;

// 指定したファイルの読み込み
void read_graph_from_text_file(string file_path, Graph& graph){
    ifstream ifs(file_path);
    if(!ifs){
        cout << "Failed to open file" << endl;
        exit(-1);
    } else {
        for(int n1, n2; ifs >> n1 >> n2;){
            graph.add_edge(n1, n2);
        }
    }
}

void read_pr_from_text_file(string file_path, Graph& graph){
    ifstream ifs(file_path);
    if(!ifs){
        cout << "Failed to open file" << endl;
        exit(-1);
    } else{
        string str;
        int i;
        double d;
        while(getline(ifs, str)){
            stringstream ss(str);
            ss >> i >> d;
            graph.pr_list[i] = d;
        }
    }
}