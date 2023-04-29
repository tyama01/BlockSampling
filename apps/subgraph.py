import networkx as nx
import sys
import os 

# 元グラフ読み込み
graph_name = input("Enter graph name : ")
graph_path = "datasets/Gorder/" + graph_name + ".txt"
G = nx.read_edgelist(graph_path, create_using=nx.DiGraph, nodetype=int)

# PR 上位の頂点を取得
graph_dir = input("Enter graph directory : ")
node_file = input("Enter node file : ") # ファイル名
node_path = "sampling_datasets/" + graph_dir + "/" + node_file + ".txt" 
node_list = []
with open(node_path, "r", encoding="utf-8") as fin:
    for line in fin.readlines():
        try:
            num = int(line)
        except ValueError as e:
            print(e, file=sys.stderr)
            
        node_list.append(num)
        
H = G.subgraph(node_list)

# サンプリングした頂点数      
ns = H.number_of_nodes()
print(ns)

# サンプリンググラフ取得
output_file = input("Sampling graph name : ")
out_path = "sampling_datasets/" + graph_dir + "/" + output_file + ".txt"
nx.write_edgelist(H, out_path, data=False)

# ノードファイルの削除
os.remove(node_path)