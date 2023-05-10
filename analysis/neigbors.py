import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams as rcp

# サンプリングを格納
Gs_list = []

# 元グラフ読み込み
graph_name = input("Enter graph name : ")
graph_path = "datasets/Gorder/" + graph_name + "_Gorder.txt"

# 有向グラフ
G = nx.read_edgelist(graph_path, create_using=nx.DiGraph, nodetype=int)

# 無向グラフ
#G = nx.read_edgelist(graph_path, nodetype=int)

labels_series = [] # サンプリングの種類のラベル

while(True):
    sampling_type = input("Enter Sampling type labels (X quit) : ")
    
    if (sampling_type == 'X'):
        break
    
    data_file = input("Enter Sampling Graph file name : ") # ファイル名
    data_path = "sampling_datasets/" + graph_name + "/" + data_file + ".txt"
    
    # 有向グラフ
    Gs = nx.read_edgelist(data_path, create_using=nx.DiGraph, nodetype=int)
    
    # 無向グラフ
    #Gs = nx.read_edgelist(data_path, nodetype=int)
    
    Gs_list.append(Gs)
    
    labels_series.append(sampling_type)
    
# 元グラフのPR値読み込み 頂点ID のみ(PRが高い順)
node_id = [] # 元グラフの頂点ID 
#pr_dir = input("Enter Real datasets directory : ")
#pr_file = input("Enter Original PR file name : ") # ファイル名
pr_path = "pr_result/" + graph_name+ "/" + graph_name + "_Gorder_pr.txt" 
with open(pr_path) as f:
    for line in f:
        (k, v) = line.split()
        node_id.append(int(k))
        
# 頂点数
N = len(node_id)
x = 0.1 /100 # 0.1 %
x_id = node_id[:int(N*x)] # 上位 x の範囲まで調べる

# 上位の隣接頂点の取得割合を計算
neigbors_ratio_all_list = []
for i in range(len(Gs_list)):
    neigbors_ratio_list = []
    for v in x_id:
        neigbors_ratio = Gs_list[i].degree[v] / G.degree[v]
        neigbors_ratio_list.append(neigbors_ratio)
    neigbors_ratio_all_list.append(neigbors_ratio_list)


#----------------- plot ----------------------- 
# フォントを設定する。
rcp['font.family'] = 'sans-serif'
rcp['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

# カラーマップを用意する。
cmap = plt.get_cmap("tab10")       

# Figureを作成する。
fig = plt.figure()
# Axesを作成する。
ax = fig.add_subplot(111)

# Figureの解像度と色を設定する。
fig.set_dpi(150)
fig.set_facecolor("white")

# Axesのタイトルと色を設定する。
#ax.set_title("物品の所有率")
ax.set_facecolor("white")

# x軸とy軸のラベルを設定する。
ax.set_xlabel("top k%", fontsize=14)
ax.set_ylabel("neigbors ratio", fontsize=14)

# x軸の目盛のラベルの位置を変数xで保持する。
k = np.arange(len(x_id))

# x軸の目盛の位置を設定する。
ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(k*100))

# y軸の範囲を設定する。
ax.set_ylim(0, 1.0)
# y軸の目盛の位置を設定する。
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.05))

for i in range(len(neigbors_ratio_all_list)):
    ax.scatter(k, neigbors_ratio_all_list[i], label = labels_series[i], color=cmap(i))
    ax.plot(k, neigbors_ratio_all_list[i], linestyle = "dashed", color=cmap(i))
    
# グリッドを表示する。
ax.set_axisbelow(True)
ax.grid(True, "major", "y", linestyle="--")

# 凡例を表示する。
ax.legend(loc="upper right")

# グラフを表示する。
plt.show()