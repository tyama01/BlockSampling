#ifndef GUARD_GRAPH_H
#define GUARD_GRAPH_H

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <time.h>

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

        // エッジ追加　有向グラフ
        void add_edge(int n1, int n2);

        // エッジ追加 無向グラフ
        void u_add_edge(int n3, int n4);

        // 頂点IDをブロック化
        vector<vector<int>> get_block(double per_block_ratio);

        // 跨ぎを許した頂点IDのブロック化
        vector<vector<int>> get_cross_block(double per_block_ratio);

        // ブロックスコア取得
        vector<double> get_block_score(vector<vector<int>> block,
         unordered_map<int, double> pr_list);

        // ブロックサンプリング
        unordered_set<int> block_sampling(int block_num, vector<vector<int>> block,
        vector<int> index, double sampling_size, double beta);

        // グラフ演算
        unordered_map<int, double> pagerank();
        
};

#endif // GURAD_GRAPH_H