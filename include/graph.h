#ifndef GUARD_GRAPH_H
#define GUARD_GRAPH_H

#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Graph{
    private:
        unordered_set<int> node_list_set;
        unordered_map<int, vector<int>> adjacency_list; // ノードid -> 隣接ノードのvector

    public:
        // getter 関数
        const vector<int> get_node_list_id_sort();
        const unordered_map<int, vector<int>>& get_adjacency_list();
        const int get_number_of_nodes();
        const int get_number_of_edges();

        // PR 値 unordered_map
        unordered_map<int, double> pr_list;

        // グラフの操作
        void add_edge(int n1, int n2);

        // 頂点IDをブロック化
        vector<vector<int>> get_block_id(double per_block_ratio);

        // グラフ演算
        unordered_map<int, double> pagerank();
        
};

#endif // GURAD_GRAPH_H