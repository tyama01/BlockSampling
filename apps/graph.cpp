#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <algorithm>
#include "../include/graph.h"

using namespace std;

/* getter 関数 */

// const 参照のノードリストを返す vector でidが昇順
const vector<int> Graph::get_node_list_id_sort(){
    vector<int> node_list(this->node_list_set.begin(), this->node_list_set.end());
    sort(node_list.begin(), node_list.end());
    return node_list;
}

// const 参照の隣接リストを返す
const unordered_map<int, vector<int>>& Graph::get_adjacency_list(){
    return this->adjacency_list;
}

// ノード数を返す
const int Graph::get_number_of_nodes(){
    return this->node_list_set.size();
}

// エッジ数を返す
const int Graph::get_number_of_edges(){
    int number_of_edges = 0;

    // ノードが持つエッジ数を合計する
    for(const pair<int, vector<int>>& item : this->adjacency_list){
        number_of_edges += item.second.size();
    }

    return number_of_edges;
}


/* グラフの操作 */

// エッジ生成 
void Graph::add_edge(int n1, int n2){
    // adjacency_list に n1 -> n2 を追加(有向のため)
    this->adjacency_list[n1].push_back(n2);
    this->adjacency_list[n2];

    // 頂点リスト生成 (set)
    this->node_list_set.insert(n1);
    this->node_list_set.insert(n2);
}


/* 頂点IDをブロック化 */
vector<vector<int>> Graph::get_block_id(double per_block_ratio){

    // ソートされた頂点ID
    vector<int> v = Graph::get_node_list_id_sort();

    // 頂点数
    int N = Graph::get_number_of_nodes();

    //vectorをそれぞれサイズ`n`のサブvectorに分割します
    int n = N*per_block_ratio;
 
    //サイズ`n`のサブvectorの総数を決定します
    int size = (v.size() - 1) / n + 1;

    //サブvectorを格納するvectorのアレイを作成します
    vector<int> vec[size];
 
    //このループの各反復は、次の`n`要素のセットを処理します
    //そしてそれを`vec`のk番目のインデックスのvectorに格納します
    for (int k = 0; k < size; ++k)
    {
        //次の`n`要素のセットの範囲を取得します
        auto start_itr = next(v.cbegin(), k*n);
        auto end_itr = next(v.cbegin(), k*n + n);
 
        //サブvectorにメモリを割り当てます
        vec[k].resize(n);
 
        //最後のサブvectorを処理するコード
        //含まれる要素が少ない
        if (k*n + n > v.size())
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

    return block_id;
}

/* PageRank 演算 */
unordered_map<int, double> Graph::pagerank(){

    // 変数を定義
    #define D 0.85
    #define E 0.0001

    // 頂点数
    int N = Graph::get_number_of_nodes();

    // 隣接行列のグラフ G 
    unordered_map<int, vector<int>> G = Graph::get_adjacency_list();

    //スコア初期化
    unordered_map<int, double> score;
    for(auto itr = G.begin(); itr != G.end(); ++itr){
        score[itr->first] = 1/N;
    }

    double sub = 1;

    unordered_map<int, double> init_score;
    for(auto itr = G.begin(); itr != G.end(); ++itr){
            init_score[itr->first] = 0;
    }

    // スコア変化が小さくなるまで繰り返し
    while(sub > E)
    {
        // 「prev_score : 今のスコア」, 「score : 次の iteration のスコア」, という状態にする
        unordered_map<int, double> prev_score = init_score;
        swap(score, prev_score);

        // 全ノードに対してスコア分配をシミュレーション
        double dangling_score = 0;
        for(auto itr = G.begin(); itr != G.end(); ++itr){
            int m = G[itr->first].size();
            if (m == 0) { // dangling node の場合
                // dangling node から分配されるスコアを記憶しておく
                dangling_score += D*prev_score[itr->first]/N;
            } else { // そうでない場合
                for (int v : G[itr->first]) { 
                    // 隣接ノードへスコア分配
                    score[v] += D*prev_score[itr->first]/m; 
                }
            }
        }

        for(auto itr = G.begin(); itr != G.end(); ++itr){
            score[itr->first] += dangling_score;
            score[itr->first] += (1.0-D)/N; 
        }

        // 一次ノルムを計算
        sub = 0;
        for(auto itr = G.begin(); itr != G.end(); ++itr){
            sub += abs(prev_score[itr->first] - score[itr->first]); 
        }
    }    

    return score;
}