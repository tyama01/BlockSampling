import networkx as nx

G = nx.read_edgelist("../datasets/web-Google.txt", create_using=nx.DiGraph, nodetype=int)

bc = nx.pagerank(G, alpha=0.85)

# bc 結果出力
f = open('../pr_result/Google_pr_result_py.txt', 'a', encoding='UTF-8')
for tmp_bc in sorted(bc.items(), key=lambda x:x[1], reverse=True):
    f.write(str(tmp_bc[0]))
    f.write(' ')
    f.write(str(tmp_bc[1]))
    f.write('\n')
