import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import linregress
from matplotlib import rcParams as rcp
from matplotlib import rcParams

# 元グラフ読み込み
graph_name = input("Enter graph name : ")
graph_path = "datasets/Gorder/" + graph_name + "_Gorder.txt"

#有向グラフ
G = nx.read_edgelist(graph_path, create_using=nx.DiGraph, nodetype=int)

#無向グラフ
#G = nx.read_edgelist(graph_path, nodetype=int)


labels_series = [] # サンプリングの種類のラベル
labels_series.append("original")

# サンプリンググラフのリスト [[block グラフ 10~40], [pr_top 10 ~ 40]]
Gs_list = []

while(True):
    sampling_type = input("Enter Sampling type labels (X quit) : ")
    
    if (sampling_type == 'X'):
        break
    
    labels_series.append(sampling_type)
    Gs_size_list = [] # サンプリンググラフサイズごとに格納
    
    while(True):
        data_file = input("Enter Sampling Graph file name (X quit) : ") # ファイル名
        if(data_file == 'X'):
            break
        
        data_path = "sampling_datasets/" + graph_name + "/" + data_file + ".txt"
        
        # 有向グラフ
        Gs = nx.read_edgelist(data_path, create_using=nx.DiGraph, nodetype=int)
        
        # 無向グラフ
        #Gs = nx.read_edgelist(data_path, nodetype=int)
        
        Gs_size_list.append(Gs)
    
    Gs_list.append(Gs_size_list)

# 元グラフの grad を計算
degree = dict(G.degree())
pos_degree_vals = list(filter(lambda val:val>0, degree.values()))
uq_pos_degree_vals = sorted(set(pos_degree_vals))
in_hist = [pos_degree_vals.count(x) for x in uq_pos_degree_vals]

x = np.asarray(uq_pos_degree_vals, dtype = float)
y = np.asarray(in_hist, dtype = float)


logx = np.log10(x)
logy = np.log10(y)

a, b = np.polyfit(logx, logy, 1)
print(a)

# 元グラフの grad をサンプリングサイズ分追加
G_grad = []
for i in range(4):
    G_grad.append(-a)
    
# grad_data
grad_data = [] # [[元グラフの傾き], [Block の傾き], [pr_top の傾き]
grad_data.append(G_grad)

# サンプリンググラフの傾きを計算
for i in range(len(Gs_list)):
    a_list = []
    for j in range(len(Gs_list[0])):
        degree = dict(Gs_list[i][j].degree())
        pos_degree_vals = list(filter(lambda val:val>0, degree.values()))
        uq_pos_degree_vals = sorted(set(pos_degree_vals))
        in_hist = [pos_degree_vals.count(x) for x in uq_pos_degree_vals]

        x = np.asarray(uq_pos_degree_vals, dtype = float)
        y = np.asarray(in_hist, dtype = float)
        
        
        logx = np.log10(x)
        logy = np.log10(y)
        

        a, b = np.polyfit(logx, logy, 1)
        a_list.append(-a)
        
    grad_data.append(a_list)
    
       

# ------------------ grad plot -------------------------

labels_data = ["10%", "20%", "30%", "40%"]

rcParams['pdf.fonttype'] = 42

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
ax.set_xlabel("Graph size", fontsize=14)
ax.set_ylabel("gamma", fontsize=14)

# x軸の目盛のラベルの位置を変数xで保持する。
x = np.arange(len(labels_data))

# x軸の目盛の位置を設定する。
ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(x))
# x軸の目盛のラベルを設定する。
ax.xaxis.set_major_formatter(mpl.ticker.FixedFormatter(labels_data))

# y軸の範囲を設定する。
ax.set_ylim(1.5, 2.5)
# y軸の目盛の位置を設定する。
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))
# y軸の目盛のラベルを設定する。
#ax.yaxis.set_major_formatter(mpl.ticker.PercentFormatter())

ax.plot(x, grad_data[0], label = labels_series[0], linestyle="solid", color=cmap(0))

for i in range(1, (len(Gs_list) + 1)):
    ax.scatter(x, grad_data[i], label = labels_series[i], color=cmap(i))
    ax.plot(x, grad_data[i], linestyle = "dashed", color=cmap(i))
    
# グリッドを表示する。
ax.set_axisbelow(True)
ax.grid(True, "major", "y", linestyle="--")

# 凡例を表示する。
ax.legend(loc="upper right")

# グラフを表示する。
plt.show()