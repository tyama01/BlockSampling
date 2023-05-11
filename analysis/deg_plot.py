import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 元グラフとサンプリングを格納
G_list = []

# 元グラフ読み込み
graph_name = input("Enter graph name : ")
graph_path = "datasets/Gorder/" + graph_name + "_Gorder.txt"

#有向グラフ
G = nx.read_edgelist(graph_path, create_using=nx.DiGraph, nodetype=int)

#無向グラフ
#G = nx.read_edgelist(graph_path, nodetype=int)

G_list.append(G)

labels_series = [] # サンプリングの種類のラベル
labels_series.append("original")

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
    
    G_list.append(Gs)
    
    labels_series.append(sampling_type)
     

# 次数分布
logx_list = []
logy_list = []

a_list = []
b_list = []

for i in range(len(G_list)):
    degree = dict(G_list[i].degree())
    pos_degree_vals = list(filter(lambda val:val>0, degree.values()))
    uq_pos_degree_vals = sorted(set(pos_degree_vals))
    in_hist = [pos_degree_vals.count(x) for x in uq_pos_degree_vals]

    x = np.asarray(uq_pos_degree_vals, dtype = float)
    y = np.asarray(in_hist, dtype = float)
    
    
    logx = np.log10(x)
    logy = np.log10(y)
    
    logx_list.append(logx)
    logy_list.append(logy)

    a, b = np.polyfit(logx, logy, 1)
    a_list.append(a)
    b_list.append(b)


# ----------------- plot 次数分布全体 ----------------

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
ax.set_xlabel("log10 (Degree)", fontsize=14)
ax.set_ylabel("log10 (Number of nodes)", fontsize=14)

ax.set_xlim(min(logx_list[0]), max(logx_list[0]))

for i in range(len(G_list)):
    scatter_plot = plt.scatter(logx_list[i], logy_list[i],color=cmap(i), s=0.5)
    scatter_plot_regression = ax.plot(logx_list[i], a_list[i]*logx_list[i] + 
                                      b_list[i], label=labels_series[i], color=cmap(i))
    
    

# 凡例を表示する。
ax.legend(loc="upper right")

for i in range(len(a_list)):
    print("a: " + str(a_list[i]))

# 表示
plt.show()

