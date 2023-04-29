import networkx as nx

# 元グラフ読み込み
graph_name = input("Enter graph name : ")
graph_path = "datasets/Gorder/" + graph_name + ".txt"
G = nx.read_edgelist(graph_path, create_using=nx.DiGraph, nodetype=int)


# PR 上位の頂点を取得
pr_dir = input("Enter PR directory : ")
pr_file = input("Enter PR name : ") # ファイル名
pr_path = "pr_result/" + pr_dir + "/" + pr_file + ".txt" 
pr_list = []
with open(pr_path) as f:
    for line in f:
        (k, v) = line.split()
        pr_list.append(int(k))

# 頂点数      
n = G.number_of_nodes()

# PR 上位を取得 sampling_rate 分
sampling_rate = 0.3 # サンプリング割合
size = int(n * sampling_rate)
H = G.subgraph(pr_list[:size])

# サンプリングした頂点数      
ns = H.number_of_nodes()
print(ns)

# PR-top グラフ取得
output_file = input("PR-top graph name : ")
out_path = "sampling_datasets/" + pr_dir + "/" + output_file + ".txt"
nx.write_edgelist(H, out_path, data=False)
