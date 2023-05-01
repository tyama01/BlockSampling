import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams as rcp
from ndcg import *

# 元グラフのPR値読み込み
pr_original = {} # 元グラフの頂点ID と PR値を辞書型で保持
pr_dir = input("Enter Real datasets directory : ")
pr_file = input("Enter Original PR file name : ") # ファイル名
pr_path = "pr_result/" + pr_dir + "/" + pr_file + "_pr.txt" 
with open(pr_path) as f:
    for line in f:
        (k, v) = line.split()
        pr_original[int(k)] = float(v)
        
# サンプリンググラフのPR値読み込み
pr_sample_nest = {} # サンプリングの種類とPR値を辞書型で保持
while(True):
    sampling_type = input("Enter Sampling type labels (X quit) : ")
    
    if(sampling_type == 'X'):
        break
    
    pr_sample = {} # 元グラフの頂点ID と PR値を辞書型で保持
    pr_file = input("Enter Sampling PR file name : ") # ファイル名
    pr_path = "pr_result/" + pr_dir + "/" + pr_file + "_pr.txt" 
    with open(pr_path) as f:
        for line in f:
            (k, v) = line.split()
            pr_sample[int(k)] = float(v)
    
    pr_sample_nest[sampling_type] = pr_sample # e.g., {pr_top : {id : pr_value}}


# nDCG を計算
ndcg_result_dic = {}
r_list = [0.0001, 0.001, 0.01, 0.1] # 0.001%, 00.1%, 0.1%, 1%
for key in pr_sample_nest.keys():
    ndcg_result = []
    for r in r_list:
        ndcg_value = ndcg_tyama(pr_original, pr_sample_nest[key], r)
        ndcg_result.append(ndcg_value)
        
    ndcg_result_dic[key] = ndcg_result
    

# --------------------Plot------------------------
# フォントを設定する。
rcp['font.family'] = 'sans-serif'
rcp['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

# カラーマップを用意する。
cmap = plt.get_cmap("tab10")

labels_series = [] # サンプリングの種類のラベル
for key in ndcg_result_dic.keys():
    labels_series.append(key)
    
labels_data = ["0.001%", "00.1%", "0.1%", "1%"] # nDCG 適用範囲ラベル

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
ax.set_xlabel("nDCG top x%", fontsize=14)
ax.set_ylabel("nDCG value", fontsize=14)

# x軸の目盛のラベルの位置を変数xで保持する。
x = np.arange(len(labels_data))

# x軸の目盛の位置を設定する。
ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(x))
# x軸の目盛のラベルを設定する。
ax.xaxis.set_major_formatter(mpl.ticker.FixedFormatter(labels_data))

# y軸の範囲を設定する。
ax.set_ylim(0.9, 1.0)
# y軸の目盛の位置を設定する。
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.01))
# y軸の目盛のラベルを設定する。
#ax.yaxis.set_major_formatter(mpl.ticker.PercentFormatter())

# nDCG の結果をdata 配列に入れる
data = []
for key in ndcg_result_dic.keys():
    data.append(ndcg_result_dic[key])
    
    
for i in range(len(data)):
    ax.scatter(x, data[i], label = labels_series[i], color=cmap(i + 1))
    ax.plot(x, data[i], linestyle = "dashed", color=cmap(i + 1))

# グリッドを表示する。
ax.set_axisbelow(True)
ax.grid(True, "major", "y", linestyle="--")

# 凡例を表示する。
ax.legend(loc="lower left")

# グラフを表示する。
plt.show()


#output_file = input("figure name : ")
#output_path = ("analysis_data/" + pr_dir + "/" + output_file + ".pdf")
#plt.savefig(output_path)    